'''`bestdori.utils`

杂项模块'''
from typing import Optional, Literal, Any

from .utils import API, RES,ASSETS
from .network import Api, Res, Assets
from ..exceptions import (
    AssetsNotExistError
)

# 将十六进制颜色代码转换为 RGB 元组
def hex_to_rgb(hex_: str) -> tuple[int, int, int]:
    '''将十六进制颜色代码转换为 RGB 元组

    参数:
        hex_ (str): 十六进制颜色代码

    返回:
        tuple[int, int, int]: RGB 元组
    '''
    if hex_[0] == '#':
        hex_ = hex_[1:]
    if len(hex_) == 3:
        hex_ = hex_[0] * 2 + hex_[1] * 2 + hex_[2] * 2
    rgb = tuple(int(hex_[i:i+2], 16) for i in (0, 2, 4))
    if len(rgb) != 3:
        raise ValueError('十六进制颜色代码')
    return rgb

# 获取称号资源
def get_degree(
    degree_name: str,
    server: Literal['jp', 'en', 'tw', 'cn', 'kr'],
    proxy: Optional[str]=None
) -> bytes:
    '''获取称号资源

    参数:
        degree_name (str): 称号名称
        
        server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        bytes: 称号资源字节数据 `bytes`
    '''
    try:
        return Assets(ASSETS['thumb']['degree'].format(degree_name=degree_name), server, proxy).get()
    except AssetsNotExistError:
        raise AssetsNotExistError(f'称号 {degree_name}-{server}')

# 获取总技能信息
def get_skill_all(index: Literal[10]=10, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总技能信息

    参数:
        index (Literal[10], optional): 指定获取哪种 `all.json`
            `10`: 获取所有已有技能的信息 `all.5.json`
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总技能信息
    '''
    return Api(API['all']['skills'].format(index=index), proxy=proxy).request('get').json()

# 获取总乐队信息
def get_bands_all(index: Literal[1]=1, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取总乐队信息

    参数:
        index (Literal[1], optional): 指定获取哪种 `all.json`
            `1`: 获取所有已有乐队的名称信息 `all.1.json`，默认为该项
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的总乐队信息
    '''
    return Api(API['bands']['all'].format(index=index), proxy=proxy).request('get').json()

# 获取主要乐队信息
def get_bands_main(index: Literal[1]=1, proxy: Optional[str]=None) -> dict[str, dict[str, Any]]:
    '''获取主要乐队信息

    参数:
        index (Literal[1], optional): 指定获取哪种 `main.json`
            `1`: 获取所有主要乐队的名称信息 `main.1.json`，默认为该项
        
        proxy (Optional[str], optional): 代理服务器

    返回:
        dict[str, dict[str, Any]]: 获取到的主要乐队信息
    '''
    return Api(API['bands']['main'].format(index=index), proxy=proxy).request('get').json()

# 获取乐队 logo
def get_band_logo(
    id_: int,
    type_: Literal['logoS', 'logoL', 'logoL_Mask'],
    server: Literal['jp', 'en', 'tw', 'cn', 'kr']
) -> bytes:
    '''获取乐队 logo

    参数:
        id_ (int): 乐队 ID
        
        type_ (Literal[&#39;logoS&#39;, &#39;logoL&#39;, &#39;logoL_Mask&#39;]): logo 类型
            `logoS`: 小 logo
            `logoL`: 大 logo
            `logoL_Mask`: 大 logo 遮罩
        
        server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 指定服务器

    返回:
        bytes: 乐队 logo 字节数据 `bytes`
    '''
    return Assets(ASSETS['band']['logo'].format(id=id_, type=type_), server).get()

# 获取乐队图标
def get_band_icon(id_: str) -> bytes:
    '''获取乐队图标

    参数:
        id_ (str): 乐队 ID

    返回:
        bytes: 乐队图标字节数据
    '''
    return Res(RES['icon']['svg'].format(name=f'band_{id_}')).get()

# 获取服务器图标
def get_server_icon(server: Literal['jp', 'en', 'tw', 'cn', 'kr']) -> bytes:
    '''获取服务器图标

    参数:
        server (Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]): 服务器名称
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服

    返回:
        bytes: 服务器图标字节数据
    '''
    return Res(RES['icon']['svg'].format(name=server)).get()

from .content import Content
