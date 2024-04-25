'''`bestdori.gacha`

BanG Dream! 招募相关操作'''
import asyncio
from typing import Any, Literal

from aiohttp import ClientResponseError
from httpx import Response, HTTPStatusError

from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .post import get_list, get_list_async
from .exceptions import (
    NoDataException,
    GachaNotExistError,
    AssetsNotExistError,
    ServerNotAvailableError
)

# 获取总招募信息
def get_all(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总招募信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有招募 ID `all.0.json`
            `5`: 获取所有已有招募的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总招募信息
    '''
    return Api(API['gacha']['all'].format(index=index)).get().json()

# 异步获取总招募信息
async def get_all_async(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总招募信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有招募 ID `all.0.json`
            `5`: 获取所有已有招募的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总招募信息
    '''
    response = await Api(API['gacha']['all'].format(index=index)).aget()
    if isinstance(response, Response):
        return response.json()
    else:
        return await response.json()

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
        self.__info: dict[str, Any] = {}
        '''招募信息'''
        return
    
    # 获取招募标题
    @property
    def name(self) -> str:
        '''获取招募标题

        返回:
            str: 招募标题
        '''
        info = self.__info
        # 获取 eventName 数据
        if (gacha_name := info.get('gachaName', None)) is None:
            raise NoDataException('招募标题')
        # 获取第一个非 None 招募标题
        try:
            return next(filter(lambda x: x is not None, gacha_name))
        except StopIteration:
            raise NoDataException('招募标题')
    
    # 获取招募默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取招募默认服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.__info
        # 获取 publishedAt 数据
        if (published_at := info.get('publishedAt', None)) is None:
            raise NoDataException('招募起始时间')
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('招募所在服务器')
    
    # 获取招募信息
    def get_info(self) -> dict[str, Any]:
        '''获取招募信息

        返回:
            dict[str, Any]: 招募详细信息
        '''
        try:
            response = Api(
                API['gacha']['info'].format(id=self.id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise GachaNotExistError(self.id)
            else:
                raise exception
        
        self.__info = dict(response.json())
        return self.__info
    
    # 异步获取招募信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取招募信息

        返回:
            dict[str, Any]: 招募详细信息
        '''
        try:
            response = await Api(
                API['gacha']['info'].format(id=self.id)
            ).aget()
        except ClientResponseError as exception:
            if exception.status == 404:
                raise GachaNotExistError(self.id)
            else:
                raise exception
        
        self.__info = dict(await response.json())
        return self.__info
    
    # 获取缓存信息
    def __get_info_cache(self) -> dict[str, Any]:
        '''获取缓存信息

        返回:
            dict[str, Any]: 缓存信息
        '''
        if not self.__info:
            return self.get_info()
        return self.__info
    
    # 异步获取缓存信息
    async def __get_info_cache_async(self) -> dict[str, Any]:
        '''获取缓存信息

        返回:
            dict[str, Any]: 缓存信息
        '''
        if not self.__info:
            return await self.get_info_async()
        return self.__info
    
    # 获取招募评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取招募评论

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
            category_name='GACHA_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取招募评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取招募评论

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
            category_name='GACHA_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取招募缩略图图片
    def get_banner(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取招募缩略图图片

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 招募缩略图图片字节数据 `bytes`
        '''
        # 获取招募数据包名称
        info = self.__get_info_cache()
        if (banner_asset_bundle_name := info.get('bannerAssetBundleName', None)) is None:
            raise ValueError('无法获取招募数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取招募起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'招募 {self.name}', server)
        return Assets(
            ASSETS['homebanner']['get'].format(
                banner_asset_bundle_name=banner_asset_bundle_name
            ), server
        ).get()
    
    # 异步获取招募缩略图图片
    async def get_banner_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取招募缩略图图片

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 招募缩略图图片字节数据 `bytes`
        '''
        # 获取招募数据包名称
        info = await self.__get_info_cache_async()
        if (banner_asset_bundle_name := info.get('bannerAssetBundleName', None)) is None:
            raise ValueError('无法获取招募数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取招募起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'招募 {self.name}', server)
        return await Assets(
            ASSETS['homebanner']['get'].format(
                banner_asset_bundle_name=banner_asset_bundle_name
            ), server
        ).aget()
    
    # 获取招募 pickup 图像
    def get_pickups(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> list[bytes]:
        '''获取招募 pickup 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 服务器

        返回:
            list[bytes]: pickup 图像字节数据 `bytes` 列表
        '''
        PICKUPS = ['pickup1', 'pickup2', 'pickup']
        # 遍历尝试获取
        pickup_list: list[bytes] = []
        for pickup in PICKUPS:
            try:
                pickup_list.append(
                    Assets(
                        ASSETS['gacha']['screen'].format(
                            id=self.id, asset_name=pickup
                        ), server
                    ).get()
                )
            except:
                continue
        if len(pickup_list) <= 0:
            # 没有获取到任何 pickup 图像
            raise AssetsNotExistError('招募 pickup 图像')
        return pickup_list
    
    # 异步获取招募 pickup 图像
    async def get_pickups_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> list[bytes]:
        '''获取招募 pickup 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 服务器

        返回:
            list[bytes]: pickup 图像字节数据 `bytes` 列表
        '''
        PICKUPS = ['pickup1', 'pickup2', 'pickup']
        # 遍历尝试获取
        pickup_list: list[bytes] = []
        tasks = [Assets(ASSETS['gacha']['screen'].format(id=self.id, asset_name=pickup), server).aget() for pickup in PICKUPS]
        for task in asyncio.as_completed(tasks):
            try:
                pickup_list.append(await task)
            except:
                continue
        if len(pickup_list) <= 0:
            # 没有获取到任何 pickup 图像
            raise AssetsNotExistError('招募 pickup 图像')
        return pickup_list
    
    # 获取招募 logo 图像
    def get_logo(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取招募 logo 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 服务器

        返回:
            bytes: logo 图像字节数据 `bytes`
        '''
        try:
            return Assets(
                ASSETS['gacha']['screen'].format(
                    id=self.id, asset_name='logo'
                ), server
            ).get()
        except:
            raise AssetsNotExistError('招募 logo 图像')
    
    # 异步获取招募 logo 图像
    async def get_logo_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取招募 logo 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 服务器

        返回:
            bytes: logo 图像字节数据 `bytes`
        '''
        try:
            return await Assets(
                ASSETS['gacha']['screen'].format(
                    id=self.id, asset_name='logo'
                ), server
            ).aget()
        except:
            raise AssetsNotExistError('招募 logo 图像')
