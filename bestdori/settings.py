'''`bestdori.settings` 设置项'''

from typing import TYPE_CHECKING, Optional

from http.cookies import SimpleCookie

from .exceptions import NoCookiesError

if TYPE_CHECKING:
    from .user import Me

class AyachanSettings:
    '''`bestdori.ayachan` 设置类'''
    
    proxy: Optional[str] = None
    '''代理服务器'''
    
    timeout: int = 10
    '''超时时间'''

class Settings:
    '''`bestdori` 设置类'''
    
    ayachan: AyachanSettings = AyachanSettings()
    '''`bestdori.ayachan` 设置项'''
    
    proxy: Optional[str] = None
    '''代理服务器

    若想要使用代理，则必须设置该选项，
    因为 `bestdori` 将会在内部默认无视系统环境下的代理设置
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

    def set_user(self, username: str, password: str) -> None:
        '''设置用户名与密码'''
        self._username = username
        self._password = password

    def _cookies(self) -> SimpleCookie:
        '''获取 Cookies'''
        if self.cookies:
            return self.cookies
        if self._me is not None:
            return self._me.cookies
        raise NoCookiesError()

settings = Settings()