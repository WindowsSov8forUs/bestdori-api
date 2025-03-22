'''`bestdori.utils`

杂项模块'''

import sys
from json import load
from functools import lru_cache
from importlib import resources
from typing import Dict, List, Tuple, Optional, Protocol

class _NamedObject(Protocol):
    '''可获取 `__name__` 属性方法的类型'''

    @property
    def __name__(self) -> List[Optional[str]]: ...

@lru_cache(maxsize=128)
def get_api(*paths: str) -> Dict[str, Dict[str, str]]:
    '''获取 API 字典

    参数:
        *paths (str): API 文件路径

    返回:
        Dict[str, Dict[str, str]]: API 字典
    '''
    _paths = []
    for path in paths:
        _paths.extend(path.split('.'))
    
    if len(_paths) == 1:
        _path = "bestdori.data.api"
    else:
        _path = "bestdori.data.api." + '.'.join(_paths[:-1])
    filename = _paths[-1] + '.json'
    
    if sys.version_info < (3, 11):
        with resources.open_text(_path, filename) as f:
            return load(f)
    else:
        path = resources.files(_path).joinpath(filename)
        with path.open('r') as f:
            return load(f)

# 将十六进制颜色代码转换为 RGB 元组
def hex_to_rgb(hex: str) -> Tuple[int, int, int]:
    '''将十六进制颜色代码转换为 RGB 元组

    参数:
        hex (str): 十六进制颜色代码

    返回:
        Tuple[int, int, int]: RGB 元组
    '''
    if hex[0] == '#':
        hex = hex[1:]
    if len(hex) == 3:
        hex = hex[0] * 2 + hex[1] * 2 + hex[2] * 2
    rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    if len(rgb) != 3:
        raise ValueError('Invalid hex color code')
    return rgb

# 提取名称列表中第一个非空元素
def name(obj: _NamedObject) -> str:
    '''提取名称列表中第一个非空元素

    参数:
        obj (_NamedObject): 可获取 `__name__` 属性方法的对象

    返回:
        str: 名称
    '''
    return next(filter(None, obj.__name__))
