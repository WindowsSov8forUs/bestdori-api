'''`bestdori.ayachan.sonolus`

Sonolus 测试服模块'''

from pathlib import Path
from mimetypes import guess_type
from typing import TYPE_CHECKING, Any, Dict, List, Union

from bestdori.charts import Chart
from bestdori.utils import get_api
from bestdori.utils.network import Api

if TYPE_CHECKING:
    from .typing import Level

API = get_api('ayachan.sonolus')

# Sonolus 谱面测试上传
def levels_post(
    title: str,
    bgm: Union[str, Path],
    chart: Union[Chart, List[Dict[str, Any]]],
    difficulty: int = 25,
    hidden: bool = False,
    lifetime: int = 21600,
) -> int:
    '''Sonolus 谱面测试

    参数:
        title (str): 谱面标题
        bgm (Union[str, Path]): 音乐文件
        chart (Union[Chart, List[Dict[str, Any]]]): 上传谱面
        difficulty (int, optional): 谱面难度. 默认为 25
        hidden (bool, optional): 谱面隐藏. 默认为 False
        lifetime (int, optional): 存活时间. 默认为 21600

    返回:
        int: 测试服 ID
    '''
    # 转换文件路径并获取名称
    if isinstance(bgm, str):
        bgm = Path(bgm)
    bgm_name = bgm.name

    if not isinstance(chart, Chart):
        chart = Chart(chart)
    
    # 构建数据
    data: Dict[str, Any] = {
        'title': title,
        'chart': chart.json(),
        'difficulty': difficulty,
        'lifetime': lifetime,
    }
    if hidden:
        data['hidden'] = True
    
    # 准备文件
    file = open(bgm, 'rb')
    files = {'bgm': (bgm_name, file, guess_type(bgm)[0])}
    
    # 发送请求
    response = Api(API['levels']['post']).post(data=data, files=files)
    file.close()
    if (uid := response.json().get('uid', None)) is None:
        raise ValueError(f"Unable to get `uid` from response: {response.json()}")
    return uid

# 异步 Sonolus 谱面测试上传
async def levels_post_async(
    title: str,
    bgm: Union[str, Path],
    chart: Union[Chart, List[Dict[str, Any]]],
    difficulty: int = 25,
    hidden: bool = False,
    lifetime: int = 21600,
) -> int:
    '''Sonolus 谱面测试

    参数:
        title (str): 谱面标题
        bgm (Union[str, Path]): 音乐文件
        chart (Union[Chart, List[Dict[str, Any]]]): 上传谱面
        difficulty (int, optional): 谱面难度. 默认为 25
        hidden (bool, optional): 谱面隐藏. 默认为 False
        lifetime (int, optional): 存活时间. 默认为 21600

    返回:
        int: 测试服 ID
    '''
    # 转换文件路径并获取名称
    if isinstance(bgm, str):
        bgm = Path(bgm)
    bgm_name = bgm.name

    if not isinstance(chart, Chart):
        chart = Chart(chart)
    
    # 构建数据
    data: Dict[str, Any] = {
        'title': title,
        'chart': chart.json(),
        'difficulty': difficulty,
        'lifetime': lifetime,
    }
    if hidden:
        data['hidden'] = True
    
    # 准备文件
    file = open(bgm, 'rb')
    files = {'bgm': (bgm_name, file, guess_type(bgm)[0])}
    
    # 发送请求
    response = await Api(API['levels']['post']).apost(data=data, files=files)
    file.close()
    if (uid := response.json().get('uid', None)) is None:
        raise ValueError(f"Unable to get `uid` from response: {response.json()}")
    return uid

# Sonolus 测试服谱面获取
def levels_get(uid: int) -> Chart:
    '''Sonolus 测试服谱面获取

    参数:
        uid (int): 测试服 ID

    返回:
        Chart: 谱面
    '''
    response = Api(API['levels']['get'].format(uid=uid)).get()
    return Chart.standardize(response.json())

# 异步 Sonolus 测试服谱面获取
async def levels_get_async(uid: int) -> Chart:
    '''Sonolus 测试服谱面获取

    参数:
        uid (int): 测试服 ID

    返回:
        Chart: 谱面
    '''
    response = await Api(API['levels']['get'].format(uid=uid)).aget()
    return Chart.standardize(response.json())

# Sonolus 测试服谱面信息获取
def levels(uid: int) -> 'Level':
    '''Sonolus 测试服谱面信息获取

    参数:
        uid (int): 测试服 ID

    返回:
        Level: 谱面信息
    '''
    return Api(API['levels']['info'].format(uid=uid)).get().json()

# 异步 Sonolus 测试服谱面信息获取
async def levels_async(uid: int) -> 'Level':
    '''Sonolus 测试服谱面信息获取

    参数:
        uid (int): 测试服 ID

    返回:
        Level: 谱面信息
    '''
    return (await Api(API['levels']['info'].format(uid=uid)).aget()).json()
