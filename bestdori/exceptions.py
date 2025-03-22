'''`bestdori.exceptions`

API 错误信息相关操作'''
from typing import TYPE_CHECKING, Any, Dict, Type

if TYPE_CHECKING:
    from .typing import PostInfo
    from .utils.network import Response

# 错误基类
class BestdoriException(Exception):
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
class RequestException(BestdoriException):
    '''请求发送错误'''
    # 初始化
    def __init__(self, api: str, msg: str='No error code received.', **kwargs: Any) -> None:
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
        return f'An error occured while sending request to Bestdori \'{self.api}\': {self.message}'

# 没有获取到 ContentType
class NoContentTypeError(RequestException):
    '''没有获取到 ContentType'''
    # 初始化
    def __init__(self, url: str) -> None:
        msg = f'没有获取到 {url} 的 ContentType'
        super().__init__(msg)
        return

# 资源错误
class AssetsException(BestdoriException):
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
        return f'An error occured while requesting for assets: {self.message}'

# 帖子错误
class PostException(BestdoriException):
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
    def __init__(self, post: 'PostInfo') -> None:
        name = post.get('categoryName', 'DEFAULT_POST')
        msg = f'Post \'{name}\' is not a chart post.'
        super().__init__(msg)
        return

# 帖子没有音乐字段
class PostHasNoSongError(PostException):
    '''帖子没有音乐字段'''
    # 初始化
    def __init__(self, post: 'PostInfo') -> None:
        name = post.get('categoryName', 'DEFAULT_POST')
        msg = f'Post \'{name}\' has no music assets.'
        super().__init__(msg)
        return

class HTTPStatusError(BestdoriException):
    '''HTTP 状态码错误'''
    
    response: 'Response'
    
    def __init__(self, response: 'Response') -> None:
        self.response = response
        super().__init__(
            f"HTTP status code error: {response.status_code}"
            + f"while requesting {response.url.path},"
            + "please check your network environment or contact the developer."
        )
    
    @property
    def status_code(self) -> int:
        '''状态码'''
        return self.response.status_code

# 请求无效
class RequestInvalidError(RequestException):
    '''请求无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = 'Request Invalid.'
        super().__init__(api, msg, **kwargs)
        return

# 需要登录
class LoginRequiredError(RequestException):
    '''需要登录'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = 'Login Required.'
        super().__init__(api, msg, **kwargs)
        return

# 证书无效
class CredentialsInvalidError(RequestException):
    '''证书无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = 'Credentials Invalid.'
        super().__init__(api, msg, **kwargs)
        return

# 用户无效
class UserInvalidError(RequestException):
    '''用户无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = 'User Invalid.'
        super().__init__(api, msg, **kwargs)
        return

# 文件已经被上传过
class AlreadyUploadedError(RequestException):
    '''文件已经被上传过'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = 'Already Uploaded.'
        super().__init__(api, msg, **kwargs)
        return

# 帖子无效
class PostInvalidError(RequestException):
    '''帖子无效'''
    # 初始化
    def __init__(self, api: str, **kwargs: Any) -> None:
        msg = 'Post Invalid.'
        super().__init__(api, msg, **kwargs)
        return

# 资源不存在
class AssetsNotExistError(AssetsException):
    '''资源不存在'''
    # 初始化
    def __init__(self, asset_name: str) -> None:
        msg = f'Assets {asset_name} may not exist.'
        super().__init__(msg)

# 某 id 指定的资源不存在
class NotExistException(BestdoriException):
    '''资源不存在'''
    # 初始化
    def __init__(self, src: str) -> None:
        msg = f'{src} is not exist.'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 玩家不存在
class PlayerNotExistError(NotExistException):
    '''玩家不存在'''
    # 初始化
    def __init__(self, server: str, id: int) -> None:
        msg = f'Player {id} is not exist in server \'{server}\'.'
        super().__init__(msg)
        return

# 服务器指定错误
class ServerNotAvailableError(BestdoriException):
    '''服务器指定错误'''
    # 初始化
    def __init__(self, name: str, server: str) -> None:
        msg = f'{name} is not available in server \'{server}\'.'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 无法获取到信息错误
class NoDataException(BestdoriException):
    '''无法获取到信息错误'''
    # 初始化
    def __init__(self, src: str) -> None:
        msg = f'Cannot get {src} data.'
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 设置出错
class SettingsException(BestdoriException):
    '''设置出错'''
    # 初始化
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.message = msg
        '''错误信息'''
        return

# 请求错误集合
REQUEST_EXCEPTION: Dict[str, Type[RequestException]] = {
    'REQUEST_INVALID': RequestInvalidError,
    'LOGIN_REQUIRED': LoginRequiredError,
    'CREDENTIALS_INVALID': CredentialsInvalidError,
    'USER_INVALID': UserInvalidError,
    'ALREADY_UPLOADED': AlreadyUploadedError,
    'POST_INVALID': PostInvalidError
}
'''请求错误集合'''

# Sonolus 相关错误
class SonolusException(Exception):
    '''Sonolus 相关错误'''
    # 初始化
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

# Ayachan 相关错误
class AyachanException(Exception):
    '''Ayachan 相关错误'''
    # 初始化
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

class AyachanResponseError(AyachanException):
    '''Ayachan API 响应错误'''
    # 初始化
    def __init__(self, error: str) -> None:
        super().__init__(error)
