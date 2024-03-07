from typing import TYPE_CHECKING, Optional

from httpx import Client
from httpx._models import Cookies

from ..exceptions import NoCookiesError

if TYPE_CHECKING:
    from ..user import Me

class Settings:
    '''`bestdori_api` 设置项类'''
    
    proxy: Optional[str] = None
    '''代理服务器'''
    cookies: Optional[Cookies] = None
    '''Cookies

    不建议直接设置，推荐通过 `Settings.set_user` 方法，
    传入传入用户名与密码设置
    '''
    client: Optional[Client] = None
    '''HTTP 客户端'''
    _username: Optional[str] = None
    '''用户名'''
    _password: Optional[str] = None
    '''密码'''
    _me: Optional['Me'] = None
    '''`Me` 对象'''
    
    def set_user(self, username: str, password: str) -> 'Settings':
        '''设置用户名与密码'''
        self._username = username
        self._password = password
        return self
    
    def _cookies(self) -> Cookies:
        '''获取 Cookies'''
        if self.cookies:
            return self.cookies
        if self._username and self._password:
            if self._me:
                return self._me.cookies
        raise NoCookiesError()

settings = Settings()
