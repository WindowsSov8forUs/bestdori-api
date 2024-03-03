from typing import Optional

class Settings:
    '''`bestdori_api` 设置项类'''
    
    proxy: Optional[str] = None
    '''代理服务器'''
    print: bool = False
    '''是否打印输出信息'''

settings = Settings()
