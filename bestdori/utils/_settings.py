from typing import TYPE_CHECKING, Union, Optional

from httpx._models import Cookies

from ..exceptions import NoCookiesError

if TYPE_CHECKING:
    from ..user import Me

class Settings:
    '''`bestdori_api` 设置项类'''
    
    proxy: Optional[Union[dict[str, str], str]] = None
    '''代理服务器

    若想要使用代理，则必须设置该选项，
    因为 `bestdori` 将会在内部默认无视系统环境下的代理设置
    '''
    cookies: Optional[Cookies] = None
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
