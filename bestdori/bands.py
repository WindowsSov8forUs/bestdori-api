'''`bestdori.bands`

乐队信息获取模块'''

from typing import TYPE_CHECKING, Literal, Optional

from .user import Me
from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import (
        BandsAll1,
        BandsMain1,
        ServerName,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总乐队信息
def get_all(index: Literal[1]=1, *, me: Optional[Me] = None) -> 'BandsAll1':
    '''获取总乐队信息

    参数:
        index (Literal[1], optional): 指定获取哪种 `all.json`

    返回:
        Dict[str, Dict[str, Any]]: 获取到的总乐队名称信息
    '''
    return Api(API['bands']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).json()

# 异步获取总乐队信息
async def get_all_async(index: Literal[1]=1, *, me: Optional[Me] = None) -> 'BandsAll1':
    '''获取总乐队信息

    参数:
        index (Literal[1], optional): 指定获取哪种 `all.json`

    返回:
        Dict[str, Dict[str, Any]]: 获取到的总乐队名称信息
    '''
    return (await Api(API['bands']['all'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me is not None else None,
    )).json()

# 获取主要乐队信息
def get_main(index: Literal[1]=1, *, me: Optional[Me] = None) -> 'BandsMain1':
    '''获取主要乐队信息

    参数:
        index (Literal[1], optional): 指定获取哪种 `main.json`

    返回:
        Dict[str, Dict[str, Any]]: 获取到的主要乐队信息
    '''
    return Api(API['bands']['main'].format(index=index)).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).json()

# 异步获取主要乐队信息
async def get_main_async(index: Literal[1]=1, *, me: Optional[Me] = None) -> 'BandsMain1':
    '''获取主要乐队信息

    参数:
        index (Literal[1], optional): 指定获取哪种 `main.json`

    返回:
        Dict[str, Dict[str, Any]]: 获取到的主要乐队信息
    '''
    return (await Api(API['bands']['main'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me is not None else None,
    )).json()

# 获取乐队 logo
def get_logo(
    id: int,
    type: Literal['logoS', 'logoL', 'logoL_Mask'],
    server: 'ServerName',
    *,
    me: Optional[Me] = None,
) -> bytes:
    '''获取乐队 logo

    参数:
        id (int): 乐队 ID
        
        type (Literal[&#39;logoS&#39;, &#39;logoL&#39;, &#39;logoL_Mask&#39;]): logo 类型
            `logoS`: 小 logo
            `logoL`: 大 logo
            `logoL_Mask`: 大 logo 遮罩
        
        server (ServerName): 指定服务器

    返回:
        bytes: 乐队 logo 字节数据 `bytes`
    '''
    return Api(ASSETS['band']['logo'].format(server=server, id=id, type=type)).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).content

# 异步获取乐队 logo
async def get_logo_async(
    id: int,
    type: Literal['logoS', 'logoL', 'logoL_Mask'],
    server: 'ServerName',
    *,
    me: Optional[Me] = None,
) -> bytes:
    '''获取乐队 logo

    参数:
        id (int): 乐队 ID
        
        type (Literal[&#39;logoS&#39;, &#39;logoL&#39;, &#39;logoL_Mask&#39;]): logo 类型
            `logoS`: 小 logo
            `logoL`: 大 logo
            `logoL_Mask`: 大 logo 遮罩
        
        server (ServerName): 指定服务器

    返回:
        bytes: 乐队 logo 字节数据 `bytes`
    '''
    return (await Api(ASSETS['band']['logo'].format(server=server, id=id, type=type)).aget(
        cookies=await me.__get_cookies_async__() if me is not None else None,
    )).content
