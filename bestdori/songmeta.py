'''`bestdori.songmeta`

BanG Dream! 歌曲 Meta 相关操作'''
from typing_extensions import overload
from typing import TYPE_CHECKING, Union, Literal, Optional

from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import (
        SongsMetaAll2,
        SongsMetaAll5,
    )

API = get_api('bestdori.api')

# 获取总歌曲 Meta 信息
@overload
def get_all(index: Literal[2]) -> 'SongsMetaAll2':
    '''获取总歌曲 Meta 信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        SongsMetaAll2: 获取到的所有已有歌曲的 Meta 信息, 只有 7s 技能数值信息 `all.2.json`
    '''
    ...
@overload
def get_all(index: Literal[5]) -> 'SongsMetaAll5':
    '''获取总歌曲 Meta 信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        SongsMetaAll5: 获取到的所有已有歌曲的 Meta 信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[2, 5]=5) -> Union['SongsMetaAll2', 'SongsMetaAll5']:
    return Api(API['all']['meta'].format(index=index)).get().json()

# 异步获取总歌曲 Meta 信息
@overload
async def get_all_async(index: Literal[2]) -> 'SongsMetaAll2':
    '''异步获取总歌曲 Meta 信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`
    
    返回:
        SongsMetaAll2: 获取到的所有已有歌曲的 Meta 信息, 只有 7s 技能数值信息 `all.2.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5]) -> 'SongsMetaAll5':
    '''异步获取总歌曲 Meta 信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`
    
    返回:
        SongsMetaAll5: 获取到的所有已有歌曲的 Meta 信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[2, 5]=5) -> Union['SongsMetaAll2', 'SongsMetaAll5']:
    return (await Api(API['all']['meta'].format(index=index)).aget()).json()
