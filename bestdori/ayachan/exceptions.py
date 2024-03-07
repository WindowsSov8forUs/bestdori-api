'''`bestdori.ayachan.exceptions`

ayachan API 错误信息相关操作'''
from typing import Any

# 错误基类
class BaseException(Exception):
    '''错误基类'''
    # 初始化
    def __init__(self, msg: str) -> None:
        self.message = msg
        '''错误信息'''
    
    # 字符串化
    def __str__(self) -> str:
        '''输出字符串'''
        return self.message

# Sonolus 相关错误
class SonolusException(BaseException):
    '''Sonolus 相关错误'''
    # 初始化
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
