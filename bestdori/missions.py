'''`bestdori.missions`

BanG Dream! 任务相关操作'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional

from . import post
from .user import Me
from .utils import get_api
from .utils.network import Api
from .exceptions import (
    HTTPStatusError,
    NoDataException,
    NotExistException,
)

if TYPE_CHECKING:
    from .typing import (
        NoneDict,
        PostList,
        ServerName,
        MissionInfo,
        MissionsAll5,
    )

API = get_api('bestdori.api')

# 获取总任务信息
@overload
def get_all(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总任务信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 获取到的所有已有任务 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'MissionsAll5':
    '''获取总任务信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        MissionsAll5: 获取到的所有已有任务的简洁信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[0, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'MissionsAll5']:
    return Api(API['missions']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取总任务信息
@overload
async def get_all_async(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总任务信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 获取到的所有已有任务 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'MissionsAll5':
    '''获取总任务信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        MissionsAll5: 获取到的所有已有任务的简洁信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[0, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'MissionsAll5']:
    return (await Api(API['missions']['all'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 任务类
class Mission:
    '''任务类

    参数:
        id (int): 任务 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''任务类

        参数:
            id (int): 任务 ID
        '''
        self.id: int = id
        '''任务 ID'''
        self.__info: Optional['MissionInfo'] = None
        '''任务信息'''

        self.__me = me
        return
    
    @property
    def info(self) -> 'MissionInfo':
        '''任务信息'''
        if self.__info is None:
            raise RuntimeError(f'Mission \'{self.id}\' info were not retrieved.')
        return self.__info

    # 任务标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''任务标题'''
        return self.info['title']
    
    # 提取任务所在默认服务器
    @property
    def __server__(self) -> 'ServerName':
        '''任务所在默认服务器'''
        # 获取 startAt 数据
        start_at = self.info['startAt']
        # 根据 startAt 数据判断服务器
        if start_at[0] is not None: return 'jp'
        elif start_at[1] is not None: return 'en'
        elif start_at[2] is not None: return 'tw'
        elif start_at[3] is not None: return 'cn'
        elif start_at[4] is not None: return 'kr'
        else:
            raise NoDataException('mission server')
    
    # 获取任务信息
    def get_info(self) -> 'MissionInfo':
        '''获取任务信息

        返回:
            MissionInfo: 任务详细信息
        '''
        try:
            response = Api(
                API['missions']['info'].format(id=self.id)
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Mission {self.id}') from exception
            raise exception
        
        self.__info = response.json()
        return self.info
    
    # 异步获取任务信息
    async def get_info_async(self) -> 'MissionInfo':
        '''获取任务信息

        返回:
            MissionInfo: 任务详细信息
        '''
        try:
            response = await Api(
                API['missions']['info'].format(id=self.id)
            ).aget(
                cookies=await self.__me.__get_cookies_async__() if self.__me else None,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Mission {self.id}') from exception
            raise exception
        
        self.__info = response.json()
        return self.info
    
    # 获取任务评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取任务评论

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
            category_name='MISSION_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 异步获取任务评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取任务评论

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
            category_name='MISSION_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    