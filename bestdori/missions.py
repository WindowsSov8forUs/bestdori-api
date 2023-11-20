'''`bestdori.missions`

BanG Dream! 任务相关操作'''
from typing import Optional, Literal, Any

from .post import get_list
from .utils.utils import API
from .utils.network import Api
from .exceptions import (
    MissionNotExistError
)

# 获取总任务信息
def get_all(index: Literal[0, 5]=5, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总任务信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有任务 ID `all.0.json`
            `5`: 获取所有已有任务的简洁信息 `all.5.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总任务信息
    '''
    return Api(API['missions']['all'].format(index), proxy=proxy).request('get').json()

# 任务类
class Mission:
    '''任务类

    参数:
        id_ (int): 任务 ID
        
        proxy (Optional[str], optional): 代理服务器
    '''
    # 初始化
    def __init__(self, id_: int, proxy: Optional[str]=None) -> None:
        '''任务类

        参数:
            id_ (int): 任务 ID
            
            proxy (Optional[str], optional): 代理服务器
        '''
        self.id: int = id_
        '''任务 ID'''
        self._info: dict[str, Any] = {}
        '''任务信息'''
        self.proxy: Optional[str] = proxy
        '''代理服务器'''
        # 检测 ID 是否存在
        all_id = get_all(0, proxy=proxy)
        if not str(id_) in all_id.keys():
            raise MissionNotExistError(id_)
        return
    
    # 获取任务信息
    def get_info(self) -> dict[str, Any]:
        '''获取任务信息

        返回:
            dict[str, Any]: 任务详细信息
        '''
        if len(self._info) <= 0:
            # 如果没有任务信息存储
            response = Api(
                API['missions']['info'].format(self.id), proxy=self.proxy
            ).request('get')
            self._info = dict(response.json())
        return self._info
    
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
            result: bool # 是否有响应
            count: int # 搜索到的评论总数
            posts: list[dict[str, Any]] # 列举出的评论
            ```
        '''
        return get_list(
            proxy=self.proxy,
            category_name='MISSION_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取任务标题
    @property
    def title(self) -> str:
        '''获取任务标题

        返回:
            str: 任务标题
        '''
        info = self.get_info()
        # 获取 title 数据
        if (title := info.get('title', None)) is None:
            raise Exception('无法获取任务标题。')
        # 获取第一个非 None 任务标题
        try:
            return next(filter(lambda x: x is not None, title))
        except StopIteration:
            raise Exception('无法获取任务标题。')
    
    # 获取任务所在服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取任务所在服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.get_info()
        # 获取 startAt 数据
        if (start_at := info.get('startAt', None)) is None:
            raise Exception('无法获取任务起始时间。')
        # 根据 startAt 数据判断服务器
        if start_at[0] is not None: return 'jp'
        elif start_at[1] is not None: return 'en'
        elif start_at[2] is not None: return 'tw'
        elif start_at[3] is not None: return 'cn'
        elif start_at[4] is not None: return 'kr'
        else:
            raise Exception('无法获取任务所在服务器。')
    