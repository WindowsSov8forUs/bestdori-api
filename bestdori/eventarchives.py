'''`bestdori.eventarchives`

BanG Dream! 活动数据相关操作'''
from typing import TYPE_CHECKING, Literal, Optional

from .user import Me
from .utils import get_api
from . import post, eventtop
from .utils.network import Api
from .exceptions import NotExistException

if TYPE_CHECKING:
    from .typing import (
        Server,
        PostList,
        EventTopData,
        EventArchiveAll5,
        EventArchiveInfo,
    )

API = get_api('bestdori.api')

# 获取总活动数据信息
def get_all(index: Literal[5]=5, *, me: Optional[Me] = None) -> 'EventArchiveAll5':
    '''获取总活动信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有活动数据的简洁信息 `all.5.json`
        me (Optional[Me], optional): 用户验证信息

    返回:
        EventArchiveAll5: 获取到的总活动信息
    '''
    return Api(API['all']['archives'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取总活动数据信息
async def get_all_async(index: Literal[5]=5, *, me: Optional[Me] = None) -> 'EventArchiveAll5':
    '''获取总活动信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有活动数据的简洁信息 `all.5.json`
        me (Optional[Me], optional): 用户验证信息

    返回:
        EventArchiveAll5: 获取到的总活动信息
    '''
    return (await Api(API['all']['archives'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 活动数据类
class EventArchive:
    '''活动数据类

    参数:
        id (int): 活动 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''活动数据类

        参数:
            id (int): 活动 ID
        '''
        self.id: int = id
        '''活动 ID'''
        self.__info: Optional['EventArchiveInfo'] = None
        '''活动信息'''

        self.__me = me
        return
    
    # 获取活动数据信息
    def get_info(self) -> 'EventArchiveInfo':
        '''获取活动数据信息

        返回:
            EventArchiveInfo: 活动数据信息
        '''
        _all = get_all(me=self.__me)
        if str(self.id) not in _all:
            raise NotExistException(f'Event archive {self.id}')
        self.__info = _all[str(self.id)]
        
        return self.__info
    
    # 异步获取活动数据信息
    async def get_info_async(self) -> 'EventArchiveInfo':
        '''获取活动数据信息

        返回:
            EventArchiveInfo: 活动数据信息
        '''
        _all = await get_all_async(me=self.__me)
        if str(self.id) not in _all:
            raise NotExistException(f'Event archive {self.id}')
        self.__info = _all[str(self.id)]
        
        return self.__info
    
    # 获取最终排名分数线
    def get_top(self, server: 'Server', mid: int = 0) -> 'EventTopData':
        '''获取排名分数线

        参数:
            server (Server): 指定服务器
                `0`: 日服
                `1`: 英服
                `2`: 台服
                `3`: 国服
                `4`: 韩服
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值

        返回:
            EventTopData: 最终排名分数线数据
        '''
        return eventtop.get_data(server, self.id, mid, latest=1, me=self.__me)
    
    # 异步获取最终排名分数线
    async def get_top_async(self, server: 'Server', mid: int = 0) -> 'EventTopData':
        '''获取排名分数线

        参数:
            server (Server): 指定服务器
                `0`: 日服
                `1`: 英服
                `2`: 台服
                `3`: 国服
                `4`: 韩服
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值

        返回:
            EventTopData: 最终排名分数线数据
        '''
        return await eventtop.get_data_async(server, self.id, mid, latest=1, me=self.__me)

    # 获取活动数据评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取活动数据评论

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
            category_id=str(self.id),
            category_name='EVENTARCHIVE_COMMENT',
            limit=limit,
            offset=offset,
            order=order,
            me=self.__me,
        )
    
    # 异步获取活动数据评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取活动数据评论

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
            category_id=str(self.id),
            category_name='EVENTARCHIVE_COMMENT',
            limit=limit,
            offset=offset,
            order=order,
            me=self.__me,
        )
