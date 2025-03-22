
from multidict import CIMultiDict
from http.cookiejar import CookieJar
from typing import Any, Dict, Type, Union, Literal, Optional, overload

from bestdori.settings import settings
from bestdori.exceptions import (
    REQUEST_EXCEPTION,
    RequestException,
    SonolusException,
    NoContentTypeError,
    AssetsNotExistError,
    AyachanResponseError,
)

from .client import (
    Client as Client,
    Request as Request,
    Response as Response,
    AsyncClient as AsyncClient,
    FilesContent as FilesContent,
)

PREFIX = {
    'ayachan': 'https://api.ayachan.fun',
    'bestdori': 'https://bestdori.com',
    'sonolus': 'https://sonolus.ayachan.fun',
    'niconi': 'https://card.niconi.co.ni',
}
HEADERS_DICT: Dict[str, CIMultiDict[str]] = {
    'bestdori-api': CIMultiDict({'Content-Type': 'application/json;charset=UTF-8'}),
    'sonolus-post': CIMultiDict({
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxjpDgorEXUAUIbBN',
    }),
}

__CLIENT_AVAILABLE__ = {
    'httpx': ['sync', 'async'],
    'aiohttp': ['async'],
}

__Client__: Optional[Type[Client]] = None
'''当前的同步客户端类'''
__AsyncClient__: Optional[Type[AsyncClient]] = None
'''当前的异步客户端类'''

@overload
def _import_client(name: str) -> Type[Client]:
    ...

@overload
def _import_client(name: str, _async: Literal[True]) -> Type[AsyncClient]:
    ...

def _import_client(name: str, _async: bool = False) -> Union[Type[Client], Type[AsyncClient]]:
    '''导入客户端类'''
    
    if name == 'httpx':
        if _async:
            from .httpx import AsyncClient
            return AsyncClient
        else:
            from .httpx import Client
            return Client
    elif name == 'aiohttp':
        if _async:
            from .aiohttp import AsyncClient
            return AsyncClient
        else:
            raise ImportError('\'aiohttp\' does not support sync client.')
    else:
        raise ImportError(f'cannot find builtin {name} client.')

def get_client(*, proxy: Optional[str], timeout: int) -> Client:
    '''获取一个当前可用的同步客户端'''
    global __Client__
    
    if __Client__ is None:
        for name, types in __CLIENT_AVAILABLE__.items():
            if 'sync' in types:
                try:
                    __Client__ = _import_client(name)
                    break
                except ImportError:
                    continue
        else:
            raise ImportError('no available client.')
    
    client = __Client__(proxy, timeout)
    
    return client

def get_async_client(*, proxy: Optional[str], timeout: int) -> AsyncClient:
    '''获取一个当前可用的异步客户端'''
    global __AsyncClient__
    
    if __AsyncClient__ is None:
        for name, types in __CLIENT_AVAILABLE__.items():
            if 'async' in types:
                try:
                    __AsyncClient__ = _import_client(name, _async=True)
                    break
                except ImportError:
                    continue
        else:
            raise ImportError('no available client.')
    
    client = __AsyncClient__(proxy, timeout)
    
    return client

# API 请求发送类
class Api:
    '''API 请求发送类'''
    
    _url: str
    
    def __init__(self, url: str) -> None:
        self._url = url
    
    @property
    def url(self) -> str:
        '''请求 URL'''
        if self._url.startswith('http'):
            return self._url
        return f'{PREFIX["bestdori"]}{self._url}'
    
    def _build_request(
        self,
        method: Literal['GET', 'POST'],
        *,
        cookies: Optional[CookieJar]=None,
        params: Optional[Dict[str, Any]]=None,
        data: Optional[Any]=None,
        files: Optional[FilesContent]=None,
    ) -> Request:
        '''构建请求体'''
        
        if self.url.startswith(PREFIX['bestdori']) and not self.url.endswith('/api/upload'):
            # Bestdori 文件上传 API 需要特殊的请求头
            headers = HEADERS_DICT['bestdori-api']
        elif self.url.startswith(PREFIX['sonolus']) and method == 'POST':
            # Sonolus 测试服上传 API 需要特殊的请求头
            headers = HEADERS_DICT['sonolus-post']
        else:
            headers = None
        
        return Request(
            method,
            self.url,
            headers=headers,
            cookies=cookies,
            params=params,
            data=data,
            files=files,
        )
    
    def _handle_response(self, response: Response) -> Response:
        '''处理响应体'''
        try:
            response.raise_for_status()
        except Exception as e:
            # 对于 Ayachan 的 400/500 响应码抛出特殊的异常
            if PREFIX['ayachan'] in self.url and response.status_code in (400, 500):
                response_data: Dict[str, Any] = response.json()
                raise AyachanResponseError(response_data.get('error', 'None'))
            
            # 对于 Sonolus 的非 200 响应码抛出特殊的异常
            elif PREFIX['sonolus'] in self.url and response.status_code != 200:
                response_data: Dict[str, Any] = response.json()
                raise SonolusException(
                    f"code: {response_data.get('code', None)}, "
                    f"description: {response_data.get('description', None)}, "
                    f"detail: {response_data.get('detail', None)}"
                )
        
        content_type = response.headers.get('Content-Type', None)
        if not content_type:
            raise NoContentTypeError(response.url.path)
        
        url = str(response.url)
        
        if url.startswith(PREFIX['bestdori']) and '/api/' in url:
            # 处理 Bestdori API 响应
            if 'application/json' not in content_type:
                return response
            
            response_data = response.json()
            if not isinstance(response_data, dict):
                return response
            result = response_data.get('result', None)
            if result is None:
                return response
            if result is False:
                if (code := response_data.get('code', None)) is not None:
                    # 如果返回了错误码，根据错误码不同抛出异常
                    if code in REQUEST_EXCEPTION.keys():
                        ExceptionClass = REQUEST_EXCEPTION[code]
                        if response.request.params is not None:
                            raise ExceptionClass(response.request.url.path, **response.request.params)
                        elif response.request.data is not None:
                            raise ExceptionClass(response.request.url.path, **response.request.data)
                        else:
                            raise ExceptionClass(response.request.url.path)
                    else:
                        raise RequestException(response.request.url.path, code)
                else:
                    raise RequestException(response.request.url.path)
        
        elif '/assets/' in url or '/res/' in url:
            # 处理资源获取响应，如果返回了 HTML 页面则说明资源不存在
            if 'text/html' in content_type:
                raise AssetsNotExistError(url)
            return response
        
        return response
    
    def _request(
        self,
        method: Literal['GET', 'POST'],
        *,
        cookies: Optional[CookieJar]=None,
        params: Optional[Dict[str, Any]]=None,
        data: Optional[Any]=None,
        files: Optional[FilesContent]=None,
    ) -> Response:
        '''发送请求'''
        request = self._build_request(method, cookies=cookies, params=params, data=data, files=files)
        
        with get_client(proxy=settings.proxy, timeout=settings.timeout) as client:
            response = client.request(request)
        
        return self._handle_response(response)
    
    async def _arequest(
        self,
        method: Literal['GET', 'POST'],
        *,
        cookies: Optional[CookieJar]=None,
        params: Optional[Dict[str, Any]]=None,
        data: Optional[Any]=None,
        files: Optional[FilesContent]=None,
    ) -> Response:
        '''异步发送请求'''
        request = self._build_request(method, cookies=cookies, params=params, data=data, files=files)
        
        async with get_async_client(proxy=settings.proxy, timeout=settings.timeout) as client:
            response = await client.request(request)
        
        return self._handle_response(response)
    
    def get(
        self,
        *,
        cookies: Optional[CookieJar]=None,
        params: Optional[Dict[str, Any]]=None,
    ) -> Response:
        '''发送 GET 请求

        参数:
            cookies (Optional[CookieJar], optional): Cookies
            params (Optional[Dict[str, Any]], optional): URL 参数

        返回:
            Response: 响应体
        '''
        return self._request('GET', cookies=cookies, params=params)
    
    async def aget(
        self,
        *,
        cookies: Optional[CookieJar]=None,
        params: Optional[Dict[str, Any]]=None,
    ) -> Response:
        '''异步发送 GET 请求

        参数:
            cookies (Optional[CookieJar], optional): Cookies
            params (Optional[Dict[str, Any]], optional): 调用参数

        返回:
            Response: 响应体
        '''
        return await self._arequest('GET', cookies=cookies, params=params)
    
    def post(
        self,
        *,
        cookies: Optional[CookieJar]=None,
        data: Optional[Any]=None,
        files: Optional[FilesContent]=None,
    ) -> Response:
        '''发送 POST 请求

        参数:
            cookies (Optional[CookieJar], optional): Cookies
            data (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[Dict[str, Tuple[str, BufferedReader]]], optional): 发送文件参数

        返回:
            Response: 响应体
        '''
        return self._request('POST', cookies=cookies, data=data, files=files)
    
    async def apost(
        self,
        *,
        cookies: Optional[CookieJar]=None,
        data: Optional[Any]=None,
        files: Optional[FilesContent]=None,
    ) -> Response:
        '''异步发送 POST 请求

        参数:
            cookies (Optional[CookieJar], optional): Cookies
            data (Optional[Any], optional): 调用参数，将以 `json` 字符串形式发送
            files (Optional[Dict[str, Tuple[str, BufferedReader]]], optional): 发送文件参数

        返回:
            Response: 响应体
        '''
        return await self._arequest('POST', cookies=cookies, data=data, files=files)