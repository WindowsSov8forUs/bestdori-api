'''`bestdori.festival` 团队佳节活动专属数据获取 API

包括舞台数据、活动歌曲数据'''

from typing import TYPE_CHECKING, List, Optional

from .user import Me
from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import (
        FestivalStage,
        FestivalRotationMusic,
    )

API = get_api('bestdori.api')

# 获取歌曲循环数据
def get_rotation_musics(id: int, *, me: Optional[Me] = None) -> List['FestivalRotationMusic']:
    '''获取歌曲循环数据

    参数:
        id (int): 活动 ID

    返回:
        List[FestivalRotationMusic]: 歌曲循环数据
    '''
    return Api(API['festival']['rotation_musics'].format(id=id)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取歌曲循环数据
async def get_rotation_musics_async(id: int, *, me: Optional[Me] = None) -> List['FestivalRotationMusic']:
    '''获取歌曲循环数据

    参数:
        id (int): 活动 ID

    返回:
        List[FestivalRotationMusic]: 歌曲循环数据
    '''
    return (await Api(API['festival']['rotation_musics'].format(id=id)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 获取舞台数据
def get_stages(id: int, *, me: Optional[Me] = None) -> List['FestivalStage']:
    '''获取舞台数据

    参数:
        id (int): 活动 ID

    返回:
        List[FestivalStage]: 舞台数据
    '''
    return Api(API['festival']['stages'].format(id=id)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取舞台数据
async def get_stages_async(id: int, *, me: Optional[Me] = None) -> List['FestivalStage']:
    '''获取舞台数据

    参数:
        id (int): 活动 ID

    返回:
        List[FestivalStage]: 舞台数据
    '''
    return (await Api(API['festival']['stages'].format(id=id)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()
