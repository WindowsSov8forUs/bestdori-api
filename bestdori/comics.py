'''`bestdori.comics`

BanG Dream! 漫画相关操作'''
from typing import Optional, Literal, Any

from .post import get_list
from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .exceptions import (
    ServerNotAvailableError,
    ComicNotExistError
)

# 获取总漫画信息
def get_all(index: Literal[5]=5, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总漫画信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有漫画信息 `all.5.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总漫画信息
    '''
    return Api(API['all']['comics'].format(index), proxy=proxy).request('get').json()

# 漫画类
class Comic:
    '''漫画类

    参数:
        id_ (int): 漫画 ID
        
        proxy (Optional[str], optional): 代理服务器
    '''
    # 初始化
    def __init__(self, id_: int, proxy: Optional[str]=None) -> None:
        '''漫画类

        参数:
            id_ (int): 漫画 ID
            
            proxy (Optional[str], optional): 代理服务器
        '''
        self.id: int = id_
        '''漫画 ID'''
        self._info: dict[str, Any] = {}
        '''漫画信息'''
        self.proxy: Optional[str] = proxy
        '''代理服务器'''
        # 检测 ID 是否存在
        all_ = get_all(5, proxy=proxy)
        if not str(id_) in all_.keys():
            raise ComicNotExistError(id_)
        self._info = all_[str(id_)]
        return
    
    # 获取漫画信息
    def get_info(self) -> dict[str, Any]:
        '''获取漫画信息

        返回:
            dict[str, Any]: 漫画详细信息
        '''
        return self._info
    
    # 获取漫画评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取漫画评论

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
            category_name='COMIC_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取漫画标题
    @property
    def title(self) -> str:
        '''获取漫画标题

        返回:
            str: 漫画标题
        '''
        info = self.get_info()
        # 获取 title 数据
        if (title := info.get('title', None)) is None:
            raise Exception('无法获取漫画标题。')
        # 获取第一个非 None 漫画标题
        try:
            return next(filter(lambda x: x is not None, title))
        except StopIteration:
            raise Exception('无法获取漫画标题。')
    
    # 获取漫画副标题
    @property
    def sub_title(self) -> str:
        '''获取漫画副标题

        返回:
            str: 漫画副标题
        '''
        info = self.get_info()
        # 获取 subTitle 数据
        if (sub_title := info.get('subTitle', None)) is None:
            raise Exception('无法获取漫画副标题。')
        # 获取第一个非 None 漫画副标题
        try:
            return next(filter(lambda x: x is not None, sub_title))
        except StopIteration:
            raise Exception('无法获取漫画副标题。')
    
    # 获取漫画默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取漫画默认服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.get_info()
        # 获取 publicStartAt 数据
        if (public_start_at := info.get('publicStartAt', None)) is None:
            raise Exception('无法获取漫画 ID 列表。')
        # 根据 publicStartAt 数据判断服务器
        if public_start_at[0] is not None: return 'jp'
        elif public_start_at[1] is not None: return 'en'
        elif public_start_at[2] is not None: return 'tw'
        elif public_start_at[3] is not None: return 'cn'
        elif public_start_at[4] is not None: return 'kr'
        else:
            raise Exception('无法获取漫画所在服务器。')

    # 获取漫画类型
    @property
    def type(self) -> Literal['singleframe', 'fourframe']:
        '''获取漫画类型

        返回:
            Literal[&#39;singleframe&#39;, &#39;fourframe&#39;]: 漫画类型
        '''
        # 获取漫画数据包名称
        info = self.get_info()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取漫画数据包名称。')
        # 判断漫画类型
        if 'fourframe' in asset_bundle_name:
            return 'fourframe'
        else:
            return 'singleframe'
    
    # 获取漫画缩略图图像
    def get_thumbnail(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取漫画缩略图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画缩略图图像字节数据 `bytes`
        '''
        # 获取漫画数据包名称
        info = self.get_info()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取漫画数据包名称。')
        # 判断服务器
        if (public_start_at := info.get('publicStartAt', None)) is None:
            raise ValueError('无法获取漫画起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'漫画 {self.title}', server)
        return Assets(
            ASSETS['comic']['thumbnail'].format(
                type=self.type, asset_bundle_name=asset_bundle_name
            ), server, self.proxy
        ).get()
    
    # 获取漫画图像
    def get(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取漫画图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画图像字节数据 `bytes`
        '''
        # 获取漫画数据包名称
        info = self.get_info()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取漫画数据包名称。')
        # 判断服务器
        if (public_start_at := info.get('publicStartAt', None)) is None:
            raise ValueError('无法获取漫画起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'漫画 {self.title}', server)
        return Assets(
            ASSETS['comic']['comic'].format(
                type=self.type, asset_bundle_name=asset_bundle_name
            ), server, self.proxy
        ).get()
