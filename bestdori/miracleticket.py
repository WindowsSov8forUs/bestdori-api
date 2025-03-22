'''`bestdori.miracleticket`

BanG Dream! 自选券相关操作'''
from typing import TYPE_CHECKING, List, Literal, Optional

from .user import Me
from .utils.network import Api
from .utils import name, get_api
from .exceptions import (
    NoDataException,
    NotExistException,
    ServerNotAvailableError,
)

if TYPE_CHECKING:
    from .typing import (
        ServerName,
        MiracleTicketEnchangeInfo,
        MiracleTicketEnchangesAll5,
    )

API = get_api('bestdori.api')

# 获取总自选券信息
def get_all(index: Literal[5]=5, *, me: Optional[Me] = None) -> 'MiracleTicketEnchangesAll5':
    '''获取总自选券信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`

    返回:
        MiracleTicketEnchangesAll5: 所有已有自选券信息 `all.5.json`
    '''
    return Api(
        API['all']['miracleTicketExchanges'].format(index=index)
    ).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取总自选券信息
async def get_all_async(index: Literal[5]=5, *, me: Optional[Me] = None) -> 'MiracleTicketEnchangesAll5':
    '''获取总自选券信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`

    返回:
        MiracleTicketEnchangesAll5: 所有已有自选券信息 `all.5.json`
    '''
    return (await Api(
        API['all']['miracleTicketExchanges'].format(index=index)
    ).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 自选券类
class MiracleTicketExchange:
    '''自选券类

    参数:
        id (int): 自选券 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''自选券类

        参数:
            id (int): 自选券 ID
        '''
        self.id: int = id
        '''自选券 ID'''
        self.__info: Optional[MiracleTicketEnchangeInfo] = None
        '''自选券信息'''

        self.__me = me
        return
    
    @property
    def info(self) -> 'MiracleTicketEnchangeInfo':
        '''自选券信息'''
        if self.__info is None:
            raise RuntimeError(f'Miracle ticket \'{self.id}\' info were not retrieved.')
        return self.__info
    
    # 自选券标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''自选券标题'''
        return self.info['name']
    
    # 提取自选券默认服务器
    @property
    def __server__(self) -> 'ServerName':
        '''提取自选券默认服务器'''
        # 获取 ids 数据
        ids = self.info['ids']
        # 根据 ids 数据判断服务器
        if ids[0] is not None: return 'jp'
        elif ids[1] is not None: return 'en'
        elif ids[2] is not None: return 'tw'
        elif ids[3] is not None: return 'cn'
        elif ids[4] is not None: return 'kr'
        else:
            raise NoDataException('miracle ticket server')
    
    # 获取自选券信息
    def get_info(self) -> 'MiracleTicketEnchangeInfo':
        '''获取自选券信息

        返回:
            MiracleTicketEnchangeInfo: 自选券详细信息
        '''
        _all = get_all(5, me=self.__me)
        if not self.id in _all.keys():
            raise NotExistException(f'Miracle ticket {self.id}')
        self.__info = _all[str(self.id)]
        return self.info
    
    def __get_info__(self) -> 'MiracleTicketEnchangeInfo':
        if self.__info is None:
            return self.get_info()
        return self.info
    
    # 异步获取自选券信息
    async def get_info_async(self) -> 'MiracleTicketEnchangeInfo':
        '''获取自选券信息

        返回:
            MiracleTicketEnchangeInfo: 自选券详细信息
        '''
        _all = await get_all_async(5, me=self.__me)
        if not self.id in _all.keys():
            raise NotExistException(f'Miracle ticket {self.id}')
        self.__info = _all[str(self.id)]
        return self.info
    
    async def __get_info_async__(self) -> 'MiracleTicketEnchangeInfo':
        if self.__info is None:
            return await self.get_info_async()
        return self.info
    
    # 获取自选券 ID 列表
    def get_ids(self, server: 'ServerName') -> List[int]:
        '''获取自选券 ID 列表

        参数:
            server (ServerName): 指定服务器

        返回:
            List[int]: 自选券 ID 列表
        '''
        info = self.__get_info__()
        # 获取 ids 数据
        ids = info['ids']
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        id_list = ids[index]
        if id_list is None:
            raise ServerNotAvailableError(f'Miracle ticket {name(self)}', server)
        return id_list
    
    # 异步获取自选券 ID 列表
    async def get_ids_async(self, server: 'ServerName') -> List[int]:
        '''获取自选券 ID 列表

        参数:
            server (ServerName): 指定服务器

        返回:
            List[int]: 自选券 ID 列表
        '''
        info = await self.__get_info_async__()
        # 获取 ids 数据
        ids = info['ids']
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        id_list = ids[index]
        if id_list is None:
            raise ServerNotAvailableError(f'Miracle ticket {name(self)}', server)
        return id_list
