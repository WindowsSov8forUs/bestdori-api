'''`bestdori.ayachan.utils.network`

向 ayachan 发送请求相关模块'''
from json import dumps
from io import BufferedReader
from httpx import Response, Request, Client
from typing import Any, Union, Literal, Optional, cast

from ._settings import settings
from ...exceptions import AssetsNotExistError

# 向 ayachan 发送 API 请求类
class Api:
    '''向 ayachan 发送 API 请求类

    参数:
        api (str): 请求的 API 地址
        proxy (Optional[Union[dict[str, str], str]]): 代理服务器
    '''
    api: str
    '''请求的 API 地址'''
    proxy: Optional[Union[dict[str, str], str]]=None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        api: str,
        proxy: Optional[Union[dict[str, str], str]]=None
    ) -> None:
        '''初始化'''
        self.api = api
        self.proxy = proxy or settings.proxy
        return
    
    # 请求发送
    def request(
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
        # 处理接收到的 API
        if self.api.startswith('http://') or self.api.startswith('https://'):
            self.api = self.api
        else:
            self.api = 'https://api.ayachan.fun/' + self.api
        # 构建一个请求体
        request = Request(
            method,
            self.api,
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
        return response

# 获取 ayachan 资源数据
class Assets:
    '''获取 Bestdori 资源数据

    参数:
        url (str): 请求的资源地址
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
            proxy (Optional[Union[dict[str, str], str]]): 代理服务器
        '''
        self.url = url
        self.proxy = proxy or settings.proxy
        return
    
    # 获取资源连接
    def get_url(self) -> str:
        '''获取资源连接

        返回:
            str: 获取的资源连接 `str`
        '''
        # 处理接收到的 URL
        if self.api.startswith('http://') or self.api.startswith('https://'):
            self.api = self.api
        else:
            self.api = 'https://api.ayachan.fun/' + self.api
        return self.url
    
    # 获取资源
    def get(self) -> bytes:
        '''获取资源

        返回:
            bytes: 获取的资源字节数据 `bytes`
        '''
        # 处理接收到的 URL
        if self.api.startswith('http://') or self.api.startswith('https://'):
            self.api = self.api
        else:
            self.api = 'https://api.ayachan.fun/' + self.api
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
