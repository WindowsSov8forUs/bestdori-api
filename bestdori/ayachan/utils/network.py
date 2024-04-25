'''`bestdori.ayachan.utils.network`

向 ayachan 发送请求相关模块'''
from json import dumps
from io import BufferedReader
from typing import Any, Union, Literal, Optional, cast

from httpx import HTTPStatusError
from aiohttp import ClientResponseError
from aiohttp import ClientSession, ClientResponse
from httpx import Client, Request, Response, AsyncClient

from . import settings
from bestdori.exceptions import AssetsNotExistError
from bestdori.settings import AsyncClient as ClientSetting

# 向 ayachan 发送 API 请求类
class Api:
    '''向 ayachan 发送 API 请求类

    参数:
        api (str): 请求的 API 地址
    '''
    api: str
    '''请求的 API 地址'''
    _proxies: Optional[Union[dict[str, str], str]]=None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        api: str
    ) -> None:
        '''初始化'''
        self.api = api
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
        if _url.startswith('http://') or _url.startswith('https://'):
            return _url
        else:
            _url = 'https://api.ayachan.fun/' + self.api
            return _url
    
    # 请求发送
    def _request(
        self,
        method: Literal['get', 'post'],
        *,
        params: Optional[dict[str, Any]]=None,
        data: Optional[Any]=None,
        files: Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]]=None,
        json: Optional[Any]=None
    ) -> Response:
        '''请求发送

        参数:
            method (Literal[&#39;get&#39;, &#39;post&#39;]): API 调用方法
            params (Optional[dict[str, Any]], optional): 调用参数
            data (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]], optional): 发送文件参数
            json (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送

        返回:
            Response: 收到的响应
        '''
        # 构建一个请求体
        request = Request(
            method,
            self._url,
            params=params,
            data=(
                cast(dict, dumps(data)) if data is not None and 'sonolus' not in self.api
                else data
            ),
            files=files,
            json=json,
            headers=(
                {
                    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxjpDgorEXUAUIbBN'
                } if 'sonolus' in self.api and method == 'post' else None
            )
        )
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        # 处理接收到的响应
        response.raise_for_status()
        return response
    
    # 异步请求发送
    async def _request_async(
        self,
        method: Literal['get', 'post'],
        *,
        params: Optional[dict[str, Any]]=None,
        data: Optional[Any]=None,
        files: Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]]=None,
        json: Optional[Any]=None
    ) -> Union[Response, ClientResponse]:
        '''请求发送

        参数:
            method (Literal[&#39;get&#39;, &#39;post&#39;]): API 调用方法
            params (Optional[dict[str, Any]], optional): 调用参数
            data (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]], optional): 发送文件参数
            json (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送

        返回:
            Response: 收到的响应
        '''
        if settings.async_client == ClientSetting.HTTPX:
            # 构建一个请求体
            request = Request(
                method,
                self._url,
                params=params,
                data=(
                    cast(dict, dumps(data)) if data is not None and 'sonolus' not in self.api
                    else data
                ),
                files=files,
                json=json,
                headers=(
                    {
                        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxjpDgorEXUAUIbBN'
                    } if 'sonolus' in self.api and method == 'post' else None
                )
            )
            
            # 发送请求并获取响应
            async with AsyncClient(proxies=cast(dict, self._proxies), timeout=settings.timeout, trust_env=False) as client:
                response = await client.send(request)
            
                # 处理接收到的响应
                response.raise_for_status()
        else:
            async with ClientSession() as session:
                async with session.request(
                    method,
                    self._url,
                    params=params,
                    data=(
                        cast(dict, dumps(data)) if data is not None and 'sonolus' not in self.api
                        else data
                    ),
                    files=files,
                    json=json,
                    headers=(
                        {
                            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxjpDgorEXUAUIbBN'
                        } if 'sonolus' in self.api and method == 'post' else None
                    )
                ) as response:
                    response.raise_for_status()
        
        return response

    def get(
        self,
        params: Optional[dict[str, Any]]=None
    ) -> Response:
        '''发送 GET 请求

        参数:
            params (Optional[dict[str, Any]], optional): 调用参数

        返回:
            Response: 收到的响应
        '''
        return self._request('get', params=params)
    
    async def aget(
        self,
        params: Optional[dict[str, Any]]=None
    ) -> Union[Response, ClientResponse]:
        '''发送 GET 请求

        参数:
            params (Optional[dict[str, Any]], optional): 调用参数

        返回:
            Response: 收到的响应
        '''
        return await self._request_async('get', params=params)
    
    def post(
        self,
        data: Optional[Any]=None,
        files: Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]]=None,
        json: Optional[Any]=None
    ) -> Response:
        '''发送 POST 请求

        参数:
            data (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]], optional): 发送文件参数
            json (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送

        返回:
            Response: 收到的响应
        '''
        return self._request('post', data=data, files=files, json=json)
    
    async def apost(
        self,
        data: Optional[Any]=None,
        files: Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]]=None,
        json: Optional[Any]=None
    ) -> Union[Response, ClientResponse]:
        '''发送 POST 请求

        参数:
            data (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]], optional): 发送文件参数
            json (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送

        返回:
            Response: 收到的响应
        '''
        return await self._request_async('post', data=data, files=files, json=json)

# 获取 ayachan 资源数据
class Assets:
    '''获取 Bestdori 资源数据

    参数:
        url (str): 请求的资源地址
        proxy (Optional[Union[dict[str, str], str]]): 代理服务器
    '''
    url: str
    '''请求的资源地址'''
    _proxies: Optional[Union[dict[str, str], str]]=None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        url: str
    ) -> None:
        '''获取 Bestdori 资源数据

        参数:
            url (str): 请求的资源地址
            proxy (Optional[Union[dict[str, str], str]]): 代理服务器
        '''
        self.url = url
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
        # 处理接收到的 URL
        if self.url.startswith('http://') or self.url.startswith('https://'):
            return self.url
        else:
            return 'https://api.ayachan.fun/' + self.url
    
    # 获取资源
    def get(self) -> bytes:
        '''获取资源

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
    
    # 异步获取资源
    async def aget(self) -> bytes:
        '''获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        if settings.async_client == ClientSetting.HTTPX:
            # 构建一个请求体
            request = Request('get', self.url)
            
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
        return await response.read()
