'''`bestdori.festival` 团队佳节活动专属数据获取 API

包括舞台数据、活动歌曲数据'''

from typing import Dict, List, TypedDict

from httpx import Response

from .utils.utils import API
from .utils.network import Api

# 歌曲循环数据类型
class RotationMusic(TypedDict):
    musicId: int
    startAt: str
    endAt: str

# 舞台数据类型
class Stage(TypedDict):
    type: str
    startAt: str
    endAt: str

# 获取歌曲循环数据
def get_rotation_musics(id: int) -> List[RotationMusic]:
    '''获取歌曲循环数据

    参数:
        id (int): 活动 ID

    返回:
        List[Dict[str, Any]]: 歌曲循环数据
    '''
    return Api(API['festival']['rotation_musics'].format(id=id)).get().json()

# 异步获取歌曲循环数据
async def get_rotation_musics_async(id: int) -> List[RotationMusic]:
    '''获取歌曲循环数据

    参数:
        id (int): 活动 ID

    返回:
        List[Dict[str, Any]]: 歌曲循环数据
    '''
    response = await Api(API['festival']['rotation_musics'].format(id=id)).aget()
    if isinstance(response, Response):
        return response.json()
    return await response.json()

# 获取舞台数据
def get_stages(id: int) -> List[Stage]:
    '''获取舞台数据

    参数:
        id (int): 活动 ID

    返回:
        List[Dict[str, Any]]: 舞台数据
    '''
    return Api(API['festival']['stages'].format(id=id)).get().json()

# 异步获取舞台数据
async def get_stages_async(id: int) -> List[Stage]:
    '''获取舞台数据

    参数:
        id (int): 活动 ID

    返回:
        List[Dict[str, Any]]: 舞台数据
    '''
    response = await Api(API['festival']['stages'].format(id=id)).aget()
    if isinstance(response, Response):
        return response.json()
    return await response.json()
