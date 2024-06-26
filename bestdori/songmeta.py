'''`bestdori.songmeta`

BanG Dream! 歌曲 Meta 相关操作'''
from typing import Any, Dict, Literal

from httpx import Response

from .utils.utils import API
from .utils.network import Api

# 获取总歌曲 Meta 信息
def get_all(index: Literal[5]=5) -> Dict[str, Dict[str, Any]]:
    '''获取总歌曲 Meta 信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有歌曲 Meta 信息 `all.5.json`

    返回:
        Dict[str, Dict[str, Any]]: 获取到的总歌曲 Meta 信息
    '''
    return Api(API['all']['meta'].format(index=index)).get().json()

# 异步获取总歌曲 Meta 信息
async def get_all_async(index: Literal[5]=5) -> Dict[str, Dict[str, Any]]:
    '''获取总歌曲 Meta 信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有歌曲 Meta 信息 `all.5.json`

    返回:
        Dict[str, Dict[str, Any]]: 获取到的总歌曲 Meta 信息
    '''
    response = await Api(API['all']['meta'].format(index=index)).aget()
    if isinstance(response, Response):
        return response.json()
    else:
        return await response.json()
