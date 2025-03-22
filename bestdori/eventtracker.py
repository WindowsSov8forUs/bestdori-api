'''`bestdori.eventtracker`

BanG Dream! 活动 PT 与排名追踪器'''
from typing import TYPE_CHECKING, List, Literal, Optional

from .user import Me
from .utils import get_api
from . import post, eventtop
from .utils.network import Api
from .exceptions import HTTPStatusError, NotExistException

if TYPE_CHECKING:
    from .typing import (
        Server,
        PostList,
        EventTopData,
        EventTrackerData,
        EventTrackerRate,
    )

API = get_api('bestdori.api')

# 获取活动追踪比率列表
def get_rates(*, me: Optional[Me] = None) -> List['EventTrackerRate']:
    '''获取活动追踪比率列表

    返回:
        List[EventTrackerRate]: 活动追踪比率列表
    '''
    return Api(API['tracker']['rates']).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取活动追踪比率列表
async def get_rates_async(*, me: Optional[Me] = None) -> List['EventTrackerRate']:
    '''异步获取活动追踪比率列表

    返回:
        List[EventTrackerRate]: 活动追踪比率列表
    '''
    return (await Api(API['tracker']['rates']).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 活动排名追踪器类
class EventTracker:
    '''活动排名追踪器类

    参数:
        server (Server): 指定服务器
        event (int): 活动 ID
    '''
    # 初始化
    def __init__(self, server: 'Server', event: int, *, me: Optional[Me] = None) -> None:
        '''活动排名追踪器类

        参数:
            server (Server): 指定服务器
            event (int): 活动 ID
            me (Optional[Me], optional): 用户验证信息
        '''
        self.server: 'Server' = server
        '''指定服务器'''
        self.event: int = event
        '''活动 ID'''

        self.__me = me
        return
    
    # 获取 T10 实时排名追踪信息
    def get_top(self, mid: int=0, *, interval: int) -> 'EventTopData':
        '''获取 T10 实时排名追踪信息

        参数:
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
            interval (int): 间隔

        返回:
            EventTopData: T10 排名数据
        '''
        return eventtop.get_data(
            server=self.server,
            event=self.event,
            mid=mid,
            interval=interval,
            me=self.__me,
        )
    
    # 异步获取 T10 实时排名追踪信息
    async def get_top_async(self, mid: int=0, *, interval: int) -> 'EventTopData':
        '''异步获取 T10 实时排名追踪信息

        参数:
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
            interval (int): 间隔

        返回:
            EventTopData: T10 排名数据
        '''
        return await eventtop.get_data_async(
            server=self.server,
            event=self.event,
            mid=mid,
            interval=interval,
            me=self.__me,
        )

    # 获取分数线追踪信息
    def get_data(self, tier: int) -> 'EventTrackerData':
        '''获取分数线追踪信息

        参数:
            tier (int): 排名

        返回:
            EventTrackerData: 分数线追踪信息
        '''
        params = {
            'server': self.server,
            'event': self.event,
            'tier': tier
        }
        
        try:
            response = Api(API['tracker']['eventtracker']).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
                params=params,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f"Event {self.event}")
            else:
                raise exception
        
        return response.json()
    
    # 异步获取分数线追踪信息
    async def get_data_async(self, tier: int) -> 'EventTrackerData':
        '''异步获取分数线追踪信息

        参数:
            tier (int): 排名

        返回:
            EventTrackerData: 分数线追踪信息
        '''
        params = {
            'server': self.server,
            'event': self.event,
            'tier': tier
        }
        
        try:
            response = await Api(API['tracker']['eventtracker']).aget(
                cookies=await self.__me.__get_cookies_async__() if self.__me else None,
                params=params,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f"Event {self.event}")
            else:
                raise exception
        
        return response.json()
    
    # 获取活动排名追踪评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取活动排名追踪评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            PostList: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[PostListPost] 列举出的评论
                }
                ```
        '''
        return post.get_list(
            category_id=f"{self.event}_{self.server}",
            category_name='EVENTTRACKER_COMMENT',
            limit=limit,
            offset=offset,
            order=order,
            me=self.__me,
        )
    
    # 异步获取活动排名追踪评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''异步获取活动排名评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            PostList: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[PostListPost] 列举出的评论
                }
                ```
        '''
        return await post.get_list_async(
            category_id=f"{self.event}_{self.server}",
            category_name='EVENTTRACKER_COMMENT',
            limit=limit,
            offset=offset,
            order=order,
            me=self.__me,
        )
