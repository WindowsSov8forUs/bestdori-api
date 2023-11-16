'''`bestdori.characters`

BanG Dream! 角色相关操作'''
from typing import Optional, Literal, Any

from .post import get_list
from .utils import hex_to_rgb
from .utils.utils import API, RES, ASSETS
from .utils.network import Api, Res, Assets
from .exceptions import (
    CharacterNotExistError
)

# 获取总角色信息
def get_all(index: Literal['2']='2', proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总角色信息

    参数:
        index (Literal[&#39;0&#39;, &#39;5&#39;], optional): 指定获取哪种 `all.json`
            `2`: 获取所有已有角色信息 `all.2.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总角色信息
    '''
    return Api(API['characters']['all'].format(index), proxy=proxy).request('get').json()

# 获取主要角色信息
def get_main(index: Literal['3']='3', proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取主要角色信息

    参数:
        index (Literal[&#39;0&#39;, &#39;5&#39;], optional): 指定获取哪种 `all.json`
            `3`: 获取所有已有主要角色信息 `all.3.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的主要角色信息
    '''
    return Api(API['characters']['main'].format(index), proxy=proxy).request('get').json()

# 角色类
class Character:
    '''角色类

    参数:
        id_ (str): 角色 ID
        
        proxy (Optional[str], optional): 代理服务器
    '''
    # 初始化
    def __init__(self, id_: str, proxy: Optional[str]=None) -> None:
        '''角色类

        参数:
            id_ (str): 角色 ID
            
            proxy (Optional[str], optional): 代理服务器
        '''
        if not id_.isdigit():
            raise ValueError('角色 ID 必须为纯数字。')
        self.id: str = id_
        '''角色 ID'''
        self._info: dict[str, Any] = {}
        '''角色信息'''
        self.proxy: Optional[str] = proxy
        '''代理服务器'''
        # 检测 ID 是否存在
        all_id = get_all('2', proxy=proxy)
        if not id_ in all_id.keys():
            raise CharacterNotExistError(id_)
        return
    
    # 获取角色信息
    def get_info(self) -> dict[str, Any]:
        '''获取角色信息

        返回:
            dict[str, Any]: 角色详细信息
        '''
        if len(self._info) <= 0:
            # 如果没有角色信息存储
            response = Api(
                API['characters']['info'].format(self.id), proxy=self.proxy
            ).request('get')
            self._info = dict(response.json())
        return self._info
    
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
            result: bool # 是否有响应
            count: int # 搜索到的评论总数
            posts: list[dict[str, Any]] # 列举出的评论
            ```
        '''
        return get_list(
            proxy=self.proxy,
            category_name='CHARACTER_COMMENT',
            category_id=self.id,
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 获取角色名称
    @property
    def name(self) -> str:
        '''获取角色名称

        返回:
            str: 角色名称
        '''
        info = self.get_info()
        # 获取 characterName 数据
        if (character_name := info.get('characterName', None)) is None:
            raise Exception('无法获取角色名称。')
        # 获取第一个非 None 角色名称
        try:
            return next(filter(lambda x: x is not None, character_name))
        except StopIteration:
            raise Exception('无法获取角色名称。')
    
    # 获取角色图标
    @property
    def icon(self) -> bytes:
        '''获取角色图标

        返回:
            bytes: 角色图标字节数据 `bytes`
        '''
        return Res(RES['icon']['png'].format(name=f'chara_icon_{self.id}')).get()
    
    # 获取角色颜色
    @property
    def color(self) -> tuple[int, int, int]:
        '''获取角色颜色

        返回:
            tuple[int, int, int]: 角色颜色元组
        '''
        info = self.get_info()
        # 获取 colorCode 数据
        if (color_code := info.get('colorCode', None)) is None:
            raise Exception('无法获取角色颜色。')
        # 将 colorCode 转换为颜色元组
        try:
            return hex_to_rgb(color_code)
        except ValueError:
            raise Exception('无法获取角色颜色。')
    
    # 获取角色主视觉图
    def get_kv_image(self) -> bytes:
        '''获取角色主视觉图

        返回:
            bytes: 主视觉图资源字节 `bytes`
        '''
        return Assets(
            ASSETS['characters']['character_kv_image'].format(id=self.id), 'jp', self.proxy
        ).get()
