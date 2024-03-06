from typing import Optional

from httpx import Client

class Settings:
    '''`bestdori_api` 设置项类'''
    
    proxy: Optional[str] = None
    '''代理服务器'''
    client: Optional[Client] = None
    '''HTTP 客户端'''
    print: bool = False
    '''是否打印输出信息'''

settings = Settings()
