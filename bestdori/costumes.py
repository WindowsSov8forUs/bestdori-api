'''`bestdori.costumes`

BanG Dream! 服装相关操作'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional

from . import post
from .user import Me
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
        ServerName,
        CostumeInfo,
        CostumesAll5,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总服装信息
@overload
def get_all(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总服装信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有服装 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'CostumesAll5':
    '''获取总服装信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CostumesAll5: 所有已有服装的简洁信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[0, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'CostumesAll5']:
    return Api(API['costumes']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取总服装信息
@overload
async def get_all_async(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总服装信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 所有已有服装 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'CostumesAll5':
    '''获取总服装信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`

    返回:
        CostumesAll5: 所有已有服装的简洁信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[0, 5]=5, *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'CostumesAll5']:
    return (await Api(API['costumes']['all'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 服装类
class Costume:
    '''服装类

    参数:
        id (int): 服装 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''服装类

        参数:
            id (int): 服装 ID
        '''
        self.id: int = id
        '''服装 ID'''
        self.__info: Optional['CostumeInfo'] = None
        '''服装信息'''

        self.__me = me
        return
    
    @property
    def info(self) -> 'CostumeInfo':
        '''服装信息'''
        if self.__info is None:
            raise ValueError(f'Costume \'{self.id}\' info were not retrieved.')
        return self.__info

    # 获取服装信息
    def get_info(self) -> 'CostumeInfo':
        '''获取服装信息

        返回:
            CostumeInfo: 服装详细信息
        '''
        try:
            response = Api(
                API['costumes']['info'].format(id=self.id)
            ).get(cookies=self.__me.__get_cookies__() if self.__me else None)
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Costume {self.id}') from exception
            else:
                raise exception
        self.__info = response.json()
        return self.info
    
    def __get_info__(self) -> 'CostumeInfo':
        if self.__info is None:
            self.get_info()
        return self.info

    # 异步获取服装信息
    async def get_info_async(self) -> 'CostumeInfo':
        '''获取服装信息

        返回:
            CostumeInfo: 服装详细信息
        '''
        try:
            response = await Api(
                API['costumes']['info'].format(id=self.id)
            ).aget(cookies=await self.__me.__get_cookies_async__() if self.__me else None)
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Costume {self.id}') from exception
            else:
                raise exception
        self.__info = response.json()
        return self.info
    
    async def __get_info_async__(self) -> 'CostumeInfo':
        if self.__info is None:
            await self.get_info_async()
        return self.info
    
    # 提取角色 ID
    @property
    def __character_id__(self) -> int:
        '''提取角色 ID'''
        return self.info['characterId']
    
    # 提取卡牌 ID
    @property
    def __card_id__(self) -> int:
        '''提取卡牌 ID'''
        # 获取 cards 数据
        cards = self.info['cards']
        if len(cards) <= 0:
            raise NoDataException('Card ID')
        return cards[0]
    
    # 服装标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''服装标题'''
        return self.info['description']
    
    # 服装所在默认服务器
    @property
    def __server__(self) -> 'ServerName':
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
    
    # 获取服装评论
    def get_comment(
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
        return post.get_list(
            category_name='COSTUME_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
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
            offset=offset,
            me=self.__me,
        )
    
    # 获取 LIVE 服装图片
    def get_sdchara(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 服装 LIVE 图片字节数据 `bytes`
        '''
        info = self.__get_info__()
        return Api(
            ASSETS['characters']['livesd'].format(
                server=self.__server__, sd_resource_name=info['sdResourceName']
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
        ).content
    
    # 异步获取 LIVE 服装图片
    async def get_sdchara_async(self) -> bytes:
        '''获取 LIVE 服装图片

        返回:
            bytes: 服装 LIVE 图片字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        return (await Api(
            ASSETS['characters']['livesd'].format(
                server=self.__server__, sd_resource_name=info['sdResourceName']
            )
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None,
        )).content
    
    # 获取服装模型数据
    def get_build_data(self) -> bytes:
        '''获取服装模型数据

        返回:
            bytes: 服装模型数据
        '''
        info = self.__get_info__()
        # 获取服装数据包名称
        asset_bundle_name = info['assetBundleName']
        try:
            return Api(
                ASSETS['live2d']['buildData'].format(
                    server=self.__server__, asset_bundle_name=asset_bundle_name
                )
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
            ).content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume build data {asset_bundle_name}-{self.__server__}')
    
    # 异步获取服装模型数据
    async def get_build_data_async(self) -> bytes:
        '''获取服装模型数据

        返回:
            bytes: 服装模型数据
        '''
        info = await self.__get_info_async__()
        # 获取服装数据包名称
        asset_bundle_name = info['assetBundleName']
        try:
            return (await Api(
                ASSETS['live2d']['buildData'].format(
                    server=self.__server__, asset_bundle_name=asset_bundle_name
                )
            ).aget(
                cookies=await self.__me.__get_cookies_async__() if self.__me else None,
            )).content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume build data {asset_bundle_name}-{self.__server__}')
    
    # 获取服装图标
    def get_icon(self) -> bytes:
        '''获取服装图标

        返回:
            bytes: 服装图标
        '''
        info = self.__get_info__()
        # 获取服装数据包名称
        asset_bundle_name = info['assetBundleName']
        try:
            return Api(
                ASSETS['thumb']['costume'].format(
                    server=self.__server__, id=self.id // 50, asset_bundle_name=asset_bundle_name
                )
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
            ).content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume icon {asset_bundle_name}-{self.__server__}')
    
    # 异步获取服装图标
    async def get_icon_async(self) -> bytes:
        '''获取服装图标

        返回:
            bytes: 服装图标
        '''
        info = await self.__get_info_async__()
        # 获取服装数据包名称
        asset_bundle_name = info['assetBundleName']
        try:
            return (await Api(
                ASSETS['thumb']['costume'].format(
                    server=self.__server__, id=self.id // 50, asset_bundle_name=asset_bundle_name
                )
            ).aget(
                cookies=await self.__me.__get_cookies_async__() if self.__me else None,
            )).content
        except AssetsNotExistError:
            raise AssetsNotExistError(f'costume icon {asset_bundle_name}-{self.__server__}')
