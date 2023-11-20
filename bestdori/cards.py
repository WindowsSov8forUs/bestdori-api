'''`bestdori.cards`

BanG Dream! 卡牌相关操作'''
from typing import Optional, Literal, Any

from .post import get_list
from .utils.utils import API, RES, ASSETS
from .utils.network import Api, Res, Assets
from .exceptions import (
    CardNotExistError
)

# 获取总卡牌信息
def get_all(index: Literal[0, 5]=5, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总卡牌信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有卡牌 ID `all.0.json`
            `5`: 获取所有已有卡牌的简洁信息 `all.5.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总卡牌信息
    '''
    return Api(API['cards']['all'].format(index), proxy=proxy).request('get').json()

# 获取属性图标
def get_attribute_icon(attribute: Literal['powerful', 'pure', 'cool', 'happy']) -> bytes:
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
    return Res(RES['icon']['svg'].format(name=f'{attribute}')).get()

# 获取星星图标
def get_star_icon(star: Literal['star', 'star_trained']) -> bytes:
    '''获取星星图标

    参数:
        star (Literal[&#39;star&#39;, &#39;star_trained&#39;]): 星标种类
            `star`: 普通星标
            `star_trained`: 训练后星标

    返回:
        bytes: 星星图标字节数据
    '''
    return Res(RES['icon']['png'].format(name=f'{star}')).get()

# 获取卡牌完整边框
def get_frame(level: Literal[1, 2, 3, 4, 5]) -> bytes:
    '''获取卡牌完整边框

    参数:
        level (Literal[1, 2, 3, 4, 5]): 边框星级

    返回:
        bytes: 卡牌完整边框字节数据
    '''
    return Res(RES['image']['png'].format(f'frame-{level}')).get()

# 获取卡牌缩略图边框
def get_card_frame(level: Literal[1, 2, 3, 4, 5]) -> bytes:
    '''获取卡牌缩略图边框

    参数:
        level (Literal[1, 2, 3, 4, 5]): 边框星级

    返回:
        bytes: 卡牌缩略图边框字节数据
    '''
    return Res(RES['image']['png'].format(f'card-{level}')).get()

# 卡牌类
class Card:
    '''卡牌类

    参数:
        id_ (int): 卡牌 ID
        
        proxy (Optional[str], optional): 代理服务器
    '''
    # 初始化
    def __init__(self, id_: int, proxy: Optional[str]=None) -> None:
        '''卡牌类

        参数:
            id_ (int): 卡牌 ID
            
            proxy (Optional[str], optional): 代理服务器
        '''
        self.id: int = id_
        '''卡牌 ID'''
        self._info: dict[str, Any] = {}
        '''卡牌信息'''
        self.proxy: Optional[str] = proxy
        '''代理服务器'''
        # 检测 ID 是否存在
        all_id = get_all(0, proxy=proxy)
        if not str(id_) in all_id.keys():
            raise CardNotExistError(id_)
        return
    
    # 获取卡牌信息
    def get_info(self) -> dict[str, Any]:
        '''获取卡牌信息

        返回:
            dict[str, Any]: 卡牌详细信息
        '''
        if len(self._info) <= 0:
            # 如果没有卡牌信息存储
            response = Api(
                API['cards']['info'].format(self.id), proxy=self.proxy
            ).request('get')
            self._info = dict(response.json())
        return self._info
    
    # 获取卡牌评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取卡牌评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            dict[str, Any]: 搜索结果
            ```python
            result: bool # 是否有响应
            count: int # 搜索到的评论总数
            posts: list[dict[str, Any]] # 列举出的评论
            ```
        '''
        return get_list(
            proxy=self.proxy,
            category_name='CARD_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取卡牌标题
    @property
    def prefix(self) -> str:
        '''获取卡牌标题

        返回:
            str: 卡牌标题
        '''
        info = self.get_info()
        # 获取 prefix 数据
        if (prefix := info.get('prefix', None)) is None:
            raise Exception('无法获取卡牌标题。')
        # 获取第一个非 None 卡牌标题
        try:
            return next(filter(lambda x: x is not None, prefix))
        except StopIteration:
            raise Exception('无法获取卡牌标题。')
    
    # 获取卡牌所在服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取卡牌所在服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.get_info()
        # 获取 releasedAt 数据
        if (released_at := info.get('releasedAt', None)) is None:
            raise Exception('无法获取卡牌发布时间。')
        # 根据 releasedAt 数据判断服务器
        if released_at[0] is not None: return 'jp'
        elif released_at[1] is not None: return 'en'
        elif released_at[2] is not None: return 'tw'
        elif released_at[3] is not None: return 'cn'
        elif released_at[4] is not None: return 'kr'
        else:
            raise Exception('无法获取卡牌所在服务器。')
    
    # 获取卡牌完整图片
    def get_card(self, type_: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌完整图片

        参数:
            type_ (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌完整图片字节数据 `bytes`
        '''
        # 获取卡牌数据包名称
        info = self.get_info()
        if (resource_set_name := info.get('resourceSetName', None)) is None:
            raise ValueError('无法获取卡牌数据包名称。')
        return Assets(
            ASSETS['characters']['resourceset'].format(
                resource_set_name=resource_set_name, name='card', type=type_
            ), self.server, self.proxy
        ).get()
    
    # 获取卡牌无背景图片
    def get_trim(self, type_: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌无背景图片

        参数:
            type_ (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌无背景图片字节数据 `bytes`
        '''
        # 获取卡牌数据包名称
        info = self.get_info()
        if (resource_set_name := info.get('resourceSetName', None)) is None:
            raise ValueError('无法获取卡牌数据包名称。')
        return Assets(
            ASSETS['characters']['resourceset'].format(
                resource_set_name=resource_set_name, name='trim', type=type_
            ), self.server, self.proxy
        ).get()
    
    # 获取卡牌缩略图图片
    def get_thumb(self, type_: Literal['normal', 'after_training']) -> bytes:
        '''获取卡牌缩略图图片

        参数:
            type (Literal[&#39;normal&#39;, &#39;after_training&#39;]): 指定特训前或特训后

        返回:
            bytes: 卡牌缩略图图片字节数据 `bytes`
        '''
        # 获取卡牌数据包名称
        info = self.get_info()
        if (resource_set_name := info.get('resourceSetName', None)) is None:
            raise ValueError('无法获取卡牌数据包名称。')
        return Assets(
            ASSETS['thumb']['chara'].format(
                id=str(int(self.id) // 50), resource_set_name=resource_set_name, type=type_
            ), self.server, self.proxy
        ).get()
    
    # 获取 LIVE 服装图片
    def get_livesd(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 卡牌 LIVE 服装图片字节数据 `bytes`
        '''
        # 获取卡牌 livesd 数据包名称
        info = self.get_info()
        if (sd_resource_name := info.get('sdResourceName', None)) is None:
            raise ValueError('无法获取卡牌 livesd 数据包名称。')
        return Assets(
            ASSETS['characters']['livesd'].format(
                sd_resource_name=sd_resource_name
            ), self.server, self.proxy
        ).get()
