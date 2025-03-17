'''`bestdori.utils`

杂项模块'''
from json import load
from typing import Dict, Tuple
from functools import lru_cache
from importlib import resources

@lru_cache(maxsize=128)
def get_api(*paths: str) -> Dict[str, Dict[str, str]]:
    '''获取 API 字典

    参数:
        *path (str): API 文件路径

    返回:
        Dict[str, Dict[str, str]]: API 字典
    '''
    if len(paths) == 1:
        _path = "bestdori.data.api"
    else:
        _path = "bestdori.data.api." + '.'.join(paths[:-1])
    filename = paths[-1] + '.json'
    
    with resources.open_text(_path, filename) as f:
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
