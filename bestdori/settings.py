'''`bestdori.settings` 设置项'''

from typing import Optional

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
    
    timeout: int = 10
    '''超时时间'''
    
settings = Settings()