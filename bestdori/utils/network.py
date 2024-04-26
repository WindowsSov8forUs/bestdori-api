'''`bestdori.utils.network`

向 Bestdori 发送请求相关模块'''
from json import dumps
from io import BufferedReader
from http.cookies import SimpleCookie
from typing import Any, Union, Literal, Optional, cast

from httpx import HTTPStatusError
from aiohttp import ClientResponseError
from aiohttp import ClientSession, ClientResponse
from httpx import Client, Request, Response, AsyncClient

from bestdori import settings
from bestdori.exceptions import (
    REQUEST_EXCEPTION,
    RequestException,
    NoContentTypeError,
    AssetsNotExistError
)

# 向 Bestdori 发送 API 请求类
class Api:
    '''向 Bestdori 发送 API 请求类

    参数:
        api (str): 请求的 API 地址
    '''
    api: str
    '''请求的 API 地址'''
    headers: dict[str, str]
    '''请求头'''
    _proxies: Optional[dict[str, str]] = None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        api: str
    ) -> None:
        '''初始化'''
        self.api = api
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}
        if isinstance(settings.proxy, str):
            self._proxies = {'http://': settings.proxy, 'https://': settings.proxy}
        elif isinstance(settings.proxy, dict):
            self._proxies = settings.proxy
        
        return
    
    # 处理 url
    @property
    def _url(self) -> str:
        # 处理接收到的 API
        _url = self.api
        if self.api.startswith('http://') or self.api.startswith('https://'):
            return _url
        else:
            _url = 'https://bestdori.com/api/' + self.api
            return _url
    
    # 请求发送
    def _request(
        self,
        method: Literal['get', 'post'],
        *,
        cookies: Optional[SimpleCookie]=None,
        params: Optional[dict[str, Any]]=None,
        data: Optional[dict[str, Any]]=None,
        files: Optional[dict[str, tuple[str, BufferedReader]]]=None
    ) -> Response:
        '''请求发送

        参数:
            method (Literal[&#39;get&#39;, &#39;post&#39;]): API 调用方法
            cookies (Optional[Cookies], optional): Cookies
            params (Optional[dict[str, Any]], optional): 调用参数
            data (Optional[dict[str, Any]], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader]]], optional): 发送文件参数

        返回:
            Response: 收到的响应
        '''
        # 构建一个请求体
        request = Request(
            method,
            self._url,
            cookies=dict(cookies) if cookies is not None else None, # type: ignore
            params=params,
            data=cast(dict, dumps(data)) if data is not None else data,
            files=files,
            headers=self.headers if not self.api.endswith('/upload') else None
        )
        # 发送请求并获取响应
        with Client(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        # 处理接收到的响应
        response.raise_for_status()
        # 判断接收到的响应是否为 json 格式
        if 'application/json' not in (content_type := response.headers.get('content-type', '')):
            if content_type != '':
                return response
            else:
                raise NoContentTypeError(response.url.path)
        
        if isinstance((response_data := response.json()), dict):
            if (result := response_data.get('result', None)) is not None:
                if result is False:
                    if (code := response_data.get('code', None)) is not None:
                        if code in REQUEST_EXCEPTION.keys(): # 若错误码已被记录
                            exception_class = REQUEST_EXCEPTION[code]
                            if params is not None:
                                raise exception_class(self.api, **params)
                            elif data is not None:
                                raise exception_class(self.api, **data)
                            else:
                                raise exception_class(self.api)
                        else:
                            raise RequestException(self.api, code)
                    else:
                        raise RequestException(self.api)
        return response
    
    # 异步请求发送
    async def _request_async(
        self,
        method: Literal['get', 'post'],
        *,
        cookies: Optional[SimpleCookie]=None,
        params: Optional[dict[str, Any]]=None,
        data: Optional[dict[str, Any]]=None,
        files: Optional[dict[str, tuple[str, BufferedReader]]]=None
    ) -> Union[Response, ClientResponse]:
        '''请求发送

        参数:
            method (Literal[&#39;get&#39;, &#39;post&#39;]): API 调用方法
            cookies (Optional[Cookies], optional): Cookies
            params (Optional[dict[str, Any]], optional): 调用参数
            data (Optional[dict[str, Any]], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader]]], optional): 发送文件参数

        返回:
            Union[Response, ClientResponse]: 收到的响应
        '''
        if settings.async_client == settings.AsyncClient.HTTPX:
            # 构建一个请求体
            request = Request(
                method,
                self._url,
                cookies=dict(cookies) if cookies is not None else None, # type: ignore
                params=params,
                data=cast(dict, dumps(data)) if data is not None else data,
                files=files,
                headers=self.headers if not self.api.endswith('/upload') else None
            )
            # 发送请求并获取响应
            async with AsyncClient(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
                response = await client.send(request)
        
                # 处理接收到的响应
                response.raise_for_status()
        else:
            async with ClientSession() as session:
                response = await session.request(
                    method,
                    self._url,
                    cookies=cookies,
                    params=params,
                    data=cast(dict, dumps(data)) if data is not None else data,
                    headers=self.headers if not self.api.endswith('/upload') else None
                )
                response.raise_for_status()
        
        # 判断接收到的响应是否为 json 格式
        if 'application/json' not in (content_type := response.headers.get('content-type', '')):
            if content_type != '':
                return response
            else:
                raise NoContentTypeError(response.url.path)
        
        if isinstance((response_data := response.json()), dict):
            if (result := response_data.get('result', None)) is not None:
                if result is False:
                    if (code := response_data.get('code', None)) is not None:
                        if code in REQUEST_EXCEPTION.keys(): # 若错误码已被记录
                            exception_class = REQUEST_EXCEPTION[code]
                            if params is not None:
                                raise exception_class(self.api, **params)
                            elif data is not None:
                                raise exception_class(self.api, **data)
                            else:
                                raise exception_class(self.api)
                        else:
                            raise RequestException(self.api, code)
                    else:
                        raise RequestException(self.api)
        return response
    
    def get(
        self,
        *,
        cookies: Optional[SimpleCookie]=None,
        params: Optional[dict[str, Any]]=None
    ) -> Response:
        '''发送 GET 请求

        参数:
            cookies (Optional[Cookies], optional): Cookies
            params (Optional[dict[str, Any]], optional): 调用参数

        返回:
            Response: 收到的响应
        '''
        return self._request('get', cookies=cookies, params=params)
    
    def post(
        self,
        *,
        cookies: Optional[SimpleCookie]=None,
        data: Optional[dict[str, Any]]=None,
        files: Optional[dict[str, tuple[str, BufferedReader]]]=None
    ) -> Response:
        '''发送 POST 请求

        参数:
            cookies (Optional[Cookies], optional): Cookies
            data (Optional[dict[str, Any]], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader]]], optional): 发送文件参数

        返回:
            Response: 收到的响应
        '''
        return self._request('post', cookies=cookies, data=data, files=files)

    async def aget(
        self,
        *,
        cookies: Optional[SimpleCookie]=None,
        params: Optional[dict[str, Any]]=None
    ) -> Union[Response, ClientResponse]:
        '''发送 GET 请求

        参数:
            cookies (Optional[Cookies], optional): Cookies
            params (Optional[dict[str, Any]], optional): 调用参数

        返回:
            Union[Response, ClientResponse]: 收到的响应
        '''
        return await self._request_async('get', cookies=cookies, params=params)
    
    async def apost(
        self,
        *,
        cookies: Optional[SimpleCookie]=None,
        data: Optional[dict[str, Any]]=None,
        files: Optional[dict[str, tuple[str, BufferedReader]]]=None
    ) -> Union[Response, ClientResponse]:
        '''发送 POST 请求

        参数:
            cookies (Optional[Cookies], optional): Cookies
            data (Optional[dict[str, Any]], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader]]], optional): 发送文件参数

        返回:
            Union[Response, ClientResponse]: 收到的响应
        '''
        return await self._request_async('post', cookies=cookies, data=data, files=files)

# 获取 Bestdori 资源数据
class Assets:
    '''获取 Bestdori 资源数据

    参数:
        url (str): 请求的资源地址
        server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 资源所在服务器
    '''
    url: str
    '''请求的资源地址'''
    server: Literal['jp', 'en', 'tw', 'cn', 'kr', 'llsif']
    '''资源所在服务器'''
    _proxies: Optional[dict[str, str]] = None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        url: str,
        server: Literal['jp', 'en', 'tw', 'cn', 'kr', 'llsif']
    ) -> None:
        '''获取 Bestdori 资源数据

        参数:
            url (str): 请求的资源地址
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;, &#39;llsif&#39;]): 资源所在服务器
        '''
        self.url = url
        self.server = server
        if isinstance(settings.proxy, str):
            self._proxies = {'http://': settings.proxy, 'https://': settings.proxy}
        elif isinstance(settings.proxy, dict):
            self._proxies = settings.proxy
        
        return
    
    # 获取资源连接
    def get_url(self) -> str:
        '''获取资源连接

        返回:
            str: 获取的资源连接 `str`
        '''
        # 如果服务器为 llsif 则转接方法
        if self.server == 'llsif':
            return self._get_niconi_url()
        
        # 处理接收到的 URL
        if self.url.startswith('http://') or self.url.startswith('https://'):
            self.url = self.url
        else:
            self.url = f'https://bestdori.com/assets/{self.server}/' + self.url
        return self.url
    
    # 从 card.niconi.co.ni 获取资源连接
    def _get_niconi_url(self) -> str:
        '''从 card.niconi.co.ni 获取资源连接

        返回:
            str: 获取的资源连接 `str`
        '''
        # 处理接收到的 URL
        if self.url.startswith('http://') or self.url.startswith('https://'):
            self.url = self.url
        else:
            self.url = f'https://card.niconi.co.ni/asset/' + self.url
        return self.url
    
    # 获取资源
    def get(self) -> bytes:
        '''获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        # 如果服务器为 llsif 则转接方法
        if self.server == 'llsif':
            return self._get_from_niconi()
        
        # 构建一个请求体
        request = Request('get', self.get_url())
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        try:
            response.raise_for_status()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise AssetsNotExistError(self.url)
            else:
                raise exception
        
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        return response.content
    
    # 异步获取资源
    async def aget(self) -> bytes:
        '''获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        # 如果服务器为 llsif 则转接方法
        if self.server == 'llsif':
            return await self._get_from_niconi_async()
        
        if settings.async_client == settings.AsyncClient.HTTPX:
            # 构建一个请求体
            request = Request('get', self.get_url())
            # 发送请求并获取响应
            async with AsyncClient(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
                response = await client.send(request)
            try:
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == 404:
                    raise AssetsNotExistError(self.url)
                else:
                    raise exception
        else:
            # 发送请求并获取响应
            async with ClientSession() as session:
                response = await session.request(
                    'get',
                    self.get_url(),
                    proxy=self._proxies,
                )
                try:
                    response.raise_for_status()
                except ClientResponseError as exception:
                    if exception.status == 404:
                        raise AssetsNotExistError(self.url)
                    else:
                        raise exception
        
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        
        if isinstance(response, Response):
            return response.content
        else:
            return await response.read()
    
    # 从 card.niconi.co.ni 获取资源
    def _get_from_niconi(self) -> bytes:
        '''从 card.niconi.co.ni 获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        # 构建一个请求体
        request = Request('get', self.get_url())
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        try:
            response.raise_for_status()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise AssetsNotExistError(self.url)
            else:
                raise exception
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        return response.content
    
    async def _get_from_niconi_async(self) -> bytes:
        '''从 card.niconi.co.ni 获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        if settings.async_client == settings.AsyncClient.HTTPX:
            # 构建一个请求体
            request = Request('get', self.get_url())
            # 发送请求并获取响应
            async with AsyncClient(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
                response = await client.send(request)
            try:
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == 404:
                    raise AssetsNotExistError(self.url)
                else:
                    raise exception
        else:
            # 发送请求并获取响应
            async with ClientSession() as session:
                response = await session.request(
                    'get',
                    self.get_url(),
                    proxy=self._proxies,
                )
                try:
                    response.raise_for_status()
                except ClientResponseError as exception:
                    if exception.status == 404:
                        raise AssetsNotExistError(self.url)
                    else:
                        raise exception
        
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        
        if isinstance(response, Response):
            return response.content
        else:
            return await response.read()

# 获取 Bestdori res 资源数据
class Res:
    '''获取 Bestdori res 资源数据

    参数:
        url (str): 请求的 res 资源地址
    '''
    url: str
    '''请求的资源地址'''
    _proxies: Optional[dict[str, str]]=None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        url: str
    ) -> None:
        '''获取 Bestdori 资源数据

        参数:
            url (str): 请求的资源地址
        '''
        self.url = url
        if isinstance(settings.proxy, str):
            self._proxies = {'http://': settings.proxy, 'https://': settings.proxy}
        elif isinstance(settings.proxy, dict):
            self._proxies = settings.proxy
        return
    
    @property
    def _url(self) -> str:
        # 处理接收到的 URL
        if self.url.startswith('http://') or self.url.startswith('https://'):
            return self.url
        else:
            return f'https://bestdori.com/res/' + self.url
    
    # 获取资源
    def get(self) -> bytes:
        '''获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        # 构建一个请求体
        request = Request(
            'get',
            self._url
        )
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        try:
            response.raise_for_status()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise AssetsNotExistError(self.url)
            else:
                raise exception
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        return response.content
    
    # 异步获取资源
    async def aget(self) -> bytes:
        '''获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        if settings.async_client == settings.AsyncClient.HTTPX:
            # 构建一个请求体
            request = Request(
                'get',
                self._url
            )
            # 发送请求并获取响应
            async with AsyncClient(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
                response = await client.send(request)
            try:
                response.raise_for_status()
            except HTTPStatusError as exception:
                if exception.response.status_code == 404:
                    raise AssetsNotExistError(self.url)
                else:
                    raise exception
        else:
            # 发送请求并获取响应
            async with ClientSession() as session:
                response = await session.request(
                    'get',
                    self._url,
                    proxy=self._proxies,
                )
                try:
                    response.raise_for_status()
                except ClientResponseError as exception:
                    if exception.status == 404:
                        raise AssetsNotExistError(self.url)
                    else:
                        raise exception
        
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        
        if isinstance(response, Response):
            return response.content
        else:
            return await response.read()
