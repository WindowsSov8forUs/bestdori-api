'''HTTP 客户端类型基类'''

from yarl import URL
from json import loads
from io import BufferedReader
from multidict import CIMultiDict
from abc import ABC, abstractmethod
from http.cookiejar import CookieJar
from typing import Any, Dict, Self, Tuple, Union, Optional, TypeAlias

from bestdori.exceptions import HTTPStatusError

FilesContent: TypeAlias = Dict[str, Tuple[str, BufferedReader, Optional[str]]]

class Request:
    '''HTTP 请求类'''
    
    def __init__(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[CIMultiDict[str]]=None,
        cookies: Optional[CookieJar]=None,
        params: Optional[Dict[str, Any]]=None,
        data: Optional[Any]=None,
        files: Optional[FilesContent]=None,
        json: Optional[Any]=None,
    ) -> None:
        self.method = method
        '''请求方法'''
        self.url = URL(url)
        '''请求 URL'''
        self.headers = headers
        '''请求头'''
        self.cookies = cookies
        '''请求 Cookie'''
        self.params = params
        '''请求参数'''
        self.data = data
        '''请求数据'''
        self.files = files
        '''请求文件'''
        self.json = json
        '''请求 JSON 数据'''

class Response:
    '''HTTP 响应类'''
    
    def __init__(
        self,
        request: Request,
        headers: CIMultiDict[str],
        cookies: CookieJar,
        content: bytes,
        status_code: int,
        exception: Optional[Exception]=None,
    ) -> None:
        self.request = request
        '''请求体'''
        self.headers = headers
        '''响应头'''
        
        self.cookies = cookies
        '''响应 Cookie'''
        
        self.content = content
        '''响应内容'''
        self.status_code = status_code
        '''状态码'''
        self.exception = exception
        '''异常'''
    
    @property
    def url(self) -> URL:
        '''响应 URL'''
        return self.request.url
    
    def json(self, **kwargs: Any) -> Any:
        '''解析 JSON 响应内容'''
        return loads(self.content, **kwargs)
    
    def raise_for_status(self) -> None:
        '''检查响应状态码'''
        if self.status_code >= 400:
            raise HTTPStatusError(self)

class Client(ABC):
    '''同步 HTTP 客户端类型基类'''
    
    def __init__(self, proxy: Optional[str], timeout: int) -> None:
        self.proxy = proxy
        '''代理服务器地址'''
        self.timeout = timeout
        '''超时时间'''
    
    @abstractmethod
    def __enter__(self) -> Self:
        raise NotImplementedError
    
    @abstractmethod
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def request(self, request: Request) -> Response:
        '''发送请求并获取响应'''
        raise NotImplementedError

class AsyncClient(ABC):
    '''异步 HTTP 客户端类型基类'''
    
    def __init__(self, proxy: Optional[str], timeout: int) -> None:
        self.proxy = proxy
        '''代理服务器地址'''
        self.timeout = timeout
        '''超时时间'''
    
    @abstractmethod
    async def __aenter__(self) -> Self:
        raise NotImplementedError
    
    @abstractmethod
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        raise NotImplementedError
    
    @abstractmethod
    async def request(self, request: Request) -> Response:
        '''异步发送请求并获取响应'''
        raise NotImplementedError
