'''`bestdori.ayachan.exceptions`

ayachan API 错误信息相关操作'''

# Sonolus 相关错误
class SonolusException(Exception):
    '''Sonolus 相关错误'''
    # 初始化
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
