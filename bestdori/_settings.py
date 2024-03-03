from typing import TYPE_CHECKING, Optional

from httpx._models import Cookies

if TYPE_CHECKING:
    from .user import Me

class Settings:
    '''`bestdori_api` 设置项类'''
    
    proxy: Optional[str] = None
    '''代理服务器'''
    cookies: Optional[Cookies] = None
    '''Cookies

    不建议直接设置，推荐通过 `Settings.set_cookies` 方法，
    传入一个 `bestdori.user.Me` 对象设置
    '''
    print: bool = False
    '''是否打印输出信息'''
    
    def set_cookies(self, me: 'Me') -> 'Settings':
        '''设置 Cookies'''
        self.cookies = me.cookies
        return self

settings = Settings()
