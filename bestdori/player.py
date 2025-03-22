'''`bestdori.player`

BanG Dream! 玩家信息相关操作'''

from typing import TYPE_CHECKING, Literal, Optional

from .user import Me
from .utils import get_api
from .utils.network import Api
from .exceptions import PlayerNotExistError

if TYPE_CHECKING:
    from .typing import (
        PlayerData,
        PlayerInfo,
        PlayerDataProfile,
    )

API = get_api('bestdori.api')

class Player:
    '''玩家类

    参数:
        id (int): 玩家 ID
        server (str): 服务器
    '''
    def __init__(self, id: int, server: str, *, me: Optional[Me] = None) -> None:
        self.id: int = id
        self.server: str = server
        self.__profile: Optional[PlayerDataProfile] = None

        self.__me = me
    
    @property
    def profile(self) -> 'PlayerDataProfile':
        if self.__profile is None:
            raise RuntimeError(f'Player {self.id}\'s profile in server \'{self.server}\' were not retrieved.')
        return self.__profile
    
    def get_profile(self, mode: Literal[0, 1, 2, 3] = 2) -> 'PlayerDataProfile':
        '''获取玩家信息
        
        参数:
            mode (Literal[0, 1, 2, 3]):\
                0: 立即返回缓存数据,\
                1: 立即返回缓存数据，同时请求数据更新,\
                2: 请求并等待数据更新并返回更新后数据，若耗时过长则返回缓存数据,\
                3: 请求并持续等待数据更新，返回更新后数据

        返回:
            PlayerDataProfile: 玩家信息
        '''
        params = {
            'mode': mode
        }
        info: 'PlayerInfo' = Api(
            API['player']['info'].format(server=self.server, id=self.id)
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
            params=params,
        ).json()
        if not info['result']:
            raise ValueError(f'Invalid Server: {self.server}')
        data: 'PlayerData' = info['data']
        profile: Optional['PlayerDataProfile'] = data['profile']
        if profile is None:
            raise PlayerNotExistError(self.server, self.id)
        self.__profile = profile
        
        return self.profile
    
    async def get_profile_async(self, mode: Literal[0, 1, 2, 3] = 2) -> 'PlayerDataProfile':
        '''获取玩家信息
        
        参数:
            mode (Literal[0, 1, 2, 3]):\
                0: 立即返回缓存数据,\
                1: 立即返回缓存数据，同时请求数据更新,\
                2: 请求并等待数据更新并返回更新后数据，若耗时过长则返回缓存数据,\
                3: 请求并持续等待数据更新，返回更新后数据

        返回:
            PlayerDataProfile: 玩家信息
        '''
        params = {
            'mode': mode
        }
        info: 'PlayerInfo' = (await Api(
            API['player']['info'].format(server=self.server, id=self.id)
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None,
            params=params,
        )).json()
        if not info['result']:
            raise ValueError(f'Invalid Server: {self.server}')
        data: 'PlayerData' = info['data']
        profile: Optional['PlayerDataProfile'] = data['profile']
        if profile is None:
            raise PlayerNotExistError(self.server, self.id)
        self.__profile = profile

        return self.profile
