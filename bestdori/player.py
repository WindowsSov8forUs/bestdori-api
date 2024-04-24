'''`bestdori.player`

BanG Dream! 玩家信息相关操作'''

from typing import Any, Optional

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
        self._info: Optional[dict[str, Any]] = None
    
    def get(self) -> dict[str, Any]:
        '''获取玩家信息

        返回:
            dict[str, Any]: 玩家信息
        '''
        if self._info is None:
            params = {
                'mode': 2
            }
            _info = Api(
                API['player']['info'].format(server=self.server, id=self.id)
            ).request('get', params=params).json()
            if not _info.get('result', False):
                raise ValueError(f'Invalid Server: {self.server}')
            _data: dict[str, Any] = _info.get('data', {})
            _profile: Optional[dict[str, Any]] = _data.get('profile', None)
            if _profile is None:
                raise PlayerNotExistError(self.server, self.id)
            self._info = _profile
        
        return self._info
