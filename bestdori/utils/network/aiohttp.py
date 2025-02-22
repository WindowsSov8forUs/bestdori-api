from typing import Any
from multidict import CIMultiDict
from typing_extensions import override

from .client import Request, Response
from .client import AsyncClient as _AsyncClient

try:
    import aiohttp
except ModuleNotFoundError as exception:
    raise ImportError(
        'module \'aiohttp\' is not installed, please install it by running \'pip install aiohttp\''
    ) from exception

class AsyncClient(_AsyncClient):
    '''AIOHTTP 异步 HTTP 客户端'''
    _client_session: aiohttp.ClientSession
    
    @override
    async def __aenter__(self) -> 'AsyncClient':
        self._client_session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(self.timeout),
            trust_env=False,
        )
        await self._client_session.__aenter__()
        return self
    
    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        await self._client_session.__aexit__(exc_type, exc_value, traceback)
    
    async def request(self, request: Request) -> Response:
        '''异步发送请求并获取响应'''
        response: aiohttp.ClientResponse
        
        data = request.data
        if request.files:
            data = aiohttp.FormData(data or {}, quote_fields=False)
            for name, file in request.files.items():
                data.add_field(name, file[1].read(), filename=file[0])
        
        async with self._client_session.request(
            request.method,
            request.url,
            cookies=request.cookies,
            headers=request.headers,
            params=request.params,
            data=data,
            json=request.json,
            proxy=self.proxy,
        ) as response:
            
            try:
                response.raise_for_status()
                return Response(
                    request,
                    CIMultiDict(response.headers),
                    response.cookies,
                    await response.read(),
                    response.status,
                )
            except Exception as exception:
                return Response(
                    request,
                    CIMultiDict(response.headers),
                    response.cookies,
                    await response.read(),
                    response.status,
                    exception,
                )