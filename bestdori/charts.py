'''`bestdori.charts`

谱面相关操作'''
from copy import deepcopy
from json import dumps, loads
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from .utils import get_api
from .models.note import *
from .utils.network import Api

if TYPE_CHECKING:
    from .user import Me
    from .typing import DifficultyName

API = get_api('bestdori.api')
__NOTE_TYPES__ = ['Long', 'Slide', 'BPM', 'Single', 'Directional']

# 谱面数据类
@dataclass
class Statistics:
    '''谱面数据类

    参数:
        time (float): 谱面时长
        notes (int): 谱面音符总数
        bpm (List[float]): 谱面 BPM 范围
        main_bpm (float): 谱面主 BPM
    '''
    
    time: float
    '''谱面时长'''
    notes: int
    '''谱面音符总数'''
    bpm: List[float]
    '''谱面 BPM 范围'''
    main_bpm: float
    '''谱面主 BPM'''

# 谱面类
class Chart(List[BasicNote]):
    '''谱面类，统合针对谱面的一层操作

    参数:
        chart (List[Dict[str, Any]]): 原始谱面代码'''
    # 初始化
    def __init__(self, chart: List[Dict[str, Any]]) -> None:
        '''谱面类，统合针对谱面的一层操作

        参数:
            chart (List[Dict[str, Any]]): 原始谱面代码'''
        super().__init__()
        self._construct(chart)
        return
    
    def _construct(self, data: List[Dict[str, Any]]) -> None:
        for note in data:
            if note['type'] not in __NOTE_TYPES__:
                continue
            if note['type'] in ['Long', 'Slide']:
                self.append(Slide(**note))
            elif note['type'] == 'BPM':
                self.append(BPM(**note))
            elif note['type'] == 'Single':
                self.append(Single(**note))
            elif note['type'] == 'Directional':
                self.append(Directional(**note))
            else:
                continue
    
    # 检查是否为 SP 谱面
    @property
    def is_sp_rhythm(self) -> bool:
        '''是否为使用了 SP 键的谱面'''
        for note in self:
            if isinstance(note, Slide):
                for connection in note.connections:
                    if connection.hidden:
                        return True
            elif isinstance(note, Directional):
                return True
        return False
    
    # 谱面规范化处理
    def standardize(self) -> 'Chart':
        '''谱面规范化处理

        返回:
            Chart: 处理后谱面
        '''
        standard_chart = self.copy()
        # 对谱面进行排序
        standard_chart.sort(key=lambda x: x.beat)
        # 处理可能出现的 BPM 错位
        if not isinstance(standard_chart[0], BPM):
            offset: float = 0.0 # 记录 offset 修正
            # 第一位不是 BPM，找寻真正的 BPM 线
            for note in standard_chart:
                if isinstance(note, BPM):
                    offset = note.beat
                    break
            if offset < 0: # 没有找到 BPM
                raise ValueError('Unable to find the first BPM note.')
            # 对谱面节拍进行修正
            for note in standard_chart:
                note.move(-offset)
                if isinstance(note, Slide):
                    for connection in note.connections:
                        if connection.beat < 0:
                            connection.beat = 0
                        else:
                            break
                else:
                    if note.beat < 0:
                        note.beat = 0
                    else:
                        break
        
        # 处理可能出现的不合法滑条节点
        for note in standard_chart:
            if not isinstance(note, Slide):
                continue
            
            for connection in note.connections:
                if connection.next is not None:
                    if connection.flick:
                        connection.flick = False
                    if connection.prev is not None:
                        if connection.skill:
                            connection.skill = False
        
        # 对谱面节拍进行修正
        if standard_chart[0].beat != 0:
            offset = standard_chart[0].beat
            for note in standard_chart:
                note.move(-offset)
        return standard_chart
    
    def __flatten__(self) -> List[BasicNote]:
        '''将谱面扁平化处理'''
        flattened_chart = Chart([])
        for note in self:
            if isinstance(note, Slide):
                for connection in note.connections:
                    flattened_chart.append(connection)
            else:
                flattened_chart.append(note)
        return sorted(flattened_chart, key=lambda x: x.beat)
    
    # 谱面数据统计
    def count(self) -> Statistics:
        '''谱面数据统计

        返回:
            Statistics: 统计到的谱面详细数据
        '''
        # 初始化统计数据
        duration: float = 0 # 谱面时长
        total_notes: int = 0 # 音符总数
        bpm_list: List[float] = [] # BPM 列表
        bpm_main: float = 0 # 主 BPM
        
        # 临时变量
        _started: bool = False
        _bpm_info_list: List[Dict[str, float]] = []
        _bpm_dict: Dict[float, float] = {}
        _prev_bpm: float = 0
        _prev_bpm_beat: float = 0
        
        # 谱面扁平化处理
        _flattened_chart = self.__flatten__()
        # 遍历谱面
        for note in _flattened_chart:
            # 谱面时长计算仅处理一般情况下会遇到的情况
            # 可能存在但并未考虑到的情况有：
            # - 首 BPM 为负或中途出现负数时间轴（该情况下只有实际 beat > 0 的谱面才会被渲染，但未被渲染的 note 仍然存在，且可以被上传）
            # - 最后一个实际 note 出现后出现 BPM 线（该情况下此 BPM 实际并不应该被算作谱面，但并未找到合适的方法来规避掉）
            # - 负 BPM 与正 BPM 错位交接带来的时长计算问题
            
            # BPM 处理
            if isinstance(note, BPM):
                if _prev_bpm != 0 and _started: # BPM 不可能为 0
                    _duration = (note.beat - _prev_bpm_beat) / _prev_bpm * 60
                    if _prev_bpm > 0:
                        if _bpm_info_list and _bpm_info_list[-1]['bpm'] == _prev_bpm:
                            _bpm_info_list[-1]['duration'] += _duration
                        else:
                            _bpm_info_list.append({
                                'bpm': _prev_bpm,
                                'duration': _duration
                            })
                    else:
                        while _duration < 0:
                            if _bpm_info_list:
                                if _bpm_info_list[-1]['duration'] + _duration < 0:
                                    _duration += _bpm_info_list[-1]['duration']
                                    _bpm_info_list.pop()
                                else:
                                    _bpm_info_list[-1]['duration'] += _duration
                                    _duration = 0
                            else:
                                _duration = 0
                
                _prev_bpm = note.bpm
                _prev_bpm_beat = note.beat
            
            else:
                # 音符处理
                if not _started:
                    _prev_bpm_beat = note.beat
                    _started = True
                
                if isinstance(note, Connection) and note.hidden:
                    # 忽略隐藏滑条节点
                    continue
                
                total_notes += 1
        
        if not isinstance(_flattened_chart[-1], BPM):
            _duration = (_flattened_chart[-1].beat - _prev_bpm_beat) / _prev_bpm * 60
            if _bpm_info_list and _bpm_info_list[-1]['bpm'] == _prev_bpm:
                _bpm_info_list[-1]['duration'] += _duration
            else:
                _bpm_info_list.append({
                    'bpm': _prev_bpm,
                    'duration': _duration
                })
        
        for _bpm_info in _bpm_info_list:
            if _bpm_info['bpm'] not in bpm_list:
                bpm_list.append(_bpm_info['bpm'])
            duration += _bpm_info['duration']
            if _bpm_dict.get(_bpm_info['bpm']) is None:
                _bpm_dict[_bpm_info['bpm']] = 0
            _bpm_dict[_bpm_info['bpm']] += _bpm_info['duration']
        
        bpm_main = max(_bpm_dict, key=lambda bpm: _bpm_dict[bpm])
        
        return Statistics(
            duration,
            total_notes,
            bpm_list,
            bpm_main
        )

    # 转换为字典列表对象
    def to_list(self) -> List[Dict[str, Any]]:
        '''将 `Chart` 谱面转换为 `List[Dict[str, Any]]` 对象'''
        chart_data: List[Dict[str, Any]] = []
        for note in self:
            chart_data.append(note.to_dict())
        return chart_data
    
    # 转换为 json 字符串
    def json(self) -> str:
        '''将 `Chart` 谱面转换为 `json` 字符串'''
        return dumps(self.to_list(), ensure_ascii=False)

    @classmethod
    def from_python(cls, data: List[Dict[str, Any]]) -> 'Chart':
        '''通过 `List[Note]` 谱面转换为 `Chart` 谱面

        参数:
            data (List[Dict[str, Any]]): 谱面字典列表

        返回:
            Chart: 谱面对象 `bestdori.chart.Chart`
        '''
        return cls(data).standardize()

    # 通过 json 字符串转换为 Chart 谱面
    @classmethod
    def from_json(cls, data: str) -> 'Chart':
        '''通过 `json` 字符串转换为 `Chart` 谱面

        参数:
            data (str): 谱面 `json` 字符串

        返回:
            Chart: 谱面对象 `bestdori.chart.Chart`
        '''
        return cls(loads(data)).standardize()
    
    # 获取官方谱面
    @classmethod
    def get_chart(
        cls,
        id: int,
        diff: 'DifficultyName' = 'expert',
        *,
        me: Optional['Me'] = None
    ) -> 'Chart':
        '''获取官方谱面

        参数:
            id (int): 谱面 ID
            diff (DifficultyName, optional): 难度名称

        返回:
            Chart: 获取到的谱面对象 `bestdori.chart.Chart`
        '''
        response = Api(API['charts']['info'].format(id=id, diff=diff)).get(
            cookies=me.__get_cookies__() if me else None,
        )
        return cls(response.json()).standardize()
    
    # 异步获取官方谱面
    @classmethod
    async def get_chart_async(
        cls,
        id: int,
        diff: 'DifficultyName' = 'expert',
        *,
        me: Optional['Me'] = None
    ) -> 'Chart':
        '''获取官方谱面

        参数:
            id (int): 谱面 ID
            diff (DifficultyName, optional): 难度名称

        返回:
            Chart: 获取到的谱面对象 `bestdori.chart.Chart`
        '''
        response = await Api(API['charts']['info'].format(id=id, diff=diff)).aget(
            cookies=await me.__get_cookies_async__() if me else None,
        )
        return cls(response.json()).standardize()
    
    def copy(self) -> 'Chart':
        return deepcopy(self)
