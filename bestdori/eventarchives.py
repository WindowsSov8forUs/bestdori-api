'''`bestdori.eventarchives`

BanG Dream! 活动数据相关操作'''
from typing import Any, Literal

from .post import get_list
from .utils.utils import API
from .utils.network import Api
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
    return Api(API['all']['archives'].format(index=index)).request('get').json()

# 活动数据类
class EventArchive():
    '''活动数据类

    参数:
        id_ (int): 活动 ID
    '''
    # 初始化
    def __init__(self, id_: int) -> None:
        '''活动数据类

        参数:
            id_ (int): 活动 ID
        '''
        self.id: int = id_
        '''活动 ID'''
        self._info: dict[str, Any] = {}
        '''活动信息'''
        # 检测 ID 是否存在
        all_id = get_all(5)
        if not str(id_) in all_id.keys():
            raise EventNotExistError(id_)
        return
    
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
        return Api(API['events']['top']).request(
            'get', params={
                'server': server,
                'event': self.id,
                'mid': mid,
                'latest': latest
            }
        ).json()

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
            result: bool # 是否有响应
            count: int # 搜索到的评论总数
            posts: list[dict[str, Any]] # 列举出的评论
            ```
        '''
        return get_list(
            category_id=str(self.id),
            category_name='EVENTARCHIVE_COMMENT',
            limit=limit,
            offset=offset,
            order=order
        )
