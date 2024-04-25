'''`bestdori.exceptions`

API 错误信息相关操作'''
from typing import Any

from httpx._models import Response
from httpx._exceptions import RequestError

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
    def __init__(self, api: str, msg: str='无错误代码获取', **kwargs: Any) -> None:
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

# 帖子错误
class PostException(BaseException):
    '''帖子错误'''
    # 初始化
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 帖子不是社区谱面
class PostHasNoChartError(PostException):
    '''帖子不是社区谱面'''
    # 初始化
    def __init__(self, post: dict[str, Any]) -> None:
        name = post.get('categoryName', 'DEFAULT_POST')
        msg = f'该帖子类型 {name} 不是社区谱面。'
        super().__init__(msg)
        return

# 帖子没有音乐字段
class PostHasNoSongError(PostException):
    '''帖子没有音乐字段'''
    # 初始化
    def __init__(self, post: dict[str, Any]) -> None:
        name = post.get('categoryName', 'DEFAULT_POST')
        msg = f'该帖子类型 {name} 不存在歌曲资源。'
        super().__init__(msg)
        return

# 某 id 指定的资源不存在
class NotExistException(BaseException):
    '''资源不存在'''
    # 初始化
    def __init__(self, src: str) -> None:
        msg = f'{src} 不存在。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 歌曲不存在
class SongNotExistError(NotExistException):
    '''歌曲不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        super().__init__(f'歌曲 ID {id}')
        return

# 歌曲难度不存在
class DiffNotExistError(NotExistException):
    '''歌曲难度不存在'''
    # 初始化
    def __init__(self, diff: str) -> None:
        msg = f'歌曲难度 {diff}'
        super().__init__(msg)
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
class CharacterNotExistError(NotExistException):
    '''角色不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'角色 ID {id}'
        super().__init__(msg)
        return

# 卡牌不存在
class CardNotExistError(NotExistException):
    '''卡牌不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'卡牌 ID {id}'
        super().__init__(msg)
        return

# 服装不存在
class CostumeNotExistError(NotExistException):
    '''服装不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'服装 ID {id}'
        super().__init__(msg)
        return

# 活动不存在
class EventNotExistError(NotExistException):
    '''活动不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'活动 ID {id}'
        super().__init__(msg)
        return

# 招募不存在
class GachaNotExistError(NotExistException):
    '''招募不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'招募 ID {id}NotExistException'
        super().__init__(msg)
        return

# 登录奖励不存在
class LoginCampaignNotExistError(NotExistException):
    '''登录奖励不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'登录奖励 ID {id} 不存在。'
        super().__init__(msg)
        return

# 自选券不存在
class MiracleTicketExchangeNotExistError(NotExistException):
    '''自选券不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'自选券 ID {id} 不存在。'
        super().__init__(msg)
        return

# 漫画不存在
class ComicNotExistError(NotExistException):
    '''漫画不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'漫画 ID {id} 不存在。'
        super().__init__(msg)
        return

# 任务不存在
class MissionNotExistError(NotExistException):
    '''任务不存在'''
    # 初始化
    def __init__(self, id: int) -> None:
        msg = f'任务 ID {id} 不存在。'
        super().__init__(msg)
        return

# 玩家不存在
class PlayerNotExistError(NotExistException):
    '''玩家不存在'''
    # 初始化
    def __init__(self, server: str, id: int) -> None:
        msg = f'服务器 {server} 上的玩家 ID {id} 不存在。'
        super().__init__(msg)
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
    def __init__(self, id: int) -> None:
        msg = f'活动 ID {id} 没有奖励贴纸。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 无法获取到信息错误
class NoDataException(BaseException):
    '''无法获取到信息错误'''
    # 初始化
    def __init__(self, src: str) -> None:
        msg = f'无法获取 {src} 。'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 设置出错
class SettingsException(BaseException):
    '''设置出错'''
    # 初始化
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 没有设置 Cookies
class NoCookiesError(SettingsException):
    '''没有设置 Cookies'''
    # 初始化
    def __init__(self) -> None:
        msg = '没有设置 Cookies'
        super().__init__(msg)
        return

# 没有获取到 ContentType
class NoContentTypeError(RequestError):
    '''没有获取到 ContentType'''
    # 初始化
    def __init__(self, url: str) -> None:
        msg = f'没有获取到 {url} 的 ContentType'
        super().__init__(msg)
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