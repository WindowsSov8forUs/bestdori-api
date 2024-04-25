'''`bestdori.eventarchives`

BanG Dream! 活动数据相关操作'''
from typing import Any, Literal

from httpx import Response

from .utils.utils import API
from .utils.network import Api
from .post import get_list, get_list_async
from .exceptions import (
    EventNotExistError
)

# 获取总活动数据信息
def get_all(index: Literal[5]=5) -> dict[str, dict[str, Any]]:
    '''获取总活动信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有活动数据的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总活动信息
    '''
    return Api(API['all']['archives'].format(index=index)).get().json()

# 异步获取总活动数据信息
async def get_all_async(index: Literal[5]=5) -> dict[str, dict[str, Any]]:
    '''获取总活动信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有活动数据的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总活动信息
    '''
    response = await Api(API['all']['archives'].format(index=index)).aget()
    if isinstance(response, Response):
        return response.json()
    else:
        return await response.json()

# 活动数据类
class EventArchive:
    '''活动数据类

    参数:
        id (int): 活动 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''活动数据类

        参数:
            id (int): 活动 ID
        '''
        self.id: int = id
        '''活动 ID'''
        self.__info: dict[str, Any] = {}
        '''活动信息'''
        return
    
    # 获取活动数据信息
    def get_info(self) -> dict[str, Any]:
        '''获取活动数据信息

        返回:
            dict[str, Any]: 活动数据信息
        '''
        _all = get_all()
        if str(self.id) not in _all:
            raise EventNotExistError(self.id)
        self.__info = _all[str(self.id)]
        
        return self.__info
    
    # 异步获取活动数据信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取活动数据信息

        返回:
            dict[str, Any]: 活动数据信息
        '''
        _all = await get_all_async()
        if str(self.id) not in _all:
            raise EventNotExistError(self.id)
        self.__info = _all[str(self.id)]
        
        return self.__info
    
    # 获取排名分数线
    def get_top(
        self,
        server: Literal[0, 1, 2, 3, 4],
        mid: Literal['0']='0',
        latest: Literal['1']='1'
    ) -> dict[str, list[dict[str, Any]]]:
        '''获取排名分数线

        参数:
            server (Literal[0, 1, 2, 3, 4]): 指定服务器
                `0`: 日服
                `1`: 英服
                `2`: 台服
                `3`: 国服
                `4`: 韩服
            mid (Literal[&#39;0&#39;], optional): 指定是否为中间分数线，默认为 `0`
            latest (Literal[&#39;1&#39;], optional): 指定是否为最终分数线，默认为 `1`

        返回:
            dict[str, list[dict[str, Any]]]: 排名分数线数据
        '''
        return Api(API['events']['top']).get(
            params={
                'server': server,
                'event': self.id,
                'mid': mid,
                'latest': latest
            }
        ).json()
    
    # 异步获取排名分数线
    async def get_top_async(
        self,
        server: Literal[0, 1, 2, 3, 4],
        mid: Literal['0']='0',
        latest: Literal['1']='1'
    ) -> dict[str, list[dict[str, Any]]]:
        '''获取排名分数线

        参数:
            server (Literal[0, 1, 2, 3, 4]): 指定服务器
                `0`: 日服
                `1`: 英服
                `2`: 台服
                `3`: 国服
                `4`: 韩服
            mid (Literal[&#39;0&#39;], optional): 指定是否为中间分数线，默认为 `0`
            latest (Literal[&#39;1&#39;], optional): 指定是否为最终分数线，默认为 `1`

        返回:
            dict[str, list[dict[str, Any]]]: 排名分数线数据
        '''
        response = await Api(API['events']['top']).aget(
            params={
                'server': server,
                'event': self.id,
                'mid': mid,
                'latest': latest
            }
        )
        if isinstance(response, Response):
            return response.json()
        else:
            return await response.json()

    # 获取活动数据评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取动数据评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            dict[str, Any]: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # list[dict[str, Any]] 列举出的评论
                }
                ```
        '''
        return get_list(
            category_id=str(self.id),
            category_name='EVENTARCHIVE_COMMENT',
            limit=limit,
            offset=offset,
            order=order
        )
    
    # 异步获取活动数据评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取动数据评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            dict[str, Any]: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # list[dict[str, Any]] 列举出的评论
                }
                ```
        '''
        return await get_list_async(
            category_id=str(self.id),
            category_name='EVENTARCHIVE_COMMENT',
            limit=limit,
            offset=offset,
            order=order
        )
