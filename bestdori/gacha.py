'''`bestdori.gacha`

BanG Dream! 招募相关操作'''
import asyncio
from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional

from . import post
from .user import Me  # Me 引用保留仅用于类型检查（可后续移除）
from .utils.network import Api
from .utils import name, get_api
from .exceptions import (
    NoDataException,
    HTTPStatusError,
    NotExistException,
    AssetsNotExistError,
    ServerNotAvailableError,
)

if TYPE_CHECKING:
    from .typing import (
        NoneDict,
        PostList,
        GachaAll1,
        GachaAll3,
        GachaAll5,
        GachaInfo,
        ServerName,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总招募信息
@overload
def get_all(index: Literal[0]) -> Dict[str, 'NoneDict']:
    '''获取总招募信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有招募 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[1]) -> 'GachaAll1':
    '''获取总招募信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`

    返回:
        GachaAll1: 所有已有招募的简洁信息 `all.1.json`
    '''
    ...
@overload
def get_all(index: Literal[3]) -> 'GachaAll3':
    '''获取总招募信息

    参数:
        index (Literal[3]): 指定获取哪种 `all.json`

    返回:
        GachaAll3: 所有已有招募的较详细信息 `all.3.json`
    '''
    ...
@overload
def get_all(index: Literal[5]) -> 'GachaAll5':
    '''获取总招募信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        GachaAll5: 所有已有招募的详细信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[0, 1, 3, 5]=5) -> Union[Dict[str, 'NoneDict'], 'GachaAll1', 'GachaAll3', 'GachaAll5']:
    return Api(API['gacha']['all'].format(index=index)).get().json()

# 异步获取总招募信息
@overload
async def get_all_async(index: Literal[0]) -> Dict[str, 'NoneDict']:
    '''获取总招募信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有招募 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[1]) -> 'GachaAll1':
    '''获取总招募信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`

    返回:
        GachaAll1: 所有已有招募的简洁信息 `all.1.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[3]) -> 'GachaAll3':
    '''获取总招募信息

    参数:
        index (Literal[3]): 指定获取哪种 `all.json`

    返回:
        GachaAll3: 所有已有招募的较详细信息 `all.3.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5]) -> 'GachaAll5':
    '''获取总招募信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        GachaAll5: 所有已有招募的详细信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[0, 1, 3, 5]=5) -> Union[Dict[str, 'NoneDict'], 'GachaAll1', 'GachaAll3', 'GachaAll5']:
    return (await Api(API['gacha']['all'].format(index=index)).aget()).json()

# 招募类
class Gacha:
    '''招募类

    参数:
        id (int): 招募 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''招募类

        参数:
            id (int): 招募 ID
        '''
        self.id: int = id
        '''招募 ID'''
        self.__info: Optional['GachaInfo'] = None
        '''招募信息'''

    # me 参数已移除
    
    @property
    def info(self) -> 'GachaInfo':
        '''招募信息'''
        if not self.__info:
            raise RuntimeError(f'Gacha \'{self.id}\' info were not retrieved.')
        return self.__info
    
    # 招募标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''招募标题'''
        return self.info['gachaName']
    
    #招募默认服务器
    @property
    def __server__(self) -> 'ServerName':
        '''招募默认服务器'''
        # 获取 publishedAt 数据
        published_at = self.info['publishedAt']
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('gacha server')
    
    # 获取招募信息
    def get_info(self) -> 'GachaInfo':
        '''获取招募信息

        返回:
            GachaInfo: 招募详细信息
        '''
        try:
            response = Api(
                API['gacha']['info'].format(id=self.id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Gacha {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return self.info
    
    def __get_info__(self) -> 'GachaInfo':
        if not self.__info:
            return self.get_info()
        return self.__info
    
    # 异步获取招募信息
    async def get_info_async(self) -> 'GachaInfo':
        '''获取招募信息

        返回:
            GachaInfo: 招募详细信息
        '''
        try:
            response = await Api(
                API['gacha']['info'].format(id=self.id)
            ).aget()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Gacha {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return self.info
    
    async def __get_info_async__(self) -> 'GachaInfo':
        if not self.__info:
            return await self.get_info_async()
        return self.__info
    
    # 获取招募评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取招募评论

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
            category_name='GACHA_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
        )
    
    # 异步获取招募评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取招募评论

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
            category_name='GACHA_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
        )
    
    # 获取招募缩略图图片
    def get_banner(self, server: 'ServerName') -> bytes:
        '''获取招募缩略图图片

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 招募缩略图图片字节数据 `bytes`
        '''
        # 获取招募数据包名称
        info = self.__get_info__()
        if (banner_asset_bundle_name := info.get('bannerAssetBundleName', None)) is None:
            raise ValueError('Gacha has no banner asset bundle name.')
        # 判断服务器
        published_at = info['publishedAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if published_at[index] is None:
            raise ServerNotAvailableError(f'Gacha \'{name(self)}\'', server)
        return Api(
            ASSETS['homebanner']['get'].format(
                server=server, banner_asset_bundle_name=banner_asset_bundle_name
            )
        ).get().content
    
    # 异步获取招募缩略图图片
    async def get_banner_async(self, server: 'ServerName') -> bytes:
        '''获取招募缩略图图片

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 招募缩略图图片字节数据 `bytes`
        '''
        # 获取招募数据包名称
        info = await self.__get_info_async__()
        if (banner_asset_bundle_name := info.get('bannerAssetBundleName', None)) is None:
            raise ValueError('Gacha has no banner asset bundle name.')
        # 判断服务器
        published_at = info['publishedAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if published_at[index] is None:
            raise ServerNotAvailableError(f'Gacha \'{name(self)}\'', server)
        return (await Api(
            ASSETS['homebanner']['get'].format(
                server=server, banner_asset_bundle_name=banner_asset_bundle_name
            )
        ).aget()).content
    
    # 获取招募 pickup 图像
    def get_pickups(self, server: 'ServerName') -> List[bytes]:
        '''获取招募 pickup 图像

        参数:
            server (ServerName): 服务器

        返回:
            List[bytes]: pickup 图像字节数据 `bytes` 列表
        '''
        PICKUPS = ['pickup1', 'pickup2', 'pickup']
        # 遍历尝试获取
        pickup_list: List[bytes] = []
        for pickup in PICKUPS:
            try:
                pickup_list.append(
                    Api(
                        ASSETS['gacha']['screen'].format(
                            server=server, id=self.id, asset_name=pickup,
                        )
                    ).get().content
                )
            except:
                continue
        if len(pickup_list) <= 0:
            # 没有获取到任何 pickup 图像
            raise AssetsNotExistError('gacha pickups')
        return pickup_list
    
    # 异步获取招募 pickup 图像
    async def get_pickups_async(self, server: 'ServerName') -> List[bytes]:
        '''获取招募 pickup 图像

        参数:
            server (ServerName): 服务器

        返回:
            List[bytes]: pickup 图像字节数据 `bytes` 列表
        '''
        PICKUPS = ['pickup1', 'pickup2', 'pickup']

        # 遍历尝试获取
        async def fetch_pickup(pickup: str) -> Optional[bytes]:
            try:
                return (await Api(
                    ASSETS['gacha']['screen'].format(
                    server=server, id=self.id, asset_name=pickup,
                    )
                ).aget()).content
            except:
                return None

        pickup_list = await asyncio.gather(*(fetch_pickup(pickup) for pickup in PICKUPS))
        pickup_list = [pickup for pickup in pickup_list if pickup is not None]

        if len(pickup_list) <= 0:
            # 没有获取到任何 pickup 图像
            raise AssetsNotExistError('gacha pickups')
        return pickup_list
    
    # 获取招募 logo 图像
    def get_logo(self, server: 'ServerName') -> bytes:
        '''获取招募 logo 图像

        参数:
            server (ServerName): 服务器

        返回:
            bytes: logo 图像字节数据 `bytes`
        '''
        try:
            return Api(
                ASSETS['gacha']['screen'].format(
                    server=server, id=self.id, asset_name='logo',
                )
            ).get().content
        except:
            raise AssetsNotExistError('gacha logo')
    
    # 异步获取招募 logo 图像
    async def get_logo_async(self, server: 'ServerName') -> bytes:
        '''获取招募 logo 图像

        参数:
            server (ServerName): 服务器

        返回:
            bytes: logo 图像字节数据 `bytes`
        '''
        try:
            return (await Api(
                ASSETS['gacha']['screen'].format(
                    server=server, id=self.id, asset_name='logo',
                )
            ).aget()).content
        except:
            raise AssetsNotExistError('gacha logo')
