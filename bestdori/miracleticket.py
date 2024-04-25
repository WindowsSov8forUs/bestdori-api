'''`bestdori.miracleticket`

BanG Dream! 自选券相关操作'''
from typing import Any, Literal

from httpx import Response

from .utils.utils import API
from .utils.network import Api
from .exceptions import (
    NoDataException,
    ServerNotAvailableError,
    MiracleTicketExchangeNotExistError
)

# 获取总自选券信息
def get_all(index: Literal[5]=5) -> dict[str, dict[str, Any]]:
    '''获取总自选券信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有自选券信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总自选券信息
    '''
    return Api(
        API['all']['miracleTicketExchanges'].format(index=index)
    ).get().json()

# 异步获取总自选券信息
async def get_all_async(index: Literal[5]=5) -> dict[str, dict[str, Any]]:
    '''获取总自选券信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有自选券信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总自选券信息
    '''
    response = await Api(
        API['all']['miracleTicketExchanges'].format(index=index)
    ).aget()
    if isinstance(response, Response): return response.json()
    return await response.json()

# 自选券类
class MiracleTicketExchange:
    '''自选券类

    参数:
        id (int): 自选券 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''自选券类

        参数:
            id (int): 自选券 ID
        '''
        self.id: int = id
        '''自选券 ID'''
        self.__info: dict[str, Any] = {}
        '''自选券信息'''
        return
    
    # 自选券标题
    @property
    def name(self) -> str:
        '''自选券标题'''
        info = self.__info
        # 获取 eventName 数据
        if (name := info.get('name', None)) is None:
            raise NoDataException('自选券标题')
        # 获取第一个非 None 自选券标题
        try:
            return next(filter(lambda x: x is not None, name))
        except StopIteration:
            raise NoDataException('自选券标题')
    
    # 自选券默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''自选券默认服务器'''
        info = self.__info
        # 获取 ids 数据
        if (ids := info.get('ids', None)) is None:
            raise NoDataException('自选券 ID 列表')
        # 根据 ids 数据判断服务器
        if ids[0] is not None: return 'jp'
        elif ids[1] is not None: return 'en'
        elif ids[2] is not None: return 'tw'
        elif ids[3] is not None: return 'cn'
        elif ids[4] is not None: return 'kr'
        else:
            raise NoDataException('自选券所在服务器')
    
    # 获取自选券信息
    def get_info(self) -> dict[str, Any]:
        '''获取自选券信息

        返回:
            dict[str, Any]: 自选券详细信息
        '''
        _all = get_all(5)
        if not self.id in _all.keys():
            raise MiracleTicketExchangeNotExistError(self.id)
        self.__info = _all[str(self.id)]
        return self.__info
    
    # 异步获取自选券信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取自选券信息

        返回:
            dict[str, Any]: 自选券详细信息
        '''
        _all = await get_all_async(5)
        if not self.id in _all.keys():
            raise MiracleTicketExchangeNotExistError(self.id)
        self.__info = _all[str(self.id)]
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
    
    # 获取自选券 ID 列表
    def get_ids(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> list[int]:
        '''获取自选券 ID 列表

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            list[int]: 自选券 ID 列表
        '''
        info = self.__get_info_cache()
        # 获取 ids 数据
        if (ids := info.get('ids', None)) is None:
            raise NoDataException('自选券 ID 列表')
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if ids[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return ids[index]
    
    # 异步获取自选券 ID 列表
    async def get_ids_async(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> list[int]:
        '''获取自选券 ID 列表

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            list[int]: 自选券 ID 列表
        '''
        info = await self.__get_info_cache_async()
        # 获取 ids 数据
        if (ids := info.get('ids', None)) is None:
            raise NoDataException('自选券 ID 列表')
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if ids[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return ids[index]
