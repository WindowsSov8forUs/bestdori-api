'''`bestdori.events`

BanG Dream! 活动相关操作'''
from typing import Any, Literal, Optional

from aiohttp import ClientResponseError
from httpx import Response, HTTPStatusError

from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .eventarchives import EventArchive
from .post import get_list, get_list_async
from .exceptions import (
    NoDataException,
    EventNotExistError,
    AssetsNotExistError,
    EventHasNoStampError,
    ServerNotAvailableError
)

# 获取总活动信息
def get_all(index: Literal[0, 5, 6]=5) -> dict[str, dict[str, Any]]:
    '''获取总活动信息

    参数:
        index (Literal[0, 5, 6], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有活动 ID `all.0.json`
            `5`: 获取所有已有活动的简洁信息 `all.5.json`
            `6`: 获取所有已有活动的简洁信息 `all.6.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总活动信息
    '''
    return Api(API['events']['all'].format(index=index)).get().json()

# 异步获取总活动信息
async def get_all_async(index: Literal[0, 5, 6]=5) -> dict[str, dict[str, Any]]:
    '''获取总活动信息

    参数:
        index (Literal[0, 5, 6], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有活动 ID `all.0.json`
            `5`: 获取所有已有活动的简洁信息 `all.5.json`
            `6`: 获取所有已有活动的简洁信息 `all.6.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总活动信息
    '''
    response = await Api(API['events']['all'].format(index=index)).aget()
    if isinstance(response, Response):
        return response.json()
    else:
        return await response.json()

# 活动类
class Event:
    '''活动类

    参数:
        id (int): 活动 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''活动类

        参数:
            id (int): 活动 ID
        '''
        self.id: int = id
        '''活动 ID'''
        self.archive: EventArchive = EventArchive(self.id)
        '''活动数据'''
        self.__info: dict[str, Any] = {}
        '''活动信息'''
        return
    
    # 活动标题
    @property
    def name(self) -> str:
        '''活动标题'''
        info = self.__info
        # 获取 eventName 数据
        if (event_name := info.get('eventName', None)) is None:
            raise NoDataException('活动标题')
        # 获取第一个非 None 活动标题
        try:
            return next(filter(lambda x: x is not None, event_name))
        except StopIteration:
            raise NoDataException('活动标题')
    
    # 活动默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''活动默认服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.__info
        # 获取 startAt 数据
        if (start_at := info.get('startAt', None)) is None:
            raise NoDataException('活动起始时间')
        # 根据 startAt 数据判断服务器
        if start_at[0] is not None: return 'jp'
        elif start_at[1] is not None: return 'en'
        elif start_at[2] is not None: return 'tw'
        elif start_at[3] is not None: return 'cn'
        elif start_at[4] is not None: return 'kr'
        else:
            raise NoDataException('活动所在服务器')
    
    # 获取活动信息
    def get_info(self) -> dict[str, Any]:
        '''获取活动信息

        返回:
            dict[str, Any]: 活动详细信息
        '''
        try:
            response = Api(
                API['events']['info'].format(id=self.id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise EventNotExistError(self.id)
            else:
                raise exception
        
        self._info = dict(response.json())
        return self._info
    
    # 异步获取活动信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取活动信息

        返回:
            dict[str, Any]: 活动详细信息
        '''
        try:
            response = await Api(
                API['events']['info'].format(id=self.id)
            ).aget()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise EventNotExistError(self.id)
            else:
                raise exception
        except ClientResponseError as exception:
            if exception.status == 404:
                raise EventNotExistError(self.id)
            else:
                raise exception
        
        if isinstance(response, Response):
            self._info = dict(response.json())
        else:
            self._info = dict(await response.json())
        return self._info
    
    # 获取缓存信息
    def __get_info_cache(self) -> dict[str, Any]:
        '''获取缓存信息

        返回:
            dict[str, Any]: 活动详细信息
        '''
        if not self._info:
            return self.get_info()
        return self._info
    
    # 异步获取缓存信息
    async def __get_info_cache_async(self) -> dict[str, Any]:
        '''获取缓存信息

        返回:
            dict[str, Any]: 活动详细信息
        '''
        if not self._info:
            return await self.get_info_async()
        return self._info
    
    # 获取活动评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取活动评论

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
            category_name='EVENT_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取活动评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取活动评论

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
            category_name='EVENT_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取活动缩略图图像
    def get_banner(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取活动缩略图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 活动缩略图图像字节数据 `bytes`
        '''
        # 获取活动数据包名称
        info = self.__get_info_cache()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取活动数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取活动起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return Assets(
            ASSETS['event']['banner'].format(
                asset_bundle_name=asset_bundle_name
            ), server
        ).get()
    
    # 异步获取活动缩略图图像
    async def get_banner_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取活动缩略图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 活动缩略图图像字节数据 `bytes`
        '''
        # 获取活动数据包名称
        info = await self.__get_info_cache_async()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取活动数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取活动起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return await Assets(
            ASSETS['event']['banner'].format(
                asset_bundle_name=asset_bundle_name
            ), server
        ).aget()
    
    # 获取活动 logo 图像
    def get_logo(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取活动 logo 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 活动 logo 图像字节数据 `bytes`
        '''
        # 获取活动数据包名称
        info = self.__get_info_cache()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取活动数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取活动起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return Assets(
            ASSETS['event']['logo'].format(
                asset_bundle_name=asset_bundle_name
            ), server
        ).get()
    
    # 异步获取活动 logo 图像
    async def get_logo_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取活动 logo 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 活动 logo 图像字节数据 `bytes`
        '''
        # 获取活动数据包名称
        info = await self.__get_info_cache_async()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取活动数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取活动起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return await Assets(
            ASSETS['event']['logo'].format(
                asset_bundle_name=asset_bundle_name
            ), server
        ).aget()

    # 获取活动主界面图像
    def get_topscreen(
        self,
        server: Literal['jp', 'en', 'tw', 'cn', 'kr'],
        type: Literal['bg', 'trim']
    ) -> bytes:
        '''获取活动主界面图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器
            
            type (Literal[&#39;bg&#39;, &#39;trim&#39;]): 图像类型
                `bg`: 背景图像
                `trim`: 角色图像

        返回:
            bytes: 活动主界面图像字节数据 `bytes`
        '''
        # 获取活动数据包名称
        info = self.__get_info_cache()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取活动数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取活动起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return Assets(
            ASSETS['event']['topscreen'].format(
                asset_bundle_name=asset_bundle_name, type=type
            ), server
        ).get()
    
    # 异步获取活动主界面图像
    async def get_topscreen_async(
        self,
        server: Literal['jp', 'en', 'tw', 'cn', 'kr'],
        type: Literal['bg', 'trim']
    ) -> bytes:
        '''获取活动主界面图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器
            
            type (Literal[&#39;bg&#39;, &#39;trim&#39;]): 图像类型
                `bg`: 背景图像
                `trim`: 角色图像

        返回:
            bytes: 活动主界面图像字节数据 `bytes`
        '''
        # 获取活动数据包名称
        info = await self.__get_info_cache_async()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取活动数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取活动起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return await Assets(
            ASSETS['event']['topscreen'].format(
                asset_bundle_name=asset_bundle_name, type=type
            ), server
        ).aget()
    
    # 获取活动奖励稀有表情
    def get_stamp(self) -> bytes:
        '''获取活动奖励稀有表情

        返回:
            bytes: 活动奖励稀有表情字节数据 `bytes`
        '''
        info = self.__get_info_cache()
        # 获取活动点数奖励列表
        if (point_rewards := info.get('pointRewards', None)) is None:
            raise NoDataException('活动奖励')
        # 获取第一个非 None 奖励列表
        try:
            point_reward = next(filter(lambda x: x is not None, point_rewards))
        except StopIteration:
            raise NoDataException('活动奖励')
        # 获取 rewardType 为 stamp 的活动奖励
        try:
            reward = next(filter(lambda x: x['rewardType'] == 'stamp', point_reward))
        except StopIteration:
            raise EventHasNoStampError(self.id)
        stamp_id = reward['rewardId']
        # 获取全部贴纸资源
        stamps = Api(
            API['all']['stamps'].format(index=2)
        ).get().json()
        if (stamp := stamps.get(stamp_id, None)) is None:
            raise AssetsNotExistError(f'贴纸 {stamp_id}')
        # 获取贴纸资源
        image_name = stamp['imageName']
        return Assets(
            ASSETS['stamp']['get'].format(image_name=image_name), self.server
        ).get()
    
    # 异步获取活动奖励稀有表情
    async def get_stamp_async(self) -> bytes:
        '''获取活动奖励稀有表情

        返回:
            bytes: 活动奖励稀有表情字节数据 `bytes`
        '''
        info = await self.__get_info_cache_async()
        # 获取活动点数奖励列表
        if (point_rewards := info.get('pointRewards', None)) is None:
            raise NoDataException('活动奖励')
        # 获取第一个非 None 奖励列表
        try:
            point_reward = next(filter(lambda x: x is not None, point_rewards))
        except StopIteration:
            raise NoDataException('活动奖励')
        # 获取 rewardType 为 stamp 的活动奖励
        try:
            reward = next(filter(lambda x: x['rewardType'] == 'stamp', point_reward))
        except StopIteration:
            raise EventHasNoStampError(self.id)
        stamp_id = reward['rewardId']
        # 获取全部贴纸资源
        stamps = await Api(
            API['all']['stamps'].format(index=2)
        ).aget()
        if isinstance(stamps, Response):
            stamps = stamps.json()
        else:
            stamps = await stamps.json()
        if (stamp := stamps.get(stamp_id, None)) is None:
            raise AssetsNotExistError(f'贴纸 {stamp_id}')
        # 获取贴纸资源
        image_name = stamp['imageName']
        return await Assets(
            ASSETS['stamp']['get'].format(image_name=image_name), self.server
        ).aget()

    # 获取排名分数线
    def get_top(
        self,
        server: Optional[Literal[0, 1, 2, 3, 4]]=None,
        mid: Literal['0']='0',
        latest: Literal['1']='1'
    ) -> dict[str, list[dict[str, Any]]]:
        '''获取排名分数线

        参数:
            server (Optional[Literal[0, 1, 2, 3, 4]], optional): 指定服务器
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
        if server is None:
            self.__get_info_cache()
            if self.server == 'jp': server = 0
            elif self.server == 'en': server = 1
            elif self.server == 'tw': server = 2
            elif self.server == 'cn': server = 3
            elif self.server == 'kr': server = 4
            else: raise NoDataException('活动服务器')
        return self.archive.get_top(server, mid, latest)
    
    # 异步获取排名分数线
    async def get_top_async(
        self,
        server: Optional[Literal[0, 1, 2, 3, 4]]=None,
        mid: Literal['0']='0',
        latest: Literal['1']='1'
    ) -> dict[str, list[dict[str, Any]]]:
        '''获取排名分数线

        参数:
            server (Optional[Literal[0, 1, 2, 3, 4]], optional): 指定服务器
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
        if server is None:
            await self.__get_info_cache_async()
            if self.server == 'jp': server = 0
            elif self.server == 'en': server = 1
            elif self.server == 'tw': server = 2
            elif self.server == 'cn': server = 3
            elif self.server == 'kr': server = 4
            else: raise NoDataException('活动服务器')
        return await self.archive.get_top_async(server, mid, latest)
