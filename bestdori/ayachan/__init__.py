'''`bestdori.ayachan`

ayachan 的各种 API 调用整合'''
from pathlib import Path
from mimetypes import guess_type
from typing import Any, Union, Literal

from httpx import Response

from .utils import API, Api
from bestdori.charts import Chart
from .exceptions import SonolusException

DIFF_STR = ['easy', 'normal', 'hard', 'expert', 'special']

# 自定义谱面分析
def chart_metrics_custom(chart: Chart, diff: Literal[0, 1, 2, 3, 4]) -> dict[str, Any]:
    '''自定义谱面分析

    参数:
        chart (Chart): 谱面
        diff (Literal[0, 1, 2, 3, 4]): 难度类型

    返回:
        dict[str, Any]: 分析结果
    '''
    return Api(API['chart_metrics']['custom'].format(diff_str=DIFF_STR[diff])).post(data=chart.to_list()).json()

# 异步自定义谱面分析
async def chart_metrics_custom_async(chart: Chart, diff: Literal[0, 1, 2, 3, 4]) -> dict[str, Any]:
    '''自定义谱面分析

    参数:
        chart (Chart): 谱面
        diff (Literal[0, 1, 2, 3, 4]): 难度类型

    返回:
        dict[str, Any]: 分析结果
    '''
    response = await Api(API['chart_metrics']['custom'].format(diff_str=DIFF_STR[diff])).apost(data=chart.to_list())
    if isinstance(response, Response): return response.json()
    return await response.json()

# BanG Dream 谱面分析
def chart_metrics_bandori(
    id: int,
    diff: Literal[0, 1, 2, 3, 4]
) -> dict[str, Any]:
    '''BanG Dream 谱面分析

    参数:
        id (int): 歌曲 ID
        diff (Literal[0, 1, 2, 3, 4]): 难度类型

    返回:
        dict[str, Any]: 分析结果
    '''
    return Api(API['chart_metrics']['bandori'].format(chart_id=id, diff_str=DIFF_STR[diff])).get().json()

# 异步 BanG Dream 谱面分析
async def chart_metrics_bandori_async(
    id: int,
    diff: Literal[0, 1, 2, 3, 4]
) -> dict[str, Any]:
    '''BanG Dream 谱面分析

    参数:
        id (int): 歌曲 ID
        diff (Literal[0, 1, 2, 3, 4]): 难度类型

    返回:
        dict[str, Any]: 分析结果
    '''
    response = await Api(API['chart_metrics']['bandori'].format(chart_id=id, diff_str=DIFF_STR[diff])).aget()
    if isinstance(response, Response): return response.json()
    return await response.json()

# Bestdori 谱面分析
def chart_metrics_bestdori(id: int) -> dict[str, Any]:
    '''Bestdori 谱面分析

    参数:
        id (int): 谱面 ID

    返回:
        dict[str, Any]: 分析结果
    '''
    return Api(API['chart_metrics']['bestdori'].format(chart_id=id)).get().json()

# 异步 Bestdori 谱面分析
async def chart_metrics_bestdori_async(id: int) -> dict[str, Any]:
    '''Bestdori 谱面分析

    参数:
        id (int): 谱面 ID

    返回:
        dict[str, Any]: 分析结果
    '''
    response = await Api(API['chart_metrics']['bestdori'].format(chart_id=id)).aget()
    if isinstance(response, Response): return response.json()
    return await response.json()

# Sonolus 谱面测试上传
def post_sonolus_levels(
    title: str,
    bgm: Union[str, Path],
    difficulty: int,
    hidden: bool,
    lifetime: Literal[3600, 10800, 21600, 43200, 86400],
    chart: Chart
) -> int:
    '''Sonolus 谱面测试

    参数:
        title (str): 谱面标题
        bgm (Union[str, Path]): 音乐文件
        difficulty (int): 谱面难度
        hidden (bool): 谱面隐藏
        lifetime (Literal[3600, 10800, 21600, 43200, 86400]): 存活时间
        chart (Chart): 上传谱面

    返回:
        int: 测试服 ID
    '''
    # 转换文件路径并获取名称
    if isinstance(bgm, str):
        bgm = Path(bgm)
    bgm_name = bgm.name
    
    # 构建数据
    data: dict[str, Any] = {
        'title': title,
        'difficulty': str(difficulty),
        'lifetime': str(lifetime),
        'chart': chart.json()
    }
    if hidden:
        data['hidden'] = True
    
    # 准备文件
    file = open(bgm, 'rb')
    files = {'bgm': (bgm_name, file, guess_type(bgm)[0])}
    
    # 发送请求
    response = Api(API['levels']).post(data=data, files=files)
    file.close()
    if (uid := response.json().get('uid', None)) is None:
        description = response.json().get('description', None)
        detail = response.json().get('detail', None)
        raise SonolusException(f'{description} {detail}')
    return uid

# 异步 Sonolus 谱面测试上传
async def post_sonolus_levels_async(
    title: str,
    bgm: Union[str, Path],
    difficulty: int,
    hidden: bool,
    lifetime: Literal[3600, 10800, 21600, 43200, 86400],
    chart: Chart
) -> int:
    '''Sonolus 谱面测试

    参数:
        title (str): 谱面标题
        bgm (Union[str, Path]): 音乐文件
        difficulty (int): 谱面难度
        hidden (bool): 谱面隐藏
        lifetime (Literal[3600, 10800, 21600, 43200, 86400]): 存活时间
        chart (Chart): 上传谱面

    返回:
        int: 测试服 ID
    '''
    # 转换文件路径并获取名称
    if isinstance(bgm, str):
        bgm = Path(bgm)
    bgm_name = bgm.name
    
    # 构建数据
    data: dict[str, Any] = {
        'title': title,
        'difficulty': str(difficulty),
        'lifetime': str(lifetime),
        'chart': chart.json()
    }
    if hidden:
        data['hidden'] = True
    
    # 准备文件
    file = open(bgm, 'rb')
    files = {'bgm': (bgm_name, file, guess_type(bgm)[0])}
    
    # 发送请求
    response = await Api(API['levels']).apost(data=data, files=files)
    file.close()
    
    if isinstance(response, Response): response_json = response.json()
    else: response_json = await response.json()
    
    if (uid := response_json.get('uid', None)) is None:
        description = response_json.get('description', None)
        detail = response_json.get('detail', None)
        raise SonolusException(f'{description} {detail}')
    return uid

# Sonolus 测试服谱面获取
def get_sonolus_levels(uid: int) -> Chart:
    '''Sonolus 测试服谱面获取

    参数:
        uid (int): 测试服 ID

    返回:
        Chart: 谱面
    '''
    response = Api(API['levels']['get'].format(uid=uid)).get()
    return Chart.normalize(response.json())

# 异步 Sonolus 测试服谱面获取
async def get_sonolus_levels_async(uid: int) -> Chart:
    '''Sonolus 测试服谱面获取

    参数:
        uid (int): 测试服 ID

    返回:
        Chart: 谱面
    '''
    response = await Api(API['levels']['get'].format(uid=uid)).aget()
    if isinstance(response, Response): return Chart.normalize(response.json())
    return Chart.normalize(await response.json())

# Sonolus 测试服谱面信息获取
def sonolus_levels(uid: int) -> dict[str, Any]:
    '''Sonolus 测试服谱面信息获取

    参数:
        uid (int): 测试服 ID

    返回:
        dict[str, Any]: 谱面信息
    '''
    return Api(API['levels']['info'].format(uid=uid)).get().json()

# 异步 Sonolus 测试服谱面信息获取
async def sonolus_levels_async(uid: int) -> dict[str, Any]:
    '''Sonolus 测试服谱面信息获取

    参数:
        uid (int): 测试服 ID

    返回:
        dict[str, Any]: 谱面信息
    '''
    response = await Api(API['levels']['info'].format(uid=uid)).aget()
    if isinstance(response, Response): return response.json()
    return await response.json()

from .utils import settings as settings
