from json import dumps
from typing import Any, cast
from multidict import CIMultiDict
from typing_extensions import override

from .client import Request, Response
from .client import Client as _Client
from .client import AsyncClient as _AsyncClient

try:
    import httpx
except ModuleNotFoundError as exception:
    raise ImportError(
        'module \'httpx\' is not installed, please install it by running \'pip install httpx\''
    ) from exception

__HTTPX_ABOVE_0_28_0__ : bool = tuple(httpx.__version__.split('.')) >= ('0', '28', '0')

class Client(_Client):
    '''HTTPX 同步 HTTP 客户端类型'''
    _client: httpx.Client
    
    @override
    def __enter__(self) -> "Client":
        if __HTTPX_ABOVE_0_28_0__:
            self._client = httpx.Client(
                proxy=self.proxy,
                timeout=self.timeout,
                trust_env=True,
            )
        else:
            proxies = {
                'http://': self.proxy,
                'https://': self.proxy,
            }
            self._client = httpx.Client(
                proxies=cast(dict, proxies), # type: ignore
                timeout=self.timeout,
                trust_env=True,
            )
        
        self._client.__enter__()
        return self
    
    @override
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self._client.__exit__(exc_type, exc_value, traceback)
    
    @override
    def request(self, request: Request) -> Response:
        '''发送请求并获取响应'''
        if __HTTPX_ABOVE_0_28_0__:
            _request = httpx.Request(
                request.method,
                str(request.url),
                params=request.params,
                headers=request.headers,
                cookies=request.cookies,
                content=cast(dict, dumps(request.data)) if request.data else None,
                files=request.files,
                json=request.json,
            )
        else:
            _request = httpx.Request(
                request.method,
                str(request.url),
                params=request.params,
                headers=request.headers,
                cookies=request.cookies,
                data=cast(dict, dumps(request.data)) if request.data else None,
                files=request.files,
                json=request.json,
            )
        
        response = self._client.send(_request)
        
        try:
            response.raise_for_status()
            return Response(
                request,
                CIMultiDict(response.headers),
                response.cookies.jar,
                response.content,
                response.status_code,
            )
        except Exception as exception:
            return Response(
                request,
                CIMultiDict(response.headers),
                response.cookies.jar,
                response.content,
                response.status_code,
                exception,
            )

class AsyncClient(_AsyncClient):
    '''HTTPX 异步 HTTP 客户端类型'''
    _async_client: httpx.AsyncClient
    
    @override
    async def __aenter__(self) -> "AsyncClient":
        if __HTTPX_ABOVE_0_28_0__:
            self._async_client = httpx.AsyncClient(
                proxy=self.proxy,
                timeout=self.timeout,
                trust_env=False,
            )
        else:
            proxies = {
                'http://': self.proxy,
                'https://': self.proxy,
            }
            self._async_client = httpx.AsyncClient(
                proxies=cast(dict, proxies), # type: ignore
                timeout=self.timeout,
                trust_env=False,
            )
        
        await self._async_client.__aenter__()
        return self
    
    @override
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        await self._async_client.__aexit__(exc_type, exc_value, traceback)
    
    @override
    async def request(self, request: Request) -> Response:
        '''异步发送请求并获取响应'''
        if __HTTPX_ABOVE_0_28_0__:
            _request = httpx.Request(
                request.method,
                str(request.url),
                params=request.params,
                headers=request.headers,
                cookies=request.cookies,
                content=cast(dict, dumps(request.data)) if request.data else None,
                files=request.files,
                json=request.json,
            )
        else:
            _request = httpx.Request(
                request.method,
                str(request.url),
                params=request.params,
                headers=request.headers,
                cookies=request.cookies,
                data=cast(dict, dumps(request.data)) if request.data else None,
                files=request.files,
                json=request.json,
            )
        
        response = await self._async_client.send(_request)
        
        try:
            response.raise_for_status()
            return Response(
                request,
                CIMultiDict(response.headers),
                response.cookies.jar,
                response.content,
                response.status_code,
            )
        except Exception as exception:
            return Response(
                request,
                CIMultiDict(response.headers),
                response.cookies.jar,
                response.content,
                response.status_code,
                exception,
            )
