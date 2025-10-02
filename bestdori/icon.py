'''`bestdori.icon`

各种图标资源获取模块'''

from typing import TYPE_CHECKING, Optional

from .user import Me
from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import ServerName

RES = get_api('bestdori.res')

# 获取乐队图标
def get_band(id: int, *, me: Optional[Me] = None) -> bytes:
    '''获取乐队图标

    参数:
        id (int): 乐队 ID

    返回:
        bytes: 乐队图标字节数据
    '''
    # 统一使用全局 Cookies，不再读取 me
    return Api(RES['icon']['svg'].format(name=f'band_{id}')).get().content

# 异步获取乐队图标
async def get_band_async(id: int, *, me: Optional[Me] = None) -> bytes:
    '''获取乐队图标

    参数:
        id (int): 乐队 ID

    返回:
        bytes: 乐队图标字节数据
    '''
    return (await Api(RES['icon']['svg'].format(name=f'band_{id}')).aget()).content

# 获取服务器图标
def get_server(server: 'ServerName', *, me: Optional[Me] = None) -> bytes:
    '''获取服务器图标

    参数:
        server (ServerName): 服务器名称
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服

    返回:
        bytes: 服务器图标字节数据
    '''
    return Api(RES['icon']['svg'].format(name=server)).get().content

# 异步获取服务器图标
async def get_server_async(server: 'ServerName', *, me: Optional[Me] = None) -> bytes:
    '''获取服务器图标

    参数:
        server (ServerName): 服务器名称
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服

    返回:
        bytes: 服务器图标字节数据
    '''
    return (await Api(RES['icon']['svg'].format(name=server)).aget()).content
