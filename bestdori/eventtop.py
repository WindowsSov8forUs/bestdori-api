'''`bestdori.eventtop`

BanG Dream! 活动 T10 排名数据'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Literal, Optional

from .user import Me
from .utils import get_api
from .utils.network import Api
from .exceptions import HTTPStatusError, NotExistException

if TYPE_CHECKING:
    from .typing import Server, EventTopData

API = get_api('bestdori.api')

# 获取活动最新 T10 排名分数线
@overload
def get_data(server: 'Server', event: int, mid: int = 0, *, interval: int, me: Optional[Me] = None) -> 'EventTopData':
    '''获取活动最新 T10 排名分数线

    参数:
        server (Server): 指定服务器
        event (int): 活动 ID
        mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
        interval (int): 间隔
        me (Optional[Me], optional): 用户验证信息
    
    返回:
        EventTopData: T10 排名数据
    '''
    ...
# 获取活动最终 T10 排名分数线
@overload
def get_data(server: 'Server', event: int, mid: int = 0, *, latest: Literal[1], me: Optional[Me] = None) -> 'EventTopData':
    '''获取活动最终 T10 排名分数线

    参数:
        server (Server): 指定服务器
        event (int): 活动 ID
        mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
        latest (Literal[1]): 获取最终排名分数线
        me (Optional[Me], optional): 用户验证信息
    
    返回:
        EventTopData: T10 排名数据
    '''
    ...

# 获取活动 T10 排名数据
def get_data(
    server: 'Server',
    event: int,
    mid: int = 0,
    *,
    interval: Optional[int] = None,
    latest: Optional[Literal[1]] = None,
    me: Optional[Me] = None,
) -> 'EventTopData':
    params = {
        'server': server,
        'event': event,
        'mid': mid,
    }
    if interval is not None:
        params['interval'] = interval
    if latest is not None:
        params['latest'] = latest
    
    try:
        response = Api(API['tracker']['eventtop']).get(
            cookies=me.__get_cookies__() if me else None,
            params=params,
        )
    except HTTPStatusError as exception:
        if exception.response.status_code == 404:
            raise NotExistException(f"Event {event}")
        else:
            raise exception
    
    return response.json()

# 异步获取活动最新 T10 排名分数线
@overload
async def get_data_async(server: 'Server', event: int, mid: int = 0, *, interval: int, me: Optional[Me] = None) -> 'EventTopData':
    '''异步获取活动最新 T10 排名分数线

    参数:
        server (Server): 指定服务器
        event (int): 活动 ID
        mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
        interval (int): 间隔
        me (Optional[Me], optional): 用户验证信息
    
    返回:
        EventTopData: T10 排名数据
    '''
    ...
# 异步获取活动最终 T10 排名分数线
@overload
async def get_data_async(server: 'Server', event: int, mid: int = 0, *, latest: Literal[1], me: Optional[Me] = None) -> 'EventTopData':
    '''异步获取活动最终 T10 排名分数线

    参数:
        server (Server): 指定服务器
        event (int): 活动 ID
        mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
        latest (Literal[1]): 获取最终排名分数线
        me (Optional[Me], optional): 用户验证信息
    
    返回:
        EventTopData: T10 排名数据
    '''
    ...

# 异步获取活动 T10 排名数据
async def get_data_async(
    server: 'Server',
    event: int,
    mid: int = 0,
    *,
    interval: Optional[int] = None,
    latest: Optional[Literal[1]] = None,
    me: Optional[Me] = None,
) -> 'EventTopData':
    params = {
        'server': server,
        'event': event,
        'mid': mid,
    }
    if interval is not None:
        params['interval'] = interval
    if latest is not None:
        params['latest'] = latest
    
    try:
        response = await Api(API['tracker']['eventtop']).aget(
            cookies=me.__get_cookies__() if me else None,
            params=params,
        )
    except HTTPStatusError as exception:
        if exception.response.status_code == 404:
            raise NotExistException(f"Event {event}")
        else:
            raise exception
    
    return response.json()