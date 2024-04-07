'''`bestdori.utils.network`

向 Bestdori 发送请求相关模块'''
from json import dumps
from io import BufferedReader
from typing import Any, Union, Literal, Optional, cast

from httpx._models import Cookies
from httpx import Response, Request, Client

from ._settings import settings
from ..exceptions import (
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
        proxy (Optional[Union[dict[str, str], str]]): 代理服务器
    '''
    api: str
    '''请求的 API 地址'''
    proxy: Optional[Union[dict[str, str], str]]=None
    '''代理服务器'''
    headers: dict[str, str]
    '''请求头'''
    # 初始化
    def __init__(
        self,
        api: str,
        proxy: Optional[Union[dict[str, str], str]]=None
    ) -> None:
        '''初始化'''
        self.api = api
        self.proxy = proxy or settings.proxy
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}
        return
    
    # 请求发送
    def request(
        self,
        method: Literal['get', 'post'],
        *,
        cookies: Optional[Cookies]=None,
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
        # 处理接收到的 API
        if self.api.startswith('http://') or self.api.startswith('https://'):
            self.api = self.api
        else:
            self.api = 'https://bestdori.com/api/' + self.api
        # 构建一个请求体
        request = Request(
            method,
            self.api,
            cookies=cookies,
            params=params,
            data=cast(dict, dumps(data)) if data is not None else data,
            files=files,
            headers=self.headers if not self.api.endswith('/upload') else None
        )
        # 构建代理服务器字典
        if self.proxy is not None:
            proxies = {'http://': self.proxy, 'https://': self.proxy}
        else:
            proxies = None
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        # 处理接收到的响应
        response.raise_for_status()
        # 判断接收到的响应是否为 json 格式
        if 'application/json' not in (content_type := response.headers.get('content-type', None)):
            if content_type is not None:
                return response
            else:
                raise NoContentTypeError(response)
        
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

# 获取 Bestdori 资源数据
class Assets:
    '''获取 Bestdori 资源数据

    参数:
        url (str): 请求的资源地址
        server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 资源所在服务器
        proxy (Optional[Union[dict[str, str], str]]): 代理服务器
    '''
    url: str
    '''请求的资源地址'''
    server: Literal['jp', 'en', 'tw', 'cn', 'kr', 'llsif']
    '''资源所在服务器'''
    proxy: Optional[Union[dict[str, str], str]]=None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        url: str,
        server: Literal['jp', 'en', 'tw', 'cn', 'kr', 'llsif'],
        proxy: Optional[Union[dict[str, str], str]]=None
    ) -> None:
        '''获取 Bestdori 资源数据

        参数:
            url (str): 请求的资源地址
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;, &#39;llsif&#39;]): 资源所在服务器
            proxy (Optional[Union[dict[str, str], str]]): 代理服务器
        '''
        self.url = url
        self.server = server
        self.proxy = proxy or settings.proxy
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
        
        # 处理接收到的 URL
        if self.url.startswith('http://') or self.url.startswith('https://'):
            self.url = self.url
        else:
            self.url = f'https://bestdori.com/assets/{self.server}/' + self.url
        # 构建一个请求体
        request = Request('get', self.url)
        # 构建代理服务器字典
        if self.proxy is not None:
            proxies = {'http://': self.proxy, 'https://': self.proxy}
        else:
            proxies = None
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        response.raise_for_status()
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        return response.content
    
    # 从 card.niconi.co.ni 获取资源
    def _get_from_niconi(self) -> bytes:
        '''从 card.niconi.co.ni 获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        # 处理接收到的 URL
        if self.url.startswith('http://') or self.url.startswith('https://'):
            self.url = self.url
        else:
            self.url = f'https://card.niconi.co.ni/asset/' + self.url
        # 构建一个请求体
        request = Request('get', self.url)
        # 构建代理服务器字典
        if self.proxy is not None:
            proxies = {'http://': self.proxy, 'https://': self.proxy}
        else:
            proxies = None
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        response.raise_for_status()
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        return response.content

# 获取 Bestdori res 资源数据
class Res:
    '''获取 Bestdori res 资源数据

    参数:
        url (str): 请求的 res 资源地址
        proxy (Optional[Union[dict[str, str], str]]): 代理服务器
    '''
    url: str
    '''请求的资源地址'''
    proxy: Optional[Union[dict[str, str], str]]=None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        url: str,
        proxy: Optional[Union[dict[str, str], str]]=None
    ) -> None:
        '''获取 Bestdori 资源数据

        参数:
            url (str): 请求的资源地址
            proxy (Optional[str]): 代理服务器
        '''
        self.url = url
        self.proxy = proxy or settings.proxy
        return
    
    # 获取资源
    def get(self) -> bytes:
        '''获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        # 处理接收到的 URL
        if self.url.startswith('http://') or self.url.startswith('https://'):
            self.url = self.url
        else:
            self.url = f'https://bestdori.com/res/' + self.url
        # 构建一个请求体
        request = Request(
            'get',
            self.url
        )
        # 构建代理服务器字典
        if self.proxy is not None:
            proxies = {'http://': self.proxy, 'https://': self.proxy}
        else:
            proxies = None
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, proxies), timeout=settings.timeout, trust_env=False) as client:
            response = client.send(request)
        
        response.raise_for_status()
        # 检测响应资源是否存在
        content_type = response.headers.get('content-type', None)
        if content_type is None or content_type == 'text/html':
            raise AssetsNotExistError(self.url)
        return response.content
