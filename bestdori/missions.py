'''`bestdori.missions`

BanG Dream! 任务相关操作'''
from typing import Any, Literal

from aiohttp import ClientResponseError
from httpx import Response, HTTPStatusError

from .utils.utils import API
from .utils.network import Api
from .post import get_list, get_list_async
from .exceptions import (
    NoDataException,
    MissionNotExistError
)

# 获取总任务信息
def get_all(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总任务信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有任务 ID `all.0.json`
            `5`: 获取所有已有任务的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总任务信息
    '''
    return Api(API['missions']['all'].format(index=index)).get().json()

# 异步获取总任务信息
async def get_all_async(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总任务信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有任务 ID `all.0.json`
            `5`: 获取所有已有任务的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总任务信息
    '''
    response = await Api(API['missions']['all'].format(index=index)).aget()
    if isinstance(response, Response): return response.json()
    return await response.json()

# 任务类
class Mission:
    '''任务类

    参数:
        id (int): 任务 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''任务类

        参数:
            id (int): 任务 ID
        '''
        self.id: int = id
        '''任务 ID'''
        self.__info: dict[str, Any] = {}
        '''任务信息'''
        return
    
    # 任务标题
    @property
    def title(self) -> str:
        '''任务标题'''
        info = self.__info
        # 获取 title 数据
        if (title := info.get('title', None)) is None:
            raise NoDataException('任务标题')
        # 获取第一个非 None 任务标题
        try:
            return next(filter(lambda x: x is not None, title))
        except StopIteration:
            raise NoDataException('任务标题')
    
    # 任务所在默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''任务所在默认服务器'''
        info = self.__info
        # 获取 startAt 数据
        if (start_at := info.get('startAt', None)) is None:
            raise NoDataException('任务起始时间')
        # 根据 startAt 数据判断服务器
        if start_at[0] is not None: return 'jp'
        elif start_at[1] is not None: return 'en'
        elif start_at[2] is not None: return 'tw'
        elif start_at[3] is not None: return 'cn'
        elif start_at[4] is not None: return 'kr'
        else:
            raise NoDataException('任务所在服务器')
    
    # 获取任务信息
    def get_info(self) -> dict[str, Any]:
        '''获取任务信息

        返回:
            dict[str, Any]: 任务详细信息
        '''
        try:
            response = Api(
                API['missions']['info'].format(id=self.id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise MissionNotExistError(self.id)
            raise exception
        
        self.__info = dict(response.json())
        return self.__info
    
    # 异步获取任务信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取任务信息

        返回:
            dict[str, Any]: 任务详细信息
        '''
        try:
            response = await Api(
                API['missions']['info'].format(id=self.id)
            ).aget()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise MissionNotExistError(self.id)
            raise exception
        except ClientResponseError as exception:
            if exception.status == 404:
                raise MissionNotExistError(self.id)
            raise exception
        
        if isinstance(response, Response):
            self.__info = dict(response.json())
        else:
            self.__info = dict(await response.json())
        return self.__info
    
    # 获取任务评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取任务评论

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
            category_name='MISSION_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取任务评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取任务评论

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
            category_name='MISSION_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    