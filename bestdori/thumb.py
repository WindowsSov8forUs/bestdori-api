'''`bestdori.thumb`

各种缩略图资源获取模块'''

from typing import TYPE_CHECKING, Literal, Optional

from .user import Me
from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import ServerName

ASSETS = get_api('bestdori.assets')

# 获取卡牌缩略图
def get_chara(
    id: int,
    resource_set_name: str,
    type: Literal['normal', 'after_training'],
    *,
    server: 'ServerName',
    me: Optional[Me] = None,
) -> bytes:
    '''获取卡牌缩略图

    参数:
        id (int): 卡牌 ID
        resource_set_name (str): 资源集名称
        type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 缩略图类型
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服
    
    返回:
        bytes: 卡牌缩略图字节数据 `bytes`
    '''
    return Api(
        ASSETS['thumb']['chara'].format(
            server=server,
            id=id // 50,
            resource_set_name=resource_set_name,
            type=type,
        )
    ).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).content

# 异步获取卡牌缩略图
async def get_chara_async(
    id: int,
    resource_set_name: str,
    type: Literal['normal', 'after_training'],
    *,
    server: 'ServerName',
    me: Optional[Me] = None,
) -> bytes:
    '''获取卡牌缩略图

    参数:
        id (int): 卡牌 ID
        resource_set_name (str): 资源集名称
        type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 缩略图类型
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服
    
    返回:
        bytes: 卡牌缩略图字节数据 `bytes`
    '''
    return (await Api(
        ASSETS['thumb']['chara'].format(
            server=server,
            id=id // 50,
            resource_set_name=resource_set_name,
            type=type,
        )
    ).aget(
        cookies=await me.__get_cookies_async__() if me is not None else None,
    )).content

# 获取称号资源
def get_degree(
    degree_name: str,
    *,
    server: 'ServerName',
    me: Optional[Me] = None,
) -> bytes:
    '''获取称号资源

    参数:
        degree_name (str): 称号名称
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服

    返回:
        bytes: 称号资源字节数据 `bytes`
    '''
    return Api(ASSETS['thumb']['degree'].format(server=server, degree_name=degree_name)).get(
        cookies=me.__get_cookies__() if me else None,
    ).content

# 异步获取称号资源
async def get_degree_async(
    degree_name: str,
    *,
    server: 'ServerName',
    me: Optional[Me] = None,
) -> bytes:
    '''获取称号资源

    参数:
        degree_name (str): 称号名称
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服

    返回:
        bytes: 称号资源字节数据 `bytes`
    '''
    return (await Api(ASSETS['thumb']['degree'].format(server=server, degree_name=degree_name)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).content

# 获取服装图标
def get_costume(
    id: int,
    asset_bundle_name: str,
    *,
    server: 'ServerName',
    me: Optional[Me] = None,
) -> bytes:
    '''获取服装图标

    参数:
        id (int): 服装 ID
        asset_bundle_name (str): 服装数据包名称
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服

    返回:
        bytes: 服装图标
    '''
    return Api(
        ASSETS['thumb']['costume'].format(
            server=server, id=id // 50, asset_bundle_name=asset_bundle_name
        )
    ).get(
        cookies=me.__get_cookies__() if me else None,
    ).content

# 异步获取服装图标
async def get_costume_async(
    id: int,
    asset_bundle_name: str,
    *,
    server: 'ServerName',
    me: Optional[Me] = None,
) -> bytes:
    '''获取服装图标

    参数:
        id (int): 服装 ID
        asset_bundle_name (str): 服装数据包名称
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服
    
    返回:
        bytes: 服装图标
    '''
    return (await Api(
        ASSETS['thumb']['costume'].format(
            server=server, id=id // 50, asset_bundle_name=asset_bundle_name
        )
    ).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).content
