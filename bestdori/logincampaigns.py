'''`bestdori.logincampaigns`

BanG Dream! 登录奖励相关操作'''
from typing import Any, Literal

from aiohttp import ClientResponseError
from httpx import Response, HTTPStatusError

from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .post import get_list, get_list_async
from .exceptions import (
    NoDataException,
    ServerNotAvailableError,
    LoginCampaignNotExistError
)

# 获取总登录奖励信息
def get_all(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总登录奖励信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有登录奖励 ID `all.0.json`
            `5`: 获取所有已有登录奖励的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总登录奖励信息
    '''
    return Api(API['loginCampaigns']['all'].format(index=index)).get().json()

# 异步获取总登录奖励信息
async def get_all_async(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总登录奖励信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有登录奖励 ID `all.0.json`
            `5`: 获取所有已有登录奖励的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总登录奖励信息
    '''
    response = await Api(API['loginCampaigns']['all'].format(index=index)).aget()
    if isinstance(response, Response): return response.json()
    return await response.json()

# 登录奖励类
class LoginCampaign:
    '''登录奖励类

    参数:
        id (int): 登录奖励 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''登录奖励类

        参数:
            id (int): 登录奖励 ID
        '''
        self.id: int = id
        '''登录奖励 ID'''
        self.__info: dict[str, Any] = {}
        '''登录奖励信息'''
        return
    
    # 登录奖励标题
    @property
    def name(self) -> str:
        '''登录奖励标题'''
        info = self.__info
        # 获取 eventName 数据
        if (caption := info.get('caption', None)) is None:
            raise NoDataException('登录奖励标题')
        # 获取第一个非 None 登录奖励标题
        try:
            return next(filter(lambda x: x is not None, caption))
        except StopIteration:
            raise NoDataException('登录奖励标题')
    
    # 登录奖励默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''登录奖励默认服务器'''
        info = self.__info
        # 获取 startAt 数据
        if (published_at := info.get('publishedAt', None)) is None:
            raise NoDataException('登录奖励起始时间')
        # 根据 startAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('登录奖励所在服务器')
    
    # 获取登录奖励信息
    def get_info(self) -> dict[str, Any]:
        '''获取登录奖励信息

        返回:
            dict[str, Any]: 登录奖励详细信息
        '''
        try:
            response = Api(
                API['loginCampaigns']['info'].format(id=self.id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise LoginCampaignNotExistError(self.id)
            raise exception
        
        self.__info = dict(response.json())
        return self.__info
    
    # 异步获取登录奖励信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取登录奖励信息

        返回:
            dict[str, Any]: 登录奖励详细信息
        '''
        try:
            response = await Api(
                API['loginCampaigns']['info'].format(id=self.id)
            ).aget()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise LoginCampaignNotExistError(self.id)
            raise exception
        except ClientResponseError as exception:
            if exception.status == 404:
                raise LoginCampaignNotExistError(self.id)
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
    
    # 获取登录奖励评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取登录奖励评论

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
            category_name='LOGINCAMPAIGN_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取登录奖励评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取登录奖励评论

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
            category_name='LOGINCAMPAIGN_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取登录奖励背景图图像
    def get_background(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取登录奖励背景图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 登录奖励背景图图像字节数据 `bytes`
        '''
        # 获取登录奖励数据包名称
        info = self.__get_info_cache()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取登录奖励数据包名称。')
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if asset_bundle_name[index] is None:
            raise ServerNotAvailableError(f'登录奖励 {self.name}', server)
        return Assets(
            ASSETS['event']['loginbouns'].format(
                asset_bundle_name=asset_bundle_name[index]
            ), server
        ).get()
    
    # 异步获取登录奖励背景图图像
    async def get_background_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取登录奖励背景图图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 登录奖励背景图图像字节数据 `bytes`
        '''
        # 获取登录奖励数据包名称
        info = await self.__get_info_cache_async()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取登录奖励数据包名称。')
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if asset_bundle_name[index] is None:
            raise ServerNotAvailableError(f'登录奖励 {self.name}', server)
        return await Assets(
            ASSETS['event']['loginbouns'].format(
                asset_bundle_name=asset_bundle_name[index]
            ), server
        ).aget()
