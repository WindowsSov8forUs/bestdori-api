'''`bestdori.characters`

BanG Dream! 角色相关操作'''
from typing import Any, Literal

from aiohttp import ClientResponseError
from httpx import Response, HTTPStatusError

from .utils import hexto_rgb
from .utils.utils import API, RES, ASSETS
from .post import get_list, get_list_async
from .utils.network import Api, Res, Assets
from .exceptions import (
    NoDataException,
    CharacterNotExistError
)

# 获取总角色信息
def get_all(index: Literal[2]=2) -> dict[str, dict[str, Any]]:
    '''获取总角色信息

    参数:
        index (Literal[2], optional): 指定获取哪种 `all.json`
            `2`: 获取所有已有角色信息 `all.2.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总角色信息
    '''
    return Api(API['characters']['all'].format(index=index)).get().json()

# 异步获取总角色信息
async def get_all_async(index: Literal[2]=2) -> dict[str, dict[str, Any]]:
    '''获取总角色信息

    参数:
        index (Literal[2], optional): 指定获取哪种 `all.json`
            `2`: 获取所有已有角色信息 `all.2.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总角色信息
    '''
    response = await Api(API['characters']['all'].format(index=index)).aget()
    if isinstance(response, Response):
        return response.json()
    else:
        return await response.json()
    

# 获取主要角色信息
def get_main(index: Literal[3]=3) -> dict[str, dict[str, Any]]:
    '''获取主要角色信息

    参数:
        index (Literal[3], optional): 指定获取哪种 `all.json`
            `3`: 获取所有已有主要角色信息 `all.3.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的主要角色信息
    '''
    return Api(API['characters']['main'].format(index=index)).get().json()

# 异步获取主要角色信息
async def get_main_async(index: Literal[3]=3) -> dict[str, dict[str, Any]]:
    '''获取主要角色信息

    参数:
        index (Literal[3], optional): 指定获取哪种 `all.json`
            `3`: 获取所有已有主要角色信息 `all.3.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的主要角色信息
    '''
    response = await Api(API['characters']['main'].format(index=index)).aget()
    if isinstance(response, Response):
        return response.json()
    else:
        return await response.json()

# 角色类
class Character:
    '''角色类

    参数:
        id (int): 角色 ID
    '''
    # 初始化
    def __init__(self, id: int) -> None:
        '''角色类

        参数:
            id (int): 角色 ID
        '''
        self.id: int = id
        '''角色 ID'''
        self.__info: dict[str, Any] = {}
        '''角色信息'''
        return
    
    # 角色名称
    @property
    def name(self) -> str:
        '''角色名称'''
        info = self.__info
        # 获取 characterName 数据
        if (character_name := info.get('characterName', None)) is None:
            raise NoDataException('角色名称')
        # 获取第一个非 None 角色名称
        try:
            return next(filter(lambda x: x is not None, character_name))
        except StopIteration:
            raise NoDataException('角色名称')
    
    # 角色代表色
    @property
    def color(self) -> tuple[int, int, int]:
        '''角色代表色'''
        info = self.__info
        # 获取 colorCode 数据
        if (color_code := info.get('colorCode', None)) is None:
            raise NoDataException('角色颜色')
        # 将 colorCode 转换为颜色元组
        try:
            return hexto_rgb(color_code)
        except ValueError:
            raise NoDataException('角色颜色')
    
    # 获取角色信息
    def get_info(self) -> dict[str, Any]:
        '''获取角色信息

        返回:
            dict[str, Any]: 角色详细信息
        '''
        try:
            response = Api(
                API['characters']['info'].format(id=self.id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise CharacterNotExistError(self.id)
            else:
                raise exception
        
        self.__info = dict(response.json())
        return self.__info
    
    # 异步获取角色信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取角色信息

        返回:
            dict[str, Any]: 角色详细信息
        '''
        try:
            response = await Api(
                API['characters']['info'].format(id=self.id)
            ).aget()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise CharacterNotExistError(self.id)
            else:
                raise exception
        except ClientResponseError as exception:
            if exception.status == 404:
                raise CharacterNotExistError(self.id)
            else:
                raise exception
        
        if isinstance(response, Response):
            self.__info = dict(response.json())
        else:
            self.__info = dict(await response.json())
        return self.__info
    
    # 获取角色评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取角色评论

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
            category_name='CHARACTER_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取角色评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取角色评论

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
            category_name='CHARACTER_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取角色图标
    def get_icon(self) -> bytes:
        '''获取角色图标

        返回:
            bytes: 角色图标字节数据 `bytes`
        '''
        return Res(RES['icon']['png'].format(name=f'chara_icon_{self.id}')).get()
    
    # 异步获取角色图标
    async def get_icon_async(self) -> bytes:
        '''获取角色图标

        返回:
            bytes: 角色图标字节数据 `bytes`
        '''
        return await Res(RES['icon']['png'].format(name=f'chara_icon_{self.id}')).aget()
    
    # 获取角色主视觉图
    def get_kv_image(self) -> bytes:
        '''获取角色主视觉图

        返回:
            bytes: 主视觉图资源字节 `bytes`
        '''
        return Assets(
            ASSETS['characters']['character_kv_image'].format(id=self.id), 'jp'
        ).get()
    
    # 异步获取角色主视觉图
    async def get_kv_image_async(self) -> bytes:
        '''获取角色主视觉图

        返回:
            bytes: 主视觉图资源字节 `bytes`
        '''
        return await Assets(
            ASSETS['characters']['character_kv_image'].format(id=self.id), 'jp'
        ).aget()
