'''`bestdori.costumes`

BanG Dream! 服装相关操作'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, Union, Literal

from . import post
from .utils import get_api
from .utils.network import Api
from .exceptions import (
    HTTPStatusError,
    NoDataException,
    NotExistException,
    AssetsNotExistError,
)

if TYPE_CHECKING:
    from .typing import (
        NoneDict,
        PostList,
        CostumeInfo,
        CostumesAll5,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总服装信息
@overload
def get_all(index: Literal[0]) -> Dict[str, 'NoneDict']:
    '''获取总服装信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有服装 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[5]) -> 'CostumesAll5':
    '''获取总服装信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CostumesAll5: 所有已有服装的简洁信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[0, 5]=5) -> Union[Dict[str, 'NoneDict'], 'CostumesAll5']:
    return Api(API['costumes']['all'].format(index=index)).get().json()

# 异步获取总服装信息
@overload
async def get_all_async(index: Literal[0]) -> Dict[str, 'NoneDict']:
    '''获取总服装信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有服装 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5]) -> 'CostumesAll5':
    '''获取总服装信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CostumesAll5: 所有已有服装的简洁信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[0, 5]=5) -> Union[Dict[str, 'NoneDict'], 'CostumesAll5']:
    return (await Api(API['costumes']['all'].format(index=index)).aget()).json()

# 服装类
class Costume:
    '''服装类

    参数:
        id (int): 服装 ID
    '''
    # 初始化
    def __init__(self, id: int, info: 'CostumeInfo') -> None:
        '''服装类

        参数:
            id (int): 服装 ID
        '''
        self.id: int = id
        '''服装 ID'''
        self.info: 'CostumeInfo' = info
        '''服装信息'''
        return
    
    # 角色 ID
    @property
    def character_id(self) -> int:
        '''角色 ID'''
        return self.info['characterId']
    
    # 卡牌 ID
    @property
    def card_id(self) -> int:
        '''卡牌 ID'''
        # 获取 cards 数据
        cards = self.info['cards']
        if len(cards) <= 0:
            raise NoDataException('Card ID')
        return cards[0]
    
    # 服装标题
    @property
    def description(self) -> str:
        '''服装标题'''
        # 获取第一个非 None 服装标题
        try:
            return next(x for x in self.info['description'] if x is not None)
        except StopIteration:
            raise NoDataException('costume description')
    
    # 服装所在默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''服装所在默认服务器'''
        # 获取 publishedAt 数据
        published_at = self.info['publishedAt']
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('costume server')
    
    # 获取服装信息
    @classmethod
    def get(cls, id: int) -> 'Costume':
        '''获取服装信息

        返回:
            Costume: 服装详细信息
        '''
        try:
            response = Api(
                API['costumes']['info'].format(id=id)
            ).get()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Costume {id}') from exception
            else:
                raise exception
        
        return cls(id, response.json())
    
    # 异步获取服装信息
    @classmethod
    async def get_async(cls, id: int) -> 'Costume':
        '''获取服装信息

        返回:
            Costume: 服装详细信息
        '''
        try:
            response = await Api(
                API['costumes']['info'].format(id=id)
            ).aget()
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Costume {id}') from exception
            else:
                raise exception
        
        return cls(id, response.json())
    
    # 获取服装评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> PostList:
        '''获取服装评论

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
                    "posts": ... # List[PostListList] 列举出的评论
                }
                ```
        '''
        return post.get_list(
            category_name='COSTUME_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 异步获取服装评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取服装评论

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
                    "posts": ... # List[PostListList] 列举出的评论
                }
                ```
        '''
        return await post.get_list_async(
            category_name='COSTUME_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取 LIVE 服装图片
    def get_sdchara(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 服装 LIVE 图片字节数据 `bytes`
        '''
        return Api(
            ASSETS['characters']['livesd'].format(
                server=self.server, sd_resource_name=self.info['sdResourceName']
            )
        ).get().content
    
    # 异步获取 LIVE 服装图片
    async def get_sdchara_async(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 服装 LIVE 图片字节数据 `bytes`
        '''
        return (await Api(
            ASSETS['characters']['livesd'].format(
                server=self.server, sd_resource_name=self.info['sdResourceName']
            )
        ).aget()).content
    
    # 获取服装模型数据
    def get_build_data(self) -> bytes:
        '''获取服装模型数据

        返回:
            bytes: 服装模型数据
        '''
        # 获取服装数据包名称
        asset_bundle_name = self.info['assetBundleName']
        try:
            return Api(
                ASSETS['live2d']['buildData'].format(
                    server=self.server, asset_bundle_name=asset_bundle_name
                )
            ).get().content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume build data {asset_bundle_name}-{self.server}')
    
    # 异步获取服装模型数据
    async def get_build_data_async(self) -> bytes:
        '''获取服装模型数据

        返回:
            bytes: 服装模型数据
        '''
        # 获取服装数据包名称
        asset_bundle_name = self.info['assetBundleName']
        try:
            return (await Api(
                ASSETS['live2d']['buildData'].format(
                    server=self.server, asset_bundle_name=asset_bundle_name
                )
            ).aget()).content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume build data {asset_bundle_name}-{self.server}')
    
    # 获取服装图标
    def get_icon(self) -> bytes:
        '''获取服装图标

        返回:
            bytes: 服装图标
        '''
        # 获取服装数据包名称
        asset_bundle_name = self.info['assetBundleName']
        try:
            return Api(
                ASSETS['thumb']['costume'].format(
                    server=self.server, id=str(self.id // 50), asset_bundle_name=asset_bundle_name
                )
            ).get().content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume icon {asset_bundle_name}-{self.server}')
    
    # 异步获取服装图标
    async def get_icon_async(self) -> bytes:
        '''获取服装图标

        返回:
            bytes: 服装图标
        '''
        # 获取服装数据包名称
        asset_bundle_name = self.info['assetBundleName']
        try:
            return (await Api(
                ASSETS['thumb']['costume'].format(
                    server=self.server, id=str(self.id // 50), asset_bundle_name=asset_bundle_name
                )
            ).aget()).content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume icon {asset_bundle_name}-{self.server}')
