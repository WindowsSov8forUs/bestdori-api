'''`bestdori.ayachan.chartmetrics`

Ayachan 谱面信息分析获取模块'''

from typing import TYPE_CHECKING, Any, Dict, List, Union

from bestdori.charts import Chart
from bestdori.utils import get_api
from bestdori.utils.network import Api

if TYPE_CHECKING:
    from bestdori.typing import DifficultyName

    from .typing import ChartMetrics

API = get_api('ayachan.api')

# BanG Dream 谱面分析
def chart_metrics_bandori(
    chart_id: int,
    diff_str: DifficultyName,
) -> 'ChartMetrics':
    '''BanG Dream 谱面分析

    参数:
        chart_id (int): 谱面 ID
        diff_str (DifficultyName): 难度类型
    
    返回:
        ChartMetrics: 分析结果
    '''
    return Api(
        API['chart_metrics']['bandori'].format(chart_id=chart_id, diff_str=diff_str)
    ).get().json()

# 异步 BanG Dream 谱面分析
async def chart_metrics_bandori_async(
    chart_id: int,
    diff_str: DifficultyName,
) -> 'ChartMetrics':
    '''BanG Dream 谱面分析

    参数:
        chart_id (int): 谱面 ID
        diff_str (DifficultyName): 难度类型
    
    返回:
        ChartMetrics: 分析结果
    '''
    return (await Api(
        API['chart_metrics']['bandori'].format(chart_id=chart_id, diff_str=diff_str)
    ).aget()).json()

# Bestdori 谱面分析
def chart_metrics_bestdori(chart_id: int) -> 'ChartMetrics':
    '''Bestdori 谱面分析

    参数:
        chart_id (int): 谱面 ID

    返回:
        ChartMetrics: 分析结果
    '''
    return Api(API['chart_metrics']['bestdori'].format(chart_id=chart_id)).get().json()

# 异步 Bestdori 谱面分析
async def chart_metrics_bestdori_async(chart_id: int) -> 'ChartMetrics':
    '''Bestdori 谱面分析

    参数:
        chart_id (int): 谱面 ID

    返回:
        ChartMetrics: 分析结果
    '''
    return (await Api(API['chart_metrics']['bestdori'].format(chart_id=chart_id)).aget()).json()

# 自定义谱面分析
def chart_metrics_custom(
    diff_str: 'DifficultyName',
    chart: Union[Chart, List[Dict[str, Any]]],
) -> 'ChartMetrics':
    '''自定义谱面分析

    参数:
        diff_str (DifficultyName): 难度类型
        chart (Union[Chart, List[Dict[str, Any]]]): 谱面
    
    返回:
        ChartMetrics: 分析结果
    '''
    if not isinstance(chart, Chart):
        chart = Chart.from_python(chart)
    return Api(API['chart_metrics']['custom'].format(diff_str=diff_str)).post(data=chart.to_list()).json()

# 异步自定义谱面分析
async def chart_metrics_custom_async(
    diff_str: 'DifficultyName',
    chart: Union[Chart, List[Dict[str, Any]]],
) -> 'ChartMetrics':
    '''自定义谱面分析

    参数:
        diff_str (DifficultyName): 难度类型
        chart (Union[Chart, List[Dict[str, Any]]]): 谱面
    
    返回:
        ChartMetrics: 分析结果
    '''
    if not isinstance(chart, Chart):
        chart = Chart.from_python(chart)
    return (await Api(API['chart_metrics']['custom'].format(diff_str=diff_str)).apost(data=chart.to_list())).json()
