'''`bestdori.player`

BanG Dream! 玩家信息相关操作'''

from typing import Any, Dict, Literal, Optional

from httpx import Response

from .utils.utils import API
from .utils.network import Api
from .exceptions import PlayerNotExistError

class Player:
    '''玩家类

    参数:
        id (int): 玩家 ID
        server (str): 服务器
    '''
    def __init__(self, id: int, server: str) -> None:
        self.id: int = id
        self.server: str = server
        self.__info: Optional[Dict[str, Any]] = None
    
    def get_info(self, mode: Literal[0, 1, 2, 3] = 2) -> Dict[str, Any]:
        '''获取玩家信息
        
        参数:
            mode (Literal[0, 1, 2, 3]):\
                0: 立即返回缓存数据,\
                1: 立即返回缓存数据，同时请求数据更新,\
                2: 请求并等待数据更新并返回更新后数据，若耗时过长则返回缓存数据,\
                3: 请求并持续等待数据更新，返回更新后数据

        返回:
            Dict[str, Any]: 玩家信息
        '''
        params = {
            'mode': mode
        }
        _info = Api(
            API['player']['info'].format(server=self.server, id=self.id)
        ).get(params=params).json()
        if not _info.get('result', False):
            raise ValueError(f'Invalid Server: {self.server}')
        _data: Dict[str, Any] = _info.get('data', {})
        _profile: Optional[Dict[str, Any]] = _data.get('profile', None)
        if _profile is None:
            raise PlayerNotExistError(self.server, self.id)
        self.__info = _profile
        
        return self.__info
    
    async def get_info_async(self, mode: Literal[0, 1, 2, 3] = 2) -> Dict[str, Any]:
        '''获取玩家信息
        
        参数:
            mode (Literal[0, 1, 2, 3]):\
                0: 立即返回缓存数据,\
                1: 立即返回缓存数据，同时请求数据更新,\
                2: 请求并等待数据更新并返回更新后数据，若耗时过长则返回缓存数据,\
                3: 请求并持续等待数据更新，返回更新后数据

        返回:
            Dict[str, Any]: 玩家信息
        '''
        params = {
            'mode': mode
        }
        response = await Api(
            API['player']['info'].format(server=self.server, id=self.id)
        ).aget(params=params)
        
        if isinstance(response, Response):
            _info = response.json()
        else:
            _info = await response.json()
        
        if not _info.get('result', False):
            raise ValueError(f'Invalid Server: {self.server}')
        _data: Dict[str, Any] = _info.get('data', {})
        _profile: Optional[Dict[str, Any]] = _data.get('profile', None)
        if _profile is None:
            raise PlayerNotExistError(self.server, self.id)
        self.__info = _profile
        
        return self.__info
