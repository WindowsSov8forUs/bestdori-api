'''`bestdori.costumes`

BanG Dream! 服装相关操作'''
from typing import Any, Literal

from .post import get_list
from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .exceptions import (
    NoDataException,
    AssetsNotExistError,
    CostumeNotExistError
)

# 获取总服装信息
def get_all(index: Literal[0, 5]=5) -> dict[str, dict[str, Any]]:
    '''获取总服装信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有服装 ID `all.0.json`
            `5`: 获取所有已有服装的简洁信息 `all.5.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总服装信息
    '''
    return Api(API['costumes']['all'].format(index=index)).request('get').json()

# 服装类
class Costume:
    '''服装类

    参数:
        id_ (int): 服装 ID
    '''
    # 初始化
    def __init__(self, id_: int) -> None:
        '''服装类

        参数:
            id_ (int): 服装 ID
        '''
        self.id: int = id_
        '''服装 ID'''
        self._info: dict[str, Any] = {}
        '''服装信息'''
        # 检测 ID 是否存在
        all_ = get_all(0)
        if not str(id_) in all_.keys():
            raise CostumeNotExistError(id_)
        return
    
    # 获取服装信息
    def get_info(self) -> dict[str, Any]:
        '''获取服装信息

        返回:
            dict[str, Any]: 服装详细信息
        '''
        if len(self._info) <= 0:
            # 如果没有服装信息存储
            response = Api(
                API['costumes']['info'].format(id=self.id)
            ).request('get')
            self._info = dict(response.json())
        return self._info
    
    # 获取服装评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取服装评论

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
        # 获取服装 sdchara 数据包名称
        info = self.get_info()
        if (sd_resource_name := info.get('sdResourceName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        return Assets(
            ASSETS['characters']['livesd'].format(
                sd_resource_name=sd_resource_name
            ), self.server
        ).get()
    
    # 获取角色 ID
    @property
    def character_id(self) -> int:
        '''获取角色 ID'''
        info = self.get_info()
        # 获取 characterId 数据
        if (character_id := info.get('characterId', None)) is None:
            raise NoDataException('角色 ID')
        return character_id
    
    # 获取卡牌 ID
    @property
    def card_id(self) -> int:
        '''获取角色 ID'''
        info = self.get_info()
        # 获取 cards 数据
        if (cards := info.get('cards', None)) is None:
            raise NoDataException('卡牌 ID')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(self.server)
        return cards[index]
    
    # 获取服装标题
    @property
    def description(self) -> str:
        '''获取服装标题

        返回:
            str: 服装标题
        '''
        info = self.get_info()
        # 获取 description 数据
        if (description := info.get('description', None)) is None:
            raise NoDataException('服装标题')
        # 获取第一个非 None 服装标题
        try:
            return next(filter(lambda x: x is not None, description))
        except StopIteration:
            raise NoDataException('服装标题')
    
    # 获取服装所在服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取服装所在服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.get_info()
        # 获取 publishedAt 数据
        if (published_at := info.get('publishedAt', None)) is None:
            raise NoDataException('服装发布时间')
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('服装所在服务器')
    
    # 获取服装模型数据
    @property
    def build_data(self) -> bytes:
        '''获取服装模型数据

        返回:
            bytes: 服装模型数据
        '''
        # 获取服装数据包名称
        info = self.get_info()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        try:
            return Assets(
                ASSETS['live2d']['buildData'].format(
                    asset_bundle_name=asset_bundle_name
                ), self.server
            ).get()
        except AssetsNotExistError:
            raise AssetsNotExistError(f'服装模型 {asset_bundle_name}-{self.server}')
    
    # 获取服装图标
    @property
    def icon(self) -> bytes:
        '''获取服装图标

        返回:
            bytes: 服装图标
        '''
        # 获取服装数据包名称
        info = self.get_info()
        if (asset_bundle_name := info.get('assetBundleName', None)) is None:
            raise ValueError('无法获取服装数据包名称。')
        try:
            return Assets(
                ASSETS['thumb']['costume'].format(
                    id=str(self.id // 50), asset_bundle_name=asset_bundle_name
                ), self.server
            ).get()
        except AssetsNotExistError:
            raise AssetsNotExistError(f'服装图标 {asset_bundle_name}-{self.server}')
