'''`bestdori.eventtracker`

BanG Dream! 活动 PT 与排名追踪器'''
from typing import Any, Dict, List, Literal, Optional, overload

from aiohttp import ClientResponseError
from httpx import Response, HTTPStatusError

from .utils.utils import API
from .utils.network import Api
from .post import get_list, get_list_async
from .events import get_all, get_all_async
from .exceptions import (
    EventNotExistError
)

# 活动排名追踪器类
class EventTracker:
    '''活动排名追踪器类

    参数:
        server (Literal[0, 1, 2, 3, 4]): 指定服务器
        event (int): 活动 ID
    '''
    # 初始化
    def __init__(self, server: Literal[0, 1, 2, 3, 4], event: int) -> None:
        '''活动排名追踪器类

        参数:
            server (Literal[0, 1, 2, 3, 4]): 指定服务器
            event (int): 活动 ID
        '''
        self.server: Literal[0, 1, 2, 3, 4] = server
        '''指定服务器'''
        self.event: int = event
        '''活动 ID'''
        return
    
    # 获取排名 T10 详细追踪信息
    @overload
    def get_data(self, *, mid: int, interval: int) -> Dict[str, Any]:
        '''获取排名 T10 详细追踪信息

        参数:
            mid (int): _description_
            interval (int): 间隔
        
        返回:
            Dict[str, Any]: 排名追踪信息
        '''
        ...
    
    # 获取排名追踪信息
    @overload
    def get_data(self, *, tier: int) -> Dict[str, Any]:
        '''获取排名 T10 详细追踪信息

        参数:
            tier (int): 排名
        
        返回:
            Dict[str, Any]: 排名追踪信息
        '''
        ...
    
    # 获取活动排名追踪信息
    def get_data(
        self,
        *,
        tier: Optional[int] = None,
        mid: Optional[int] = None,
        interval: Optional[int] = None
    ) -> Dict[str, Any]:
        _all = get_all()
        if str(self.event) not in _all:
            raise EventNotExistError(self.event)
        
        params = {
            'server': self.server,
            'event': self.event
        }
        if tier is not None:
            params['tier'] = tier
        else:
            if mid is None or interval is None:
                raise ValueError('若不指定 `tier` 则 `mid` 与 `interval` 必须同时指定')
            params['mid'] = mid
            params['interval'] = interval
        
        try:
            if tier is not None:
                response = Api(API['tracker']['eventtracker']).get(params=params)
            else:
                response = Api(API['tracker']['eventtop']).get(params=params)
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise EventNotExistError(self.event)
            else:
                raise exception
        
        return dict(response.json())
    
    # 异步获取排名 T10 详细追踪信息
    @overload
    async def get_data_async(self, *, mid: int, interval: int) -> Dict[str, Any]:
        '''异步获取排名 T10 详细追踪信息

        参数:
            mid (int): _description_
            interval (int): 间隔
        
        返回:
            Dict[str, Any]: 排名追踪信息
        '''
        ...
    
    # 异步获取排名追踪信息
    @overload
    async def get_data_async(self, *, tier: int) -> Dict[str, Any]:
        '''异步获取排名 T10 详细追踪信息

        参数:
            tier (int): 排名
        
        返回:
            Dict[str, Any]: 排名追踪信息
        '''
        ...
    
    # 异步获取活动排名追踪信息
    async def get_data_async(
        self,
        *,
        tier: Optional[int] = None,
        mid: Optional[int] = None,
        interval: Optional[int] = None
    ) -> Dict[str, Any]:
        _all = await get_all_async()
        if str(self.event) not in _all:
            raise EventNotExistError(self.event)
        
        params = {
            'server': self.server,
            'event': self.event
        }
        if tier is not None:
            params['tier'] = tier
        else:
            if mid is None or interval is None:
                raise ValueError('若不指定 `tier` 则 `mid` 与 `interval` 必须同时指定')
            params['mid'] = mid
            params['interval'] = interval
        
        try:
            if tier is not None:
                response = await Api(API['tracker']['eventtracker']).aget(params=params)
            else:
                response = await Api(API['tracker']['eventtop']).aget(params=params)
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise EventNotExistError(self.event)
            else:
                raise exception
        except ClientResponseError as exception:
            if exception.status == 404:
                raise EventNotExistError(self.event)
            else:
                raise exception
        
        if isinstance(response, Response):
            return dict(response.json())
        else:
            return dict(await response.json())
    
    # 获取活动排名追踪评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> Dict[str, Any]:
        '''获取活动排名追踪评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            Dict[str, Any]: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[Dict[str, Any]] 列举出的评论
                }
                ```
        '''
        return get_list(
            category_id=f"{self.event}_{self.server}",
            category_name='EVENTTRACKER_COMMENT',
            limit=limit,
            offset=offset,
            order=order
        )
    
    # 异步获取活动排名追踪评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> Dict[str, Any]:
        '''异步获取活动排名评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            Dict[str, Any]: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[Dict[str, Any]] 列举出的评论
                }
                ```
        '''
        return await get_list_async(
            category_id=f"{self.event}_{self.server}",
            category_name='EVENTTRACKER_COMMENT',
            limit=limit,
            offset=offset,
            order=order
        )
