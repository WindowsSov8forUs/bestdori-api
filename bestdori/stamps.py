'''`bestdori.stamps`

BanG Dream! 贴纸资源相关操作'''
from typing import TYPE_CHECKING, Literal, Optional

from .utils import get_api
from .utils.network import Api
from .exceptions import AssetsNotExistError

if TYPE_CHECKING:
    from .typing import (
        StampInfo,
        ServerName,
        StampsAll2,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总贴纸资源信息
def get_all(index: Literal[2]=2) -> 'StampsAll2':
    '''获取总活动信息

    参数:
        index (Literal[2], optional): 指定获取哪种 `all.json`
            `2`: 获取所有已有贴纸信息 `all.2.json`
        me (Optional[Me], optional): 用户验证信息

    返回:
        StampsAll2: 获取到的总贴纸信息
    '''
    return Api(API['all']['stamps'].format(index=index)).get().json()

# 异步获取总贴纸资源信息
async def get_all_async(index: Literal[2]=2) -> 'StampsAll2':
    '''获取总活动信息

    参数:
        index (Literal[2], optional): 指定获取哪种 `all.json`
            `2`: 获取所有已有贴纸信息 `all.2.json`
        me (Optional[Me], optional): 用户验证信息

    返回:
        StampsAll2: 获取到的总贴纸信息
    '''
    return (await Api(API['all']['stamps'].format(index=index)).aget()).json()

# 贴纸类
class Stamp:
    '''贴纸类

    参数:
        id (int): 贴纸 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''贴纸类

        参数:
            id (int): 贴纸 ID
        '''
        self.id: int = id
        '''贴纸 ID'''
        self.__info: Optional['StampInfo'] = None
        '''贴纸资源信息'''
        
    
    # 获取贴纸资源信息
    def get_info(self) -> 'StampInfo':
        '''获取贴纸资源信息

        返回:
            StampInfo: 贴纸资源信息
        '''
        _all = get_all()
        if str(self.id) not in _all:
            raise AssetsNotExistError(f'stamp {self.id}')
        self.__info = _all[str(self.id)]
        return self.__info
    
    def __get_info__(self) -> 'StampInfo':
        if not self.__info:
            return self.get_info()
        return self.__info

    # 异步获取贴纸资源信息
    async def get_info_async(self) -> 'StampInfo':
        '''获取贴纸资源信息

        返回:
            StampInfo: 贴纸资源信息
        '''
        _all = await get_all_async()
        if str(self.id) not in _all:
            raise AssetsNotExistError(f'stamp {self.id}')
        self.__info = _all[str(self.id)]
        return self.__info
    
    async def __get_info_async__(self) -> 'StampInfo':
        if not self.__info:
            return await self.get_info_async()
        return self.__info

    # 获取贴纸资源
    def get_stamp(
        self,
        server: 'ServerName',
    ) -> bytes:
        '''获取贴纸资源

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 贴纸资源
        '''
        info = self.__get_info__()
        return Api(
            ASSETS['stamp']['get'].format(server=server, image_name=info['imageName'])
        ).get().content
    
    # 异步获取贴纸资源
    async def get_stamp_async(
        self,
        server: 'ServerName',
    ) -> bytes:
        '''获取贴纸资源

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 贴纸资源
        '''
        info = await self.__get_info_async__()
        return (await Api(
            ASSETS['stamp']['get'].format(server=server, image_name=info['imageName'])
        ).aget()).content
