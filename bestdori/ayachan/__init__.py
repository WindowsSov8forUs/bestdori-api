'''`bestdori.ayachan`

ayachan 的各种 API 调用整合'''
from pathlib import Path
from mimetypes import guess_type
from typing import Any, Union, Literal, Optional

from ..charts import Chart
from .utils import API, Api
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
    return Api(API['chart_metrics']['custom'].format(diff_str=DIFF_STR[diff])).request('post', data=chart.to_list()).json()

# BanG Dream 谱面分析
def chart_metrics_bandori(
    id_: int,
    diff: Literal[0, 1, 2, 3, 4]
) -> dict[str, Any]:
    '''BanG Dream 谱面分析

    参数:
        id_ (int): 歌曲 ID
        diff (Literal[0, 1, 2, 3, 4]): 难度类型

    返回:
        dict[str, Any]: 分析结果
    '''
    return Api(API['chart_metrics']['bandori'].format(chart_id=id_, diff_str=DIFF_STR[diff])).request('get').json()

# Bestdori 谱面分析
def chart_metrics_bestdori(
    id_: int
) -> dict[str, Any]:
    '''Bestdori 谱面分析

    参数:
        id_ (int): 谱面 ID

    返回:
        dict[str, Any]: 分析结果
    '''
    return Api(API['chart_metrics']['bestdori'].format(chart_id=id_)).request('get').json()

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
    response = Api(API['levels']).request('post', data=data, files=files)
    file.close()
    if (uid := response.json().get('uid', None)) is None:
        description = response.json().get('description', None)
        detail = response.json().get('detail', None)
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
    response = Api(API['levels']['get'].format(uid=uid)).request('get')
    return Chart.normalize(response.json())

from .utils._settings import settings as settings
