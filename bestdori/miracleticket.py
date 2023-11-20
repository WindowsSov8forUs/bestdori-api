'''`bestdori.miracleticket`

BanG Dream! 自选券相关操作'''
from typing import Optional, Literal, Any

from .utils.utils import API
from .utils.network import Api
from .exceptions import (
    MiracleTicketExchangeNotExistError,
    ServerNotAvailableError
)

# 获取总自选券信息
def get_all(index: Literal[5]=5, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总自选券信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`
            `5`: 获取所有已有自选券信息 `all.5.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总自选券信息
    '''
    return Api(
        API['all']['miracleTicketExchanges'].format(index), proxy=proxy
    ).request('get').json()

# 自选券类
class MiracleTicketExchange:
    '''自选券类

    参数:
        id_ (int): 自选券 ID
        
        proxy (Optional[str], optional): 代理服务器
    '''
    # 初始化
    def __init__(self, id_: int, proxy: Optional[str]=None) -> None:
        '''自选券类

        参数:
            id_ (int): 自选券 ID
            
            proxy (Optional[str], optional): 代理服务器
        '''
        self.id: int = id_
        '''自选券 ID'''
        self._info: dict[str, Any] = {}
        '''自选券信息'''
        self.proxy: Optional[str] = proxy
        '''代理服务器'''
        # 检测 ID 是否存在
        all_ = get_all(5, proxy=proxy)
        if not str(id_) in all_.keys():
            raise MiracleTicketExchangeNotExistError(id_)
        self._info = all_[str(id_)]
        return
    
    # 获取自选券信息
    def get_info(self) -> dict[str, Any]:
        '''获取自选券信息

        返回:
            dict[str, Any]: 自选券详细信息
        '''
        return self._info
    
    # 获取自选券标题
    @property
    def name(self) -> str:
        '''获取自选券标题

        返回:
            str: 自选券标题
        '''
        info = self.get_info()
        # 获取 eventName 数据
        if (name := info.get('name', None)) is None:
            raise Exception('无法获取自选券标题。')
        # 获取第一个非 None 自选券标题
        try:
            return next(filter(lambda x: x is not None, name))
        except StopIteration:
            raise Exception('无法获取自选券标题。')
    
    # 获取自选券默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取自选券默认服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.get_info()
        # 获取 ids 数据
        if (ids := info.get('ids', None)) is None:
            raise Exception('无法获取自选券 ID 列表。')
        # 根据 ids 数据判断服务器
        if ids[0] is not None: return 'jp'
        elif ids[1] is not None: return 'en'
        elif ids[2] is not None: return 'tw'
        elif ids[3] is not None: return 'cn'
        elif ids[4] is not None: return 'kr'
        else:
            raise Exception('无法获取自选券所在服务器。')
    
    # 获取自选券 ID 列表
    def get_ids(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> list[int]:
        '''获取自选券 ID 列表

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            list[int]: 自选券 ID 列表
        '''
        info = self.get_info()
        # 获取 ids 数据
        if (ids := info.get('ids', None)) is None:
            raise Exception('无法获取自选券 ID 列表。')
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if ids[index] is None:
            raise ServerNotAvailableError(f'活动 {self.name}', server)
        return ids[index]
