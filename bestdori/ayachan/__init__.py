'''`bestdori.ayachan`

ayachan 的各种 API 调用整合'''
from pathlib import Path
from mimetypes import guess_type
from typing import Any, Union, Literal, Optional

from ..charts import Chart
from .utils import Api, API
from .exceptions import SonolusException

# 自定义谱面分析
def chart_analysis(map_: Chart, diff: Literal['0', '1', '2', '3', '4']) -> dict[str, Any]:
    '''自定义谱面分析

    参数:
        map_ (Chart): 谱面
        diff (Literal[&#39;0&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;]): 难度

    返回:
        dict[str, Any]: 分析结果
    '''
    payload = {
        'options': {
            'diff': diff
        },
        'map': map_.to_list(),
        'map_format_in': 'BestdoriV2'
    }
    return Api(API['map-info']).request('post', data=payload).json()

# Bestdori 谱面分析
def bestdori_chart_analysis(
    id_: int,
    diff: Literal['0', '1', '2', '3', '4']
) -> dict[str, Any]:
    '''Bestdori 谱面分析

    参数:
        id_ (int): 谱面 ID
        diff (Literal[&#39;0&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;]): 难度

    返回:
        dict[str, Any]: 分析结果
    '''
    return Api(API['bestdori'].format(id=id_)).request(
        'get',
        params={
            'diff': diff
        }
    ).json()

# Sonolus 谱面测试
def sonolus_test(
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
        raise SonolusException('上传测试服失败。')
    return uid

# 难度分析
def diff_analysis(
    id_: int,
    diff: Optional[Literal[0, 1, 2, 3, 4]]=None
) -> dict[str, Any]:
    '''难度分析

    参数:
        id_ (int): 谱面 ID
        diff (Optional[Literal[0, 1, 2, 3, 4]], optional): 谱面难度

    返回:
        dict[str, Any]: 难度分析结果
    '''
    # 构建数据
    params = {'id': id_}
    if diff is not None:
        params['diff'] = diff
    
    # 获取结果
    return Api(API['DiffAnalysis']).request('get', params=params).json()

from .utils._settings import settings as settings
