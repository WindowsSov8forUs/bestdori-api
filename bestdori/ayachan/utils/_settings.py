from typing import Union, Optional

class Settings:
    '''`bestdori_api` 设置项类'''
    
    proxy: Optional[Union[dict[str, str], str]] = None
    '''代理服务器'''
    timeout: int = 10
    '''超时时间'''

settings = Settings()
