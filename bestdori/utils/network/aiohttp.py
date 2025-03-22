from typing import Any
from multidict import CIMultiDict
from http.cookies import SimpleCookie
from typing_extensions import override
from http.cookiejar import Cookie, CookieJar

from .client import Request, Response
from .client import AsyncClient as _AsyncClient

try:
    import aiohttp
except ModuleNotFoundError as exception:
    raise ImportError(
        'module \'aiohttp\' is not installed, please install it by running \'pip install aiohttp\''
    ) from exception

def _simplecookie_to_cookiejar(simple_cookie: SimpleCookie) -> CookieJar:
    jar = CookieJar()

    for name, morsel in simple_cookie.items():
        cookie = Cookie(
            version=0,
            name=name,
            value=morsel.value,
            port=None,
            port_specified=False,
            domain=morsel['domain'],
            domain_specified=bool(morsel['domain']),
            domain_initial_dot=morsel['domain'].startswith('.'),
            path=morsel['path'],
            path_specified=bool(morsel['path']),
            secure=morsel['secure'],
            expires=morsel['expires'],
            discard=False,
            comment=morsel['comment'],
            comment_url=None,
            rest={'HttpOnly': morsel['httponly']},
            rfc2109=False,
        )
        jar.set_cookie(cookie)
    return jar

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
        
        # 转换 cookie
        cookies = None
        if request.cookies:
            cookies = (
                (cookie.name, cookie.value)
                for cookie in request.cookies
                if cookie.value is not None
            )

        async with self._client_session.request(
            request.method,
            request.url,
            cookies=cookies,
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
                    _simplecookie_to_cookiejar(response.cookies),
                    await response.read(),
                    response.status,
                )
            except Exception as exception:
                return Response(
                    request,
                    CIMultiDict(response.headers),
                    _simplecookie_to_cookiejar(response.cookies),
                    await response.read(),
                    response.status,
                    exception,
                )