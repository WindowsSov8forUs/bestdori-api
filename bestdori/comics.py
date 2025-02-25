'''`bestdori.comics`

BanG Dream! 漫画相关操作'''
from typing import TYPE_CHECKING, Any, Dict, Literal, Optional

from . import post
from .utils import get_api
from .utils.network import Api
from .exceptions import (
    NoDataException,
    NotExistException,
    ServerNotAvailableError,
)

if TYPE_CHECKING:
    from .typing import PostList, ComicInfo, ComicsAll5

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总漫画信息
def get_all(index: Literal[5]=5) -> 'ComicsAll5':
    '''获取总漫画信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有漫画信息 `all.5.json`

    返回:
        ComicsAll5: 获取到的总漫画信息
    '''
    return Api(API['all']['comics'].format(index=index)).get().json()

# 异步获取总漫画信息
async def get_all_async(index: Literal[5]=5) -> 'ComicsAll5':
    '''获取总漫画信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有漫画信息 `all.5.json`

    返回:
        ComicsAll5: 获取到的总漫画信息
    '''
    return (await Api(API['all']['comics'].format(index=index)).aget()).json()

# 漫画类
class Comic:
    '''漫画类

    参数:
        id (int): 漫画 ID
    '''
    # 初始化
    def __init__(self, id: int, info: 'ComicInfo') -> None:
        '''漫画类

        参数:
            id (int): 漫画 ID
        '''
        self.id: int = id
        '''漫画 ID'''
        self.info: 'ComicInfo' = info
        '''漫画信息'''
        return
    
    # 漫画标题
    @property
    def title(self) -> str:
        '''漫画标题'''
        # 获取 title 数据
        title = self.info['title']
        # 获取第一个非 None 漫画标题
        try:
            return next(x for x in title if x is not None)
        except StopIteration:
            raise NoDataException('comic title')
    
    # 漫画副标题
    @property
    def sub_title(self) -> str:
        '''漫画副标题'''
        # 获取 subTitle 数据
        sub_title = self.info['subTitle']
        # 获取第一个非 None 漫画副标题
        try:
            return next(x for x in sub_title if x is not None)
        except StopIteration:
            raise NoDataException('comic subtitle')
    
    # 漫画默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''漫画默认服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        # 获取 publicStartAt 数据
        public_start_at = self.info['publicStartAt']
        # 根据 publicStartAt 数据判断服务器
        if public_start_at[0] is not None: return 'jp'
        elif public_start_at[1] is not None: return 'en'
        elif public_start_at[2] is not None: return 'tw'
        elif public_start_at[3] is not None: return 'cn'
        elif public_start_at[4] is not None: return 'kr'
        else:
            raise NoDataException('comic server')
    
    # 漫画类型
    @property
    def type(self) -> Literal['singleframe', 'fourframe']:
        '''漫画类型

        返回:
            Literal[&#39;singleframe&#39;, &#39;fourframe&#39;]: 漫画类型
        '''
        # 获取漫画数据包名称
        asset_bundle_name = self.info['assetBundleName']
        # 判断漫画类型
        if 'fourframe' in asset_bundle_name:
            return 'fourframe'
        else:
            return 'singleframe'
    
    # 获取漫画信息
    @classmethod
    def get(cls, id: int) -> 'Comic':
        '''获取漫画信息

        返回:
            Dict[str, Any]: 漫画详细信息
        '''
        _all = get_all()
        if str(id) not in _all:
            raise NotExistException(f'Comic {id}')
        return cls(id, _all[str(id)])
    
    # 异步获取漫画信息
    @classmethod
    async def get_async(cls, id: int) -> 'Comic':
        '''获取漫画信息

        返回:
            Dict[str, Any]: 漫画详细信息
        '''
        _all = await get_all_async()
        if str(id) not in _all:
            raise NotExistException(f'Comic {id}')
        return cls(id, _all[str(id)])
    
    # 获取漫画评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取漫画评论

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
            category_name='COMIC_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取漫画评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取漫画评论

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
            category_name='COMIC_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取漫画缩略图图像
    def get_thumbnail(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取漫画缩略图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画缩略图图像字节数据 `bytes`
        '''
        # 获取漫画数据包名称
        asset_bundle_name = self.info['assetBundleName']
        # 判断服务器
        public_start_at = self.info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {self.title}', server)
        return Api(
            ASSETS['comic']['thumbnail'].format(
                server=server, type=self.type, asset_bundle_name=asset_bundle_name
            )
        ).get().content
    
    # 异步获取漫画缩略图图像
    async def get_thumbnail_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取漫画缩略图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画缩略图图像字节数据 `bytes`
        '''
        # 获取漫画数据包名称
        asset_bundle_name = self.info['assetBundleName']
        # 判断服务器
        public_start_at = self.info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {self.title}', server)
        return (await Api(
            ASSETS['comic']['thumbnail'].format(
                server=server, type=self.type, asset_bundle_name=asset_bundle_name
            )
        ).aget()).content
    
    # 获取漫画图像
    def get_asset(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取漫画图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画图像字节数据 `bytes`
        '''
        # 获取漫画数据包名称
        asset_bundle_name = self.info['assetBundleName']
        # 判断服务器
        public_start_at = self.info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {self.title}', server)
        return Api(
            ASSETS['comic']['comic'].format(
                server=server, type=self.type, asset_bundle_name=asset_bundle_name
            )
        ).get().content
    
    # 异步获取漫画图像
    async def get_asset_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取漫画图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画图像字节数据 `bytes`
        '''
        # 获取漫画数据包名称
        asset_bundle_name = self.info['assetBundleName']
        # 判断服务器
        public_start_at = self.info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {self.title}', server)
        return (await Api(
            ASSETS['comic']['comic'].format(
                server=server, type=self.type, asset_bundle_name=asset_bundle_name
            )
        ).aget()).content
