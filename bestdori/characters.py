'''`bestdori.characters`

BanG Dream! 角色相关操作'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Tuple, Union, Literal, Optional

from . import post
from .user import Me
from .utils.network import Api
from .utils import get_api, hex_to_rgb
from .exceptions import (
    HTTPStatusError,
    NoDataException,
    NotExistException,
)

if TYPE_CHECKING:
    from .typing import (
        NoneDict,
        PostList,
        CharacterAll2,
        CharacterAll5,
        CharacterInfo,
        CharacterMain1,
        CharacterMain2,
        CharacterMain3,
    )

API = get_api('bestdori.api')
RES = get_api('bestdori.res')
ASSETS = get_api('bestdori.assets')

# 获取总角色信息
@overload
def get_all(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总角色信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有角色 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[2], *, me: Optional[Me] = None) -> 'CharacterAll2':
    '''获取总角色信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CharacterAll2: 所有已有角色的简洁信息 `all.2.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'CharacterAll5':
    '''获取总角色信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        CharacterAll5: 所有已有角色的较详细信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[0, 2, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'CharacterAll2', 'CharacterAll5']:
    return Api(API['characters']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取总角色信息
@overload
async def get_all_async(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总角色信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有角色 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[2], *, me: Optional[Me] = None) -> 'CharacterAll2':
    '''获取总角色信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CharacterAll2: 所有已有角色的简洁信息 `all.2.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'CharacterAll5':
    '''获取总角色信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        CharacterAll5: 所有已有角色的较详细信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[0, 2, 3, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'CharacterAll2', 'CharacterAll5']:
    return (await Api(API['characters']['all'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 获取主要角色信息
@overload
def get_main(index: Literal[1], *, me: Optional[Me] = None) -> 'CharacterMain1':
    '''获取主要角色信息

    参数:
        index (Literal[1]): 指定获取哪种 `main.json`

    返回:
        CharacterMain1: 所有已有主要角色 ID 与其乐队 ID `main.1.json`
    '''
    ...
@overload
def get_main(index: Literal[2], *, me: Optional[Me] = None) -> 'CharacterMain2':
    '''获取主要角色信息

    参数:
        index (Literal[2]): 指定获取哪种 `main.json`

    返回:
        CharacterMain2: 所有已有主要角色的简洁信息 `main.2.json`
    '''
    ...
@overload
def get_main(index: Literal[3], *, me: Optional[Me] = None) -> 'CharacterMain3':
    '''获取主要角色信息

    参数:
        index (Literal[5]): 指定获取哪种 `main.json`

    返回:
        CharacterMain3: 所有已有主要角色的较详细信息 `main.3.json`
    '''
    ...

def get_main(index: Literal[1, 2, 3]=3, *, me: Optional[Me] = None) -> Union['CharacterMain1', 'CharacterMain2', 'CharacterMain3']:
    return Api(API['characters']['main'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取主要角色信息
@overload
async def get_main_async(index: Literal[1], *, me: Optional[Me] = None) -> 'CharacterMain1':
    '''获取主要角色信息

    参数:
        index (Literal[1]): 指定获取哪种 `main.json`

    返回:
        CharacterMain1: 所有已有主要角色 ID 与其乐队 ID `main.1.json`
    '''
    ...
@overload
async def get_main_async(index: Literal[2], *, me: Optional[Me] = None) -> 'CharacterMain2':
    '''获取主要角色信息

    参数:
        index (Literal[2]): 指定获取哪种 `main.json`

    返回:
        CharacterMain2: 所有已有主要角色的简洁信息 `main.2.json`
    '''
    ...
@overload
async def get_main_async(index: Literal[3], *, me: Optional[Me] = None) -> 'CharacterMain3':
    '''获取主要角色信息

    参数:
        index (Literal[5]): 指定获取哪种 `main.json`

    返回:
        CharacterMain3: 所有已有主要角色的较详细信息 `main.3.json`
    '''
    ...

async def get_main_async(index: Literal[1, 2, 3]=3, *, me: Optional[Me] = None) -> Union['CharacterMain1', 'CharacterMain2', 'CharacterMain3']:
    return (await Api(API['characters']['main'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 角色类
class Character:
    '''角色类

    参数:
        id (int): 角色 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''角色类

        参数:
            id (int): 角色 ID
        '''
        self.id: int = id
        '''角色 ID'''
        self.__info: Optional['CharacterInfo'] = None
        '''角色信息'''
        
        self.__me: Optional[Me] = me
        return
    
    @property
    def info(self) -> 'CharacterInfo':
        '''角色信息'''
        if self.__info is None:
            raise ValueError(f'Character \'{self.id}\' info were not retrieved.')
        return self.__info

    # 角色名称
    @property
    def __name__(self) -> List[Optional[str]]:
        '''角色名称'''
        return self.info['characterName']
    
    # 角色代表色
    @property
    def __color__(self) -> Tuple[int, int, int]:
        '''角色代表色'''
        # 获取 colorCode 数据
        if (color_code := self.info.get('colorCode', None)) is None:
            raise NoDataException('character color code')
        # 将 colorCode 转换为颜色元组
        try:
            return hex_to_rgb(color_code)
        except ValueError:
            raise NoDataException('character color code')
    
    # 获取角色信息
    def get_info(self) -> 'CharacterInfo':
        '''获取角色

        返回:
            CharacterInfo: 角色信息
        '''
        try:
            response = Api(
                API['characters']['info'].format(id=self.id)
            ).get(cookies=self.__me.__get_cookies__() if self.__me else None)
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Character {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return response.json()
    
    # 异步获取角色信息
    async def get_info_async(self) -> 'CharacterInfo':
        '''获取角色

        返回:
            CharacterInfo: 角色信息
        '''
        try:
            response = await Api(
                API['characters']['info'].format(id=self.id)
            ).aget(cookies=await self.__me.__get_cookies_async__() if self.__me else None)
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Character {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return response.json()
    
    # 获取角色评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取角色评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            PostList: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[PostListPost] 列举出的评论
                }
                ```
        '''
        return post.get_list(
            category_name='CHARACTER_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 异步获取角色评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取角色评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            PostList: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[PostListPost] 列举出的评论
                }
                ```
        '''
        return await post.get_list_async(
            category_name='CHARACTER_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 获取角色图标
    def get_icon(self) -> bytes:
        '''获取角色图标

        返回:
            bytes: 角色图标字节数据 `bytes`
        '''
        return Api(RES['icon']['png'].format(name=f'chara_icon_{self.id}')).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
        ).content
    
    # 异步获取角色图标
    async def get_icon_async(self) -> bytes:
        '''获取角色图标

        返回:
            bytes: 角色图标字节数据 `bytes`
        '''
        return (await Api(RES['icon']['png'].format(name=f'chara_icon_{self.id}')).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None,
        )).content
    
    # 获取角色主视觉图
    def get_kv_image(self) -> bytes:
        '''获取角色主视觉图

        返回:
            bytes: 主视觉图资源字节 `bytes`
        '''
        return Api(
            ASSETS['characters']['character_kv_image'].format(server='jp', id=self.id)
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
        ).content
    
    # 异步获取角色主视觉图
    async def get_kv_image_async(self) -> bytes:
        '''获取角色主视觉图

        返回:
            bytes: 主视觉图资源字节 `bytes`
        '''
        return (await Api(
            ASSETS['characters']['character_kv_image'].format(server='jp', id=self.id)
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None,
        )).content
