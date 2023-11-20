'''`bestdori.gacha`

BanG Dream! 招募相关操作'''
from typing import Optional, Literal, Any

from .post import get_list
from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .exceptions import (
    ServerNotAvailableError,
    AssetsNotExistError,
    GachaNotExistError
)

# 获取总招募信息
def get_all(index: Literal[0, 5]=5, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总招募信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有招募 ID `all.0.json`
            `5`: 获取所有已有招募的简洁信息 `all.5.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总招募信息
    '''
    return Api(API['gacha']['all'].format(index), proxy=proxy).request('get').json()

# 招募类
class Gacha:
    '''招募类

    参数:
        id_ (int): 招募 ID
        
        proxy (Optional[str], optional): 代理服务器
    '''
    # 初始化
    def __init__(self, id_: int, proxy: Optional[str]=None) -> None:
        '''招募类

        参数:
            id_ (int): 招募 ID
            
            proxy (Optional[str], optional): 代理服务器
        '''
        self.id: int = id_
        '''招募 ID'''
        self._info: dict[str, Any] = {}
        '''招募信息'''
        self.proxy: Optional[str] = proxy
        '''代理服务器'''
        # 检测 ID 是否存在
        all_id = get_all(0, proxy=proxy)
        if not id_ in all_id.keys():
            raise GachaNotExistError(id_)
        return
    
    # 获取招募信息
    def get_info(self) -> dict[str, Any]:
        '''获取招募信息

        返回:
            dict[str, Any]: 招募详细信息
        '''
        if len(self._info) <= 0:
            # 如果没有招募信息存储
            response = Api(
                API['gacha']['info'].format(self.id), proxy=self.proxy
            ).request('get')
            self._info = dict(response.json())
        return self._info
    
    # 获取招募评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取招募评论

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
            category_name='GACHA_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取招募标题
    @property
    def name(self) -> str:
        '''获取招募标题

        返回:
            str: 招募标题
        '''
        info = self.get_info()
        # 获取 eventName 数据
        if (gacha_name := info.get('gachaName', None)) is None:
            raise Exception('无法获取招募标题。')
        # 获取第一个非 None 招募标题
        try:
            return next(filter(lambda x: x is not None, gacha_name))
        except StopIteration:
            raise Exception('无法获取招募标题。')
    
    # 获取招募默认服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取招募默认服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.get_info()
        # 获取 publishedAt 数据
        if (published_at := info.get('publishedAt', None)) is None:
            raise Exception('无法获取招募起始时间。')
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise Exception('无法获取招募所在服务器。')
    
    # 获取招募缩略图图片
    def get_banner(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取招募缩略图图片

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

        返回:
            bytes: 招募缩略图图片字节数据 `bytes`
        '''
        # 获取招募数据包名称
        info = self.get_info()
        if (banner_asset_bundle_name := info.get('bannerAssetBundleName', None)) is None:
            raise ValueError('无法获取招募数据包名称。')
        # 判断服务器
        if (start_at := info.get('startAt', None)) is None:
            raise ValueError('无法获取招募起始时间。')
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'招募 {self.name}', server)
        return Assets(
            ASSETS['homebanner']['get'].format(
                banner_asset_bundle_name=banner_asset_bundle_name
            ), server, self.proxy
        ).get()
    
    # 获取招募 pickup 图像
    def get_pickups(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> list[bytes]:
        '''获取招募 pickup 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): _description_

        返回:
            list[bytes]: pickup 图像字节数据 `bytes` 列表
        '''
        PICKUPS = ['pickup1', 'pickup2', 'pickup']
        # 遍历尝试获取
        pickup_list: list[bytes] = []
        for pickup in PICKUPS:
            try:
                pickup_list.append(
                    Assets(
                        ASSETS['gacha']['screen'].format(
                            id=self.id, asset_name=pickup
                        ), server, self.proxy
                    ).get()
                )
            except:
                continue
        if len(pickup_list) <= 0:
            # 没有获取到任何 pickup 图像
            raise AssetsNotExistError('招募 pickup 图像')
        return pickup_list
    
    # 获取招募 logo 图像
    def get_logo(self, server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
        '''获取招募 logo 图像

        参数:
            server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): _description_

        返回:
            bytes: logo 图像字节数据 `bytes`
        '''
        try:
            return Assets(
                ASSETS['gacha']['screen'].format(
                    id=self.id, asset_name='logo'
                ), server, self.proxy
            ).get()
        except:
            raise AssetsNotExistError('招募 logo 图像')
