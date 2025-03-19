'''`bestdori.ayachan`

ayachan 的各种 API 调用整合'''

from typing import TYPE_CHECKING

from bestdori.utils import get_api
from bestdori.utils.network import Api

if TYPE_CHECKING:
    from .typing import Version

API = get_api('ayachan.api')

def get_version() -> 'Version':
    '''获取 API 版本信息

    返回:
        Version: API 版本信息
    '''
    return Api(API['version']['get']).get().json()

async def get_version_async() -> 'Version':
    '''获取 API 版本信息

    返回:
        Version: API 版本信息
    '''
    return (await Api(API['version']['get']).aget()).json()

from . import sonolus as sonolus
from . import chartmetrics as chartmetrics
