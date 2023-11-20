'''`bestdori.songmeta`

BanG Dream! 歌曲 Meta 相关操作'''
from typing import Optional, Literal, Any

from .utils.utils import API
from .utils.network import Api

# 获取总歌曲 Meta 信息
def get_all(index: Literal[5]=5, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总歌曲 Meta 信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有歌曲 Meta 信息 `all.5.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总歌曲 Meta 信息
    '''
    return Api(API['all']['meta'].format(index=index), proxy=proxy).request('get').json()
