'''`bestdori.comics`

BanG Dream! 漫画相关操作'''
from typing import TYPE_CHECKING, List, Literal, Optional

from . import post
from .user import Me
from .utils.network import Api
from .utils import name, get_api
from .exceptions import (
    NoDataException,
    NotExistException,
    ServerNotAvailableError,
)

if TYPE_CHECKING:
    from .typing import ServerName, PostList, ComicInfo, ComicsAll5

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总漫画信息
def get_all(index: Literal[5]=5, *, me: Optional[Me] = None) -> 'ComicsAll5':
    '''获取总漫画信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有漫画信息 `all.5.json`
        me (Optional[Me], optional): 用户验证信息

    返回:
        ComicsAll5: 获取到的总漫画信息
    '''
    return Api(API['all']['comics'].format(index=index)).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).json()

# 异步获取总漫画信息
async def get_all_async(index: Literal[5]=5, *, me: Optional[Me] = None) -> 'ComicsAll5':
    '''获取总漫画信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有漫画信息 `all.5.json`
        me (Optional[Me], optional): 用户验证信息

    返回:
        ComicsAll5: 获取到的总漫画信息
    '''
    return (await Api(API['all']['comics'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me is not None else None,
    )).json()

# 漫画类
class Comic:
    '''漫画类

    参数:
        id (int): 漫画 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''漫画类

        参数:
            id (int): 漫画 ID
        '''
        self.id: int = id
        '''漫画 ID'''
        self.__info: Optional['ComicInfo'] = None
        '''漫画信息'''

        self.__me: Optional[Me] = me
        return
    
    @property
    def info(self) -> 'ComicInfo':
        '''漫画信息'''
        if self.__info is None:
            raise ValueError(f'Comic \'{self.id}\' info were not retrieved.')
        return self.__info

    # 获取漫画信息
    def get_info(self) -> 'ComicInfo':
        '''获取漫画信息

        返回:
            ComicInfo: 漫画详细信息
        '''
        _all = get_all(me=self.__me)
        if str(self.id) not in _all:
            raise NotExistException(f'Comic {self.id}')
        self.__info = _all[str(self.id)]
        return self.info
    
    def __get_info__(self) -> 'ComicInfo':
        if self.__info is None:
            return self.get_info()
        return self.info

    # 异步获取漫画信息
    async def get_info_async(self) -> 'ComicInfo':
        '''获取漫画信息

        返回:
            ComicInfo: 漫画详细信息
        '''
        _all = await get_all_async(me=self.__me)
        if str(self.id) not in _all:
            raise NotExistException(f'Comic {self.id}')
        self.__info = _all[str(self.id)]
        return self.info
    
    async def __get_info_async__(self) -> 'ComicInfo':
        if self.__info is None:
            return await self.get_info_async()
        return self.info

    # 漫画标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''漫画标题'''
        return self.info['title']
    
    # 漫画副标题
    @property
    def __sub_title__(self) -> List[Optional[str]]:
        '''漫画副标题'''
        return self.info['subTitle']
    
    # 漫画默认服务器
    @property
    def __server__(self) -> 'ServerName':
        '''漫画默认服务器'''
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
    def __type__(self) -> Literal['singleframe', 'fourframe']:
        '''漫画类型'''
        # 获取漫画数据包名称
        asset_bundle_name = self.info['assetBundleName']
        # 判断漫画类型
        if 'fourframe' in asset_bundle_name:
            return 'fourframe'
        else:
            return 'singleframe'
    
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
            offset=offset,
            me=self.__me,
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
            offset=offset,
            me=self.__me,
        )
    
    # 获取漫画缩略图图像
    def get_thumbnail(self, server: 'ServerName') -> bytes:
        '''获取漫画缩略图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画缩略图图像字节数据 `bytes`
        '''
        info = self.__get_info__()
        # 获取漫画数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        public_start_at = info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {name(self)}', server)
        return Api(
            ASSETS['comic']['thumbnail'].format(
                server=server, type=self.__type__, asset_bundle_name=asset_bundle_name
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me is not None else None,
        ).content
    
    # 异步获取漫画缩略图图像
    async def get_thumbnail_async(self, server: 'ServerName') -> bytes:
        '''获取漫画缩略图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画缩略图图像字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取漫画数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        public_start_at = info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {name(self)}', server)
        return (await Api(
            ASSETS['comic']['thumbnail'].format(
                server=server, type=self.__type__, asset_bundle_name=asset_bundle_name
            )
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me is not None else None,
        )).content
    
    # 获取漫画图像
    def get_asset(self, server: 'ServerName') -> bytes:
        '''获取漫画图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画图像字节数据 `bytes`
        '''
        info = self.__get_info__()
        # 获取漫画数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        public_start_at = info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {name(self)}', server)
        return Api(
            ASSETS['comic']['comic'].format(
                server=server, type=self.__type__, asset_bundle_name=asset_bundle_name
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me is not None else None,
        ).content
    
    # 异步获取漫画图像
    async def get_asset_async(self, server: 'ServerName') -> bytes:
        '''获取漫画图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 漫画图像字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取漫画数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        public_start_at = info['publicStartAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if public_start_at[index] is None:
            raise ServerNotAvailableError(f'Comic {name(self)}', server)
        return (await Api(
            ASSETS['comic']['comic'].format(
                server=server, type=self.__type__, asset_bundle_name=asset_bundle_name
            )
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me is not None else None,
        )).content
