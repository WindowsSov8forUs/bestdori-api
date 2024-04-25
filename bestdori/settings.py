'''`bestdori.settings` 设置项'''

from enum import StrEnum
from typing import TYPE_CHECKING, Union, Optional

from http.cookies import SimpleCookie

from .exceptions import NoCookiesError

if TYPE_CHECKING:
    from .user import Me

class AsyncClient(StrEnum):
    '''异步客户端'''
    HTTPX = 'httpx'
    AIO_HTTP = 'aiohttp'

proxy: Optional[Union[dict[str, str], str]] = None
'''代理服务器

若想要使用代理，则必须设置该选项，
因为 `bestdori` 将会在内部默认无视系统环境下的代理设置
'''
async_client: AsyncClient = AsyncClient.HTTPX
'''异步客户端

默认为 `httpx`，可选 `aiohttp`
'''
cookies: Optional[SimpleCookie] = None
'''Cookies

不建议直接设置，推荐通过 `Settings.set_user` 方法，
传入传入用户名与密码设置
'''
timeout: int = 10
'''超时时间'''
_username: Optional[str] = None
'''用户名'''
_password: Optional[str] = None
'''密码'''
_me: Optional['Me'] = None
'''`Me` 对象'''

def set_user(username: str, password: str) -> None:
    '''设置用户名与密码'''
    global _username, _password
    
    _username = username
    _password = password

def _cookies() -> SimpleCookie:
    '''获取 Cookies'''
    global cookies, _username, _password, _me
    
    if cookies:
        return cookies
    if _me is not None:
        return _me.cookies
    raise NoCookiesError()
