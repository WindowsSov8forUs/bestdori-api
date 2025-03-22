'''`bestdori.cards`

BanG Dream! 卡牌相关操作'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional

from .user import Me
from .utils import get_api
from .post import get_list, get_list_async
from .utils.network import Api
from .exceptions import (
    HTTPStatusError,
    NoDataException,
    NotExistException,
)

if TYPE_CHECKING:
    from .typing import (
        CardAll2,
        CardAll3,
        CardAll5,
        CardInfo,
        NoneDict,
        PostList,
        ServerName,
    )

API = get_api('bestdori.api')
RES = get_api('bestdori.res')
ASSETS = get_api('bestdori.assets')

# 获取总卡牌信息
@overload
def get_all(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总卡牌信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有卡牌 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[2], *, me: Optional[Me] = None) -> 'CardAll2':
    '''获取总卡牌信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CardAll2: 所有已有卡牌的属性信息 `all.2.json`
    '''
    ...
@overload
def get_all(index: Literal[3], *, me: Optional[Me] = None) -> 'CardAll3':
    '''获取总卡牌信息

    参数:
        index (Literal[3]): 指定获取哪种 `all.json`

    返回:
        CardAll3: 所有已有卡牌的简洁信息 `all.3.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'CardAll5':
    '''获取总卡牌信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        CardAll5: 所有已有卡牌的较详细信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[0, 2, 3, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'CardAll2', 'CardAll3', 'CardAll5']:
    return Api(API['cards']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).json()

# 异步获取总卡牌信息
@overload
async def get_all_async(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总卡牌信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有卡牌 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[2], *, me: Optional[Me] = None) -> 'CardAll2':
    '''获取总卡牌信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CardAll2: 所有已有卡牌的属性信息 `all.2.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[3], *, me: Optional[Me] = None) -> 'CardAll3':
    '''获取总卡牌信息

    参数:
        index (Literal[3]): 指定获取哪种 `all.json`

    返回:
        CardAll3: 所有已有卡牌的简洁信息 `all.3.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'CardAll5':
    '''获取总卡牌信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`

    返回:
        CardAll5: 所有已有卡牌的较详细信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[0, 2, 3, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'CardAll2', 'CardAll3', 'CardAll5']:
    return (await Api(API['cards']['all'].format(index=index)).aget(
        cookies=(await me.__get_cookies_async__()) if me is not None else None,
    )).json()

# 获取属性图标
def get_attribute_icon(attribute: Literal['powerful', 'pure', 'cool', 'happy'], *, me: Optional[Me] = None) -> bytes:
    '''获取属性图标

    参数:
        attribute (Literal[&#39;powerful&#39;, &#39;pure&#39;, &#39;cool&#39;, &#39;happy&#39;]): 属性名称
            `powerful`: POWERFUL
            `pure`: PURE
            `cool`: COOL
            `happy`: HAPPY

    返回:
        bytes: 属性图标字节数据
    '''
    return Api(RES['icon']['svg'].format(name=f'{attribute}')).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).content

# 异步获取属性图标
async def get_attribute_icon_async(attribute: Literal['powerful', 'pure', 'cool', 'happy'], *, me: Optional[Me] = None) -> bytes:
    '''获取属性图标

    参数:
        attribute (Literal[&#39;powerful&#39;, &#39;pure&#39;, &#39;cool&#39;, &#39;happy&#39;]): 属性名称
            `powerful`: POWERFUL
            `pure`: PURE
            `cool`: COOL
            `happy`: HAPPY

    返回:
        bytes: 属性图标字节数据
    '''
    return (await Api(RES['icon']['svg'].format(name=f'{attribute}')).aget(
        cookies=(await me.__get_cookies_async__()) if me is not None else None,
    )).content

# 获取星星图标
def get_star_icon(star: Literal['star', 'star_trained'], *, me: Optional[Me] = None) -> bytes:
    '''获取星星图标

    参数:
        star (Literal[&#39;star&#39;, &#39;star_trained&#39;]): 星标种类
            `star`: 普通星标
            `star_trained`: 训练后星标

    返回:
        bytes: 星星图标字节数据
    '''
    return Api(RES['icon']['png'].format(name=f'{star}')).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).content

# 异步获取星星图标
async def get_star_icon_async(star: Literal['star', 'star_trained'], *, me: Optional[Me] = None) -> bytes:
    '''获取星星图标

    参数:
        star (Literal[&#39;star&#39;, &#39;star_trained&#39;]): 星标种类
            `star`: 普通星标
            `star_trained`: 训练后星标

    返回:
        bytes: 星星图标字节数据
    '''
    return (await Api(RES['icon']['png'].format(name=f'{star}')).aget(
        cookies=(await me.__get_cookies_async__()) if me is not None else None,
    )).content

# 获取卡牌完整边框
def get_frame(level: Literal[1, 2, 3, 4, 5], *, me: Optional[Me] = None) -> bytes:
    '''获取卡牌完整边框

    参数:
        level (Literal[1, 2, 3, 4, 5]): 边框星级

    返回:
        bytes: 卡牌完整边框字节数据
    '''
    return Api(RES['image']['png'].format(name=f'frame-{level}')).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).content

# 异步获取卡牌完整边框
async def get_frame_async(level: Literal[1, 2, 3, 4, 5], *, me: Optional[Me] = None) -> bytes:
    '''获取卡牌完整边框

    参数:
        level (Literal[1, 2, 3, 4, 5]): 边框星级

    返回:
        bytes: 卡牌完整边框字节数据
    '''
    return (await Api(RES['image']['png'].format(name=f'frame-{level}')).aget(
        cookies=(await me.__get_cookies_async__()) if me is not None else None,
    )).content

# 获取卡牌缩略图边框
def get_card_frame(level: Literal[1, 2, 3, 4, 5], *, me: Optional[Me] = None) -> bytes:
    '''获取卡牌缩略图边框

    参数:
        level (Literal[1, 2, 3, 4, 5]): 边框星级

    返回:
        bytes: 卡牌缩略图边框字节数据
    '''
    return Api(RES['image']['png'].format(name=f'card-{level}')).get(
        cookies=me.__get_cookies__() if me is not None else None,
    ).content

# 异步获取卡牌缩略图边框
async def get_card_frame_async(level: Literal[1, 2, 3, 4, 5], *, me: Optional[Me] = None) -> bytes:
    '''获取卡牌缩略图边框

    参数:
        level (Literal[1, 2, 3, 4, 5]): 边框星级

    返回:
        bytes: 卡牌缩略图边框字节数据
    '''
    return (await Api(RES['image']['png'].format(name=f'card-{level}')).aget(
        cookies=(await me.__get_cookies_async__()) if me is not None else None,
    )).content

# 卡牌类
class Card:
    '''卡牌类

    参数:
        id (int): 卡牌 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        self.id: int = id
        '''卡牌 ID'''
        self.__info: Optional['CardInfo'] = None
        '''卡牌信息'''
        
        self.__me: Optional[Me] = me
        return
    
    @property
    def info(self) -> 'CardInfo':
        '''卡牌信息'''
        if self.__info is None:
            raise ValueError(f'Card \'{self.id}\' info were not retrieved.')
        return self.__info

    # 获取卡牌信息
    def get_info(self) -> 'CardInfo':
        '''获取卡牌信息

        返回:
            CardInfo: 卡牌信息
        '''
        try:
            response = Api(
                API['cards']['info'].format(id=self.id)
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me is not None else None,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Card {self.id}')
            else:
                raise exception
        self.__info = response.json()
        return response.json()
    
    def __get_info__(self) -> 'CardInfo':
        if self.__info is None:
            self.__info = self.get_info()
        return self.__info
    
    # 异步获取卡牌信息
    async def get_info_async(self) -> 'CardInfo':
        '''获取卡牌信息

        返回:
            CardInfo: 卡牌信息
        '''
        try:
            response = await Api(
                API['cards']['info'].format(id=self.id)
            ).aget(
                cookies=(await self.__me.__get_cookies_async__()) if self.__me is not None else None,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Card {self.id}')
            else:
                raise exception
        self.__info = response.json()
        return response.json()
    
    async def __get_info_async__(self) -> 'CardInfo':
        if self.__info is None:
            self.__info = await self.get_info_async()
        return self.__info
    
    # 提取卡牌标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''提取卡牌标题'''
        return self.info['prefix']
    
    # 提取卡牌所在默认服务器
    @property
    def __server__(self) -> 'ServerName':
        '''提取卡牌所在默认服务器'''
        # 获取 releasedAt 数据
        released_at = self.info['releasedAt']
        # 根据 releasedAt 数据判断服务器
        if released_at[0] is not None: return 'jp'
        elif released_at[1] is not None: return 'en'
        elif released_at[2] is not None: return 'tw'
        elif released_at[3] is not None: return 'cn'
        elif released_at[4] is not None: return 'kr'
        else:
            raise NoDataException('card server')
    
    # 获取卡牌评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取卡牌评论

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
        return get_list(
            category_name='CARD_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 异步获取卡牌评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取卡牌评论

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
        return await get_list_async(
            category_name='CARD_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 获取卡牌完整图片
    def get_card(self, type: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌完整图片

        参数:
            type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌完整图片字节数据 `bytes`
        '''
        info = self.__get_info__()
        return Api(
            ASSETS['characters']['resourceset'].format(
                server=self.__server__,
                resource_set_name=info['resourceSetName'],
                name='card',
                type=type,
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me is not None else None,
        ).content
    
    # 异步获取卡牌完整图片
    async def get_card_async(self, type: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌完整图片

        参数:
            type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌完整图片字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取卡牌数据包名称
        return (await Api(
            ASSETS['characters']['resourceset'].format(
                server=self.__server__,
                resource_set_name=info['resourceSetName'],
                name='card',
                type=type,
            )
        ).aget(
            cookies=(await self.__me.__get_cookies_async__()) if self.__me is not None else None,
        )).content
    
    # 获取卡牌无背景图片
    def get_trim(self, type: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌无背景图片

        参数:
            type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌无背景图片字节数据 `bytes`
        '''
        info = self.__get_info__()
        return Api(
            ASSETS['characters']['resourceset'].format(
                server=self.__server__,
                resource_set_name=info['resourceSetName'],
                name='trim',
                type=type,
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me is not None else None,
        ).content
    
    # 异步获取卡牌无背景图片
    async def get_trim_async(self, type: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌无背景图片

        参数:
            type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌无背景图片字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        return (await Api(
            ASSETS['characters']['resourceset'].format(
                server=self.__server__,
                resource_set_name=info['resourceSetName'],
                name='trim',
                type=type,
            )
        ).aget(
            cookies=(await self.__me.__get_cookies_async__()) if self.__me is not None else None,
        )).content
    
    # 获取卡牌缩略图图片
    def get_thumb(self, type: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌缩略图图片

        参数:
            type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌缩略图图片字节数据 `bytes`
        '''
        info = self.__get_info__()
        return Api(
            ASSETS['thumb']['chara'].format(
                server=self.__server__,
                id=self.id // 50,
                resource_set_name=info['resourceSetName'],
                type=type,
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self .__me is not None else None,
        ).content
    
    # 异步获取卡牌缩略图图片
    async def get_thumb_async(self, type: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌缩略图图片

        参数:
            type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌缩略图图片字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        return (await Api(
            ASSETS['thumb']['chara'].format(
                server=self.__server__,
                id=self.id // 50,
                resource_set_name=info['resourceSetName'],
                type=type,
            )
        ).aget(
            cookies=(await self.__me.__get_cookies_async__()) if self.__me is not None else None,
        )).content
    
    # 获取 LIVE 服装图片
    def get_livesd(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 卡牌 LIVE 服装图片字节数据 `bytes`
        '''
        info = self.__get_info__()
        return Api(
            ASSETS['characters']['livesd'].format(
                server=self.__server__,
                sd_resource_name=info['sdResourceName'],
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me is not None else None,
        ).content
    
    # 异步获取 LIVE 服装图片
    async def get_livesd_async(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 卡牌 LIVE 服装图片字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        return (await Api(
            ASSETS['characters']['livesd'].format(
                server=self.__server__,
                sd_resource_name=info['sdResourceName'],
            )
        ).aget(
            cookies=(await self.__me.__get_cookies_async__()) if self.__me is not None else None,
        )).content