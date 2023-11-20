'''`bestdori.exceptions`

API 错误信息相关操作'''
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

# 请求发送错误
class RequestException(BaseException):
    '''请求发送错误'''
    # 初始化
    def __init__(self, api: str, msg: str='无错误代码获取。', **kwargs: Any) -> None:
        if len(kwargs) > 0:
            msg += f': {kwargs}'
        else:
            msg += '。'
        super().__init__(msg)
        self.api = api
        '''请求所使用的 API'''
    
    # 字符串化
    def __str__(self) -> str:
        '''输出字符串'''
        return f'向 Bestdori {self.api} 发送请求时出错。{self.message}'

# 资源错误
class AssetsException(BaseException):
    '''资源错误'''
    # 初始化
    def __init__(self, msg: str, **kwargs: Any) -> None:
        if len(kwargs) > 0:
            msg += f': {kwargs}'
        else:
            msg += '。'
        super().__init__(msg)
    
    # 字符串化
    def __str__(self) -> str:
        '''输出字符串'''
        return f'获取资源时出错。{self.message}'

# 帖子不是社区谱面
class PostHasNoChartError(BaseException):
    '''帖子不是社区谱面'''
    # 初始化
    def __init__(self, post: dict[str, Any]) -> None:
        name = post.get('categoryName', 'DEFAULT_POST')
        msg = f'该帖子类型 {name} 不是社区谱面。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 帖子没有音乐字段
class PostHasNoSongError(BaseException):
    '''帖子没有音乐字段'''
    # 初始化
    def __init__(self, post: dict[str, Any]) -> None:
        name = post.get('categoryName', 'DEFAULT_POST')
        msg = f'该帖子类型 {name} 不存在歌曲资源。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 歌曲不存在
class SongNotExistError(BaseException):
    '''歌曲不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'歌曲 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 歌曲难度不存在
class DiffNotExistError(BaseException):
    '''歌曲难度不存在'''
    # 初始化
    def __init__(self, diff: str) -> None:
        msg = f'歌曲不存在难度 {diff}。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 请求无效
class RequestInvalidError(RequestException):
    '''请求无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = '请求无效'
        super().__init__(api, msg, **kwargs)
        return

# 需要登录
class LoginRequiredError(RequestException):
    '''需要登录'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = '需要登录'
        super().__init__(api, msg, **kwargs)
        return

# 证书无效
class CredentialsInvalidError(RequestException):
    '''证书无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = '证书无效'
        super().__init__(api, msg, **kwargs)
        return

# 用户无效
class UserInvalidError(RequestException):
    '''用户无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = '用户无效'
        super().__init__(api, msg, **kwargs)
        return

# 文件已经被上传过
class AlreadyUploadedError(RequestException):
    '''文件已经被上传过'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = '文件已经被上传过'
        super().__init__(api, msg, **kwargs)
        return

# 帖子无效
class PostInvalidError(RequestException):
    '''帖子无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = '帖子无效'
        super().__init__(api, msg, **kwargs)
        return

# 资源不存在
class AssetsNotExistError(AssetsException):
    '''资源不存在'''
    # 初始化
    def __init__(self, asset_name: str) -> None:
        msg = f'资源 {asset_name} 可能不存在。'
        super().__init__(msg)

# 角色不存在
class CharacterNotExistError(BaseException):
    '''角色不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'角色 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 卡牌不存在
class CardNotExistError(BaseException):
    '''卡牌不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'卡牌 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 服装不存在
class CostumeNotExistError(BaseException):
    '''服装不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'服装 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 活动不存在
class EventNotExistError(BaseException):
    '''活动不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'活动 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 招募不存在
class GachaNotExistError(BaseException):
    '''招募不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'招募 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 登录奖励不存在
class LoginCampaignNotExistError(BaseException):
    '''登录奖励不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'登录奖励 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 自选券不存在
class MiracleTicketExchangeNotExistError(BaseException):
    '''自选券不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'自选券 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 漫画不存在
class ComicNotExistError(BaseException):
    '''漫画不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'漫画 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 任务不存在
class MissionNotExistError(BaseException):
    '''任务不存在'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'任务 ID {id_} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 服务器指定错误
class ServerNotAvailableError(BaseException):
    '''服务器指定错误'''
    # 初始化
    def __init__(self, name: str, server: str) -> None:
        msg = f'{name} 在服务器 {server} 不可用。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 活动没有奖励贴纸错误
class EventHasNoStampError(BaseException):
    '''活动没有奖励贴纸错误'''
    # 初始化
    def __init__(self, id_: int) -> None:
        msg = f'活动 ID {id_} 没有奖励贴纸。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 请求错误集合
REQUEST_EXCEPTION: dict[str, type[RequestException]] = {
    'REQUEST_INVALID': RequestInvalidError,
    'LOGIN_REQUIRED': LoginRequiredError,
    'CREDENTIALS_INVALID': CredentialsInvalidError,
    'USER_INVALID': UserInvalidError,
    'ALREADY_UPLOADED': AlreadyUploadedError,
    'POST_INVALID': PostInvalidError
}
'''请求错误集合'''