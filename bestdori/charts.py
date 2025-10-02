'''`bestdori.charts`

谱面相关操作'''
from copy import deepcopy
from json import dumps, loads
from dataclasses import asdict, dataclass
from typing import TYPE_CHECKING, Any, Set, Dict, List, Optional, TypedDict

from .utils import get_api
from .models.note import *
from .utils.network import Api

if TYPE_CHECKING:
    from .user import Me
    from .typing import DifficultyName

API = get_api('bestdori.api')

class _BPMDuration(TypedDict):
    bpm: float
    duration: float

def _get_note_beat(note: Note) -> float:
    if isinstance(note, Slide):
        if note.connections:
            return note.connections[0].beat
        return float('inf')
    return getattr(note, 'beat', float('inf'))

def _handle_bpm_duration(duration: float, prev_bpm: float, bpm_duration_stack: List[_BPMDuration]):
    while duration > 0.0:
        if len(bpm_duration_stack) <= 0:
            bpm_dur = _BPMDuration(bpm=prev_bpm, duration=duration)
            bpm_duration_stack.append(bpm_dur)
            break
        else:
            top = bpm_duration_stack[-1]
            if (top['bpm'] > 0.0 and prev_bpm > 0.0) or (top['bpm'] < 0.0 and prev_bpm < 0.0):
                # 同向 BPM 时长不相减
                if top['bpm'] == prev_bpm:
                    top['duration'] += duration
                else:
                    bpm_dur = _BPMDuration(bpm=prev_bpm, duration=duration)
                    bpm_duration_stack.append(bpm_dur)
                break
            else:
                # 反向 BPM 时长相减
                if top['duration'] >= duration:
                    top['duration'] -= duration
                    if top['duration'] <= 0.0:
                        bpm_duration_stack.pop()
                    break
                else:
                    duration -= top['duration']
                    bpm_duration_stack.pop()

# 谱面数据类
@dataclass
class Stats:
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
    bpms: List[float]
    '''谱面 BPM 范围'''
    main_bpm: float
    '''谱面主 BPM'''

# 谱面类
class Chart(List[Note]):
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
            NoteType = NOTE_TYPE.get(note.get('type', ''), None)
            if NoteType is None:
                continue
            self.append(NoteType(**note))
    
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
        # 对谱面进行排序
        self.sort(key=lambda x: _get_note_beat(x))
        
        # 偏移量计算
        offset: float = 0
        for note in self:
            if isinstance(note, BPM):
                offset = note.bpm
                break
        
        # 规范化处理
        result = Chart([])
        for note in self:
            if isinstance(note, Slide):
                connections = []

                # 统一类型名称
                note.type = 'Slide'
                for index, connection in enumerate(note.connections):
                    # 修正偏移量
                    connection.beat -= offset
                    if connection.beat < 0:
                        connection.beat = 0.0
                    
                    # 修正字段值
                    if index != 0 and index != len(note.connections) - 1:
                        connection.flick = False
                        connection.skill = False
                    
                    connections.append(connection)
                note.connections = connections
            else:
                # 修正偏移量
                note.beat -= offset
                if note.beat < 0:
                    note.beat = 0.0
            
            result.append(note)
        
        return result
    
    def __flatten__(self) -> List[FlattenedNote]:
        '''将谱面扁平化处理'''
        notes: List[FlattenedNote] = []
        for note in self:
            if isinstance(note, Slide):
                for connection in note.connections:
                    notes.append(connection)
            else:
                notes.append(note)
        
        # 按节拍排序
        notes.sort(key=lambda x: x.beat)

        # 清理后跟 BPM 音符
        while notes and isinstance(notes[-1], BPM):
            notes.pop()
        
        return notes
    
    # 谱面数据统计
    def count(self) -> Stats:
        '''谱面数据统计

        返回:
            Stats: 统计到的谱面详细数据
        '''
        stats = Stats(
            time=0.0,
            notes=0,
            bpms=[],
            main_bpm=0.0
        )

        # 扁平化谱面
        notes = self.__flatten__()

        bpm_duration_stack: List[_BPMDuration] = []
        prev_beat = 0.0
        prev_bpm = 0.0
        bpms: Set[float] = set()
        # 再次遍历音符列表进行统计
        for note in notes:
            if isinstance(note, BPM):
                if prev_bpm != 0.0:
                    # bpm_duration_stack 为空与 prev_bpm == 0.0 必定同时成立
                    duration = (note.beat - prev_beat) * 60.0 / abs(prev_bpm)
                    _handle_bpm_duration(duration, prev_bpm, bpm_duration_stack)
                
                prev_bpm = note.bpm
                prev_beat = note.beat
                if prev_bpm > 0.0 and prev_bpm not in bpms:
                    bpms.add(prev_bpm)
                    stats.bpms.append(prev_bpm)
            else:
                if not isinstance(note, Connection) or not note.hidden:
                    stats.notes += 1
        
        # 处理收尾 BPM 时长
        if prev_bpm != 0.0 and prev_beat != 0.0:
            duration = (notes[-1].beat - prev_beat) * 60.0 / abs(prev_bpm)
            _handle_bpm_duration(duration, prev_bpm, bpm_duration_stack)
            if duration > 0.0 and prev_bpm > 0.0 and prev_bpm not in bpms:
                bpms.add(prev_bpm)
                stats.bpms.append(prev_bpm)
        
        # 处理 BPM 计算栈计算谱面时长与 BPM 时长统计
        bpm_time_dict: Dict[float, float] = {}
        total_time = 0.0
        for bpm_dur in bpm_duration_stack:
            total_time += bpm_dur['duration']
            if bpm_dur['bpm'] in bpm_time_dict:
                bpm_time_dict[bpm_dur['bpm']] += bpm_dur['duration']
            else:
                bpm_time_dict[bpm_dur['bpm']] = bpm_dur['duration']
        stats.time = total_time

        # 计算主 BPM
        main_duration = 0.0
        for bpm, duration in bpm_time_dict.items():
            if duration > main_duration:
                main_duration = duration
                stats.main_bpm = bpm
        
        return stats

    # 转换为字典列表对象
    def to_list(self) -> List[Dict[str, Any]]:
        '''将 `Chart` 谱面转换为 `List[Dict[str, Any]]` 对象'''
        chart_data: List[Dict[str, Any]] = []
        for note in self:
            chart_data.append(asdict(note))
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
        response = Api(API['charts']['info'].format(id=id, diff=diff)).get()
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
        response = await Api(API['charts']['info'].format(id=id, diff=diff)).aget()
        return cls(response.json()).standardize()
    
    def copy(self) -> 'Chart':
        """返回当前谱面的深拷贝副本"""
        new_chart = Chart([])
        new_chart.extend(deepcopy(self))
        return new_chart

    def __copy__(self):
        new_chart = Chart([])
        new_chart.extend(self)
        return new_chart

    def __deepcopy__(self, memo):
        new_chart = Chart([])
        new_chart.extend(deepcopy(list(self), memo))
        return new_chart
