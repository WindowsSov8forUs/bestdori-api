'''`bestdori.costumes`

BanG Dream! 服装相关操作'''
from typing import Any, Literal

from aiohttp import ClientResponseError
from httpx import Response, HTTPStatusError

from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .post import get_list, get_list_async
from .exceptions import (
    NoDataException,
    AssetsNotExistError,
    CostumeNotExistError
)

# 获取总服装信息
def get_all(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总服装信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有服装 ID `all.0.json`
            `5`: 获取所有已有服装的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总服装信息
    '''
    return Api(API['costumes']['all'].format(index=index)).get().json()

# 异步获取总服装信息
async def get_all_async(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总服装信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有服装 ID `all.0.json`
            `5`: 获取所有已有服装的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总服装信息
    '''
    response = await Api(API['costumes']['all'].format(index=index)).aget()
    if isinstance(response, Response):
        return response.json()
    else:
        return await response.json()

# 服装类
class Costume:
    '''服装类

    参数:
        id (int): 服装 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''服装类

        参数:
            id (int): 服装 ID
        '''
        self.id: int = id
        '''服装 ID'''
        self.__info: dict[str, Any] = {}
        '''服装信息'''
        return
    
    # 角色 ID
    @property
    def character_id(self) -> int:
        '''角色 ID'''
        info = self.__info
        # 获取 characterId 数据
        if (character_id := info.get('characterId', None)) is None:
            raise NoDataException('角色 ID')
        return character_id
    
    # 卡牌 ID
    @property
    def card_id(self) -> int:
        '''卡牌 ID'''
        info = self.__info
        # 获取 cards 数据
        if (cards := info.get('cards', None)) is None:
            raise NoDataException('卡牌 ID')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(self.server)
        return cards[index]
    
    # 服装标题
    @property
    def description(self) -> str:
        '''服装标题'''
        info = self.__info
        # 获取 description 数据
        if (description := info.get('description', None)) is None:
            raise NoDataException('服装标题')
        # 获取第一个非 None 服装标题
        try:
            return next(filter(lambda x: x is not None, description))
        except StopIteration:
            raise NoDataException('服装标题')
    
    # 服装所在默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''服装所在默认服务器'''
        info = self.__info
        # 获取 publishedAt 数据
        if (published_at := info.get('publishedAt', None)) is None:
            raise NoDataException('服装发布时间')
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('服装所在服务器')
    
    # 获取服装信息
    def get_info(self) -> dict[str, Any]:
        '''获取服装信息

        返回:
            dict[str, Any]: 服装详细信息
        '''
        try:
            response = Api(
                API['costumes']['info'].format(id=self.id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise CostumeNotExistError(self.id)
            else:
                raise exception
        
        self.__info = dict(response.json())
        return self.__info
    
    # 异步获取服装信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取服装信息

        返回:
            dict[str, Any]: 服装详细信息
        '''
        try:
            response = await Api(
                API['costumes']['info'].format(id=self.id)
            ).aget()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise CostumeNotExistError(self.id)
            else:
                raise exception
        except ClientResponseError as exception:
            if exception.status == 404:
                raise CostumeNotExistError(self.id)
            else:
                raise exception
        
        if isinstance(response, Response):
            self.__info = dict(response.json())
        else:
            self.__info = dict(await response.json())
        return self.__info
    
    # 获取缓存信息
    def __get_info_cache(self) -> dict[str, Any]:
        '''获取缓存信息

        返回:
            dict[str, Any]: 服装详细信息
        '''
        if not self.__info:
            return self.get_info()
        return self.__info
    
    # 异步获取缓存信息
    async def __get_info_cache_async(self) -> dict[str, Any]:
        '''获取缓存信息

        返回:
            dict[str, Any]: 服装详细信息
        '''
        if not self.__info:
            return await self.get_info_async()
        return self.__info
    
    # 获取服装评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取服装评论

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
            category_name='COSTUME_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取服装评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取服装评论

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
            category_name='COSTUME_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取 LIVE 服装图片
    def get_sdchara(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 服装 LIVE 图片字节数据 `bytes`
        '''
        # 获取服装 sdchara 数据包名称
        info = self.__get_info_cache()
        if (sd_resource_name := info.get('sdResourceName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        return Assets(
            ASSETS['characters']['livesd'].format(
                sd_resource_name=sd_resource_name
            ), self.server
        ).get()
    
    # 异步获取 LIVE 服装图片
    async def get_sdchara_async(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 服装 LIVE 图片字节数据 `bytes`
        '''
        # 获取服装 sdchara 数据包名称
        info = await self.__get_info_cache_async()
        if (sd_resource_name := info.get('sdResourceName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        return await Assets(
            ASSETS['characters']['livesd'].format(
                sd_resource_name=sd_resource_name
            ), self.server
        ).aget()
    
    # 获取服装模型数据
    def get_build_data(self) -> bytes:
        '''获取服装模型数据

        返回:
            bytes: 服装模型数据
        '''
        # 获取服装数据包名称
        info = self.__get_info_cache()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        try:
            return Assets(
                ASSETS['live2d']['buildData'].format(
                    asset_bundle_name=asset_bundle_name
                ), self.server
            ).get()
        except AssetsNotExistError:
            raise AssetsNotExistError(f'服装模型 {asset_bundle_name}-{self.server}')
    
    # 异步获取服装模型数据
    async def get_build_data_async(self) -> bytes:
        '''获取服装模型数据

        返回:
            bytes: 服装模型数据
        '''
        # 获取服装数据包名称
        info = await self.__get_info_cache_async()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        try:
            return await Assets(
                ASSETS['live2d']['buildData'].format(
                    asset_bundle_name=asset_bundle_name
                ), self.server
            ).aget()
        except AssetsNotExistError:
            raise AssetsNotExistError(f'服装模型 {asset_bundle_name}-{self.server}')
    
    # 获取服装图标
    def get_icon(self) -> bytes:
        '''获取服装图标

        返回:
            bytes: 服装图标
        '''
        # 获取服装数据包名称
        info = self.__get_info_cache()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        try:
            return Assets(
                ASSETS['thumb']['costume'].format(
                    id=str(self.id // 50), asset_bundle_name=asset_bundle_name
                ), self.server
            ).get()
        except AssetsNotExistError:
            raise AssetsNotExistError(f'服装图标 {asset_bundle_name}-{self.server}')
    
    # 异步获取服装图标
    async def get_icon_async(self) -> bytes:
        '''获取服装图标

        返回:
            bytes: 服装图标
        '''
        # 获取服装数据包名称
        info = await self.__get_info_cache_async()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        try:
            return await Assets(
                ASSETS['thumb']['costume'].format(
                    id=str(self.id // 50), asset_bundle_name=asset_bundle_name
                ), self.server
            ).aget()
        except AssetsNotExistError:
            raise AssetsNotExistError(f'服装图标 {asset_bundle_name}-{self.server}')
