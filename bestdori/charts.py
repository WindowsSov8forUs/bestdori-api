'''`bestdori.charts`

谱面相关操作'''
from json import dumps, loads
from typing import Any, Literal

from .utils.note import *
from .utils.utils import API
from .utils.network import Api

# 谱面数据类
class Statistics:
    '''谱面数据类

    参数:
        time (float): 谱面时长
        notes (int): 谱面音符总数
        bpm (list[float]): 谱面 BPM 范围
        main_bpm (float): 谱面主 BPM
    '''
    # 初始化
    def __init__(self, time: float, notes: int, bpm: list[float], main_bpm: float) -> None:
        '''谱面数据类

        参数:
            time (float): 谱面时长
            notes (int): 谱面音符总数
            bpm (list[float]): 谱面 BPM 范围
            main_bpm (float): 谱面主 BPM
        '''
        self.time: float = time
        '''谱面时长'''
        self.notes: int = notes
        '''谱面音符总数'''
        self.bpm: list[float] = bpm
        '''谱面 BPM 范围'''
        self.main_bpm: float = main_bpm
        '''谱面主 BPM'''
        return

# 谱面类
class Chart(list[NoteType]):
    '''谱面类，统合针对谱面的一层操作

    参数:
        chart (list[dict[str, Any]]): 原始谱面代码'''
    # 初始化
    def __init__(self, chart: list[dict[str, Any]]) -> None:
        '''谱面类，统合针对谱面的一层操作

        参数:
            chart (list[dict[str, Any]]): 原始谱面代码'''
        super().__init__()
        for note in chart:
            # 遍历分类添加
            if note['type'] in ['Long', 'Slide']:
                self.append(Slide(**note))
            elif note['type'] == 'BPM':
                self.append(BPM(**note))
            elif note['type'] == 'Single':
                self.append(Single(**note))
            elif note['type'] == 'Directional':
                self.append(Directional(**note))
            else:
                # 删除其他音符
                continue
        return
    
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
    @classmethod
    def normalize(cls, chart: list[dict[str, Any]]) -> 'Chart':
        '''谱面规范化处理

        参数:
            chart (list[dict[str, Any]]): 待处理谱面

        返回:
            Chart: 处理后谱面
        '''
        normalized_chart: cls = cls(chart)
        # 对谱面进行排序
        normalized_chart.sort(key=lambda x: x.beat)
        # 处理可能出现的 BPM 错位
        if not isinstance(normalized_chart[0], BPM):
            offset: float = -1.0 # 记录 offset 修正
            # 第一位不是 BPM，找寻真正的 BPM 线
            for note in normalized_chart:
                if isinstance(note, BPM):
                    offset = note.beat
                    break
            if offset < 0: # 没有找到 BPM
                raise ValueError('谱面内未找到 BPM 线。')
            # 对谱面节拍进行修正
            for note in normalized_chart:
                note.beat_move(-offset)
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
        for note in normalized_chart:
            if not isinstance(note, Slide):
                continue
            index: int = 0
            for connection in note.connections:
                if index < (len(note.connections) - 1):
                    if connection.flick:
                        connection.flick = False
                if 0 < index < (len(note.connections) - 1):
                    if connection.skill:
                        connection.skill = False
                index += 1
        
        # 对谱面节拍进行修正
        if normalized_chart[0].beat != 0:
            offset = normalized_chart[0].beat
            for note in normalized_chart:
                note.beat_move(-offset)
        return normalized_chart
    
    # 谱面数据统计
    def count(self) -> Statistics:
        '''谱面数据统计

        返回:
            Statistics: 统计到的谱面详细数据
        '''
        # 初始化统计数据
        start_beat = 0.0 # 谱面开始 beat 值
        end_beat = 0.0 # 谱面结束 beat 值
        prev_bpm = 120.0 # 上一个 BPM 线的 BPM 值
        prev_bpm_beat = 0.0 # 上一个 BPM 线的 beat 值
        total_notes = 0 # 总物量
        bpm_list: list[dict[str, float]] = [] # BPM 统计列表，统计所有出现的 BPM 及其有效时间
        
        # 遍历谱面数据
        for note in self:
            # 谱面为一个字典列表，每一个 note 都是一个字典
            if isinstance(note, BPM): # 如果当前是 BPM
                if note.bpm >= 0: # 如果当前 BPM 大于等于 0
                    # 如果不是谱面一开始的 BPM 线且已有 note 被记录（即已出现过有效 bpm ）
                    if note.beat > 0 and total_notes > 0:
                        if prev_bpm_beat <= start_beat: # 如果上一个 BPM 线先于第一个 note
                            prev_bpm_beat = start_beat
                        bpm_duration = (note.beat - prev_bpm_beat) * 60.0 / prev_bpm # 计算持续时间
                        bpm_flag: bool = False # 检测 BPM 表中是否已存在指定 BPM
                        for bpm_dict in bpm_list:
                            if bpm_dict['bpm'] == prev_bpm:
                                bpm_dict['duration'] += bpm_duration
                                bpm_flag = True
                                break
                        if not bpm_flag: # 如果 BPM 未被记录
                            bpm_dict = {
                                'bpm': prev_bpm,
                                'duration': bpm_duration
                            }
                            bpm_list.append(bpm_dict)
                    prev_bpm = note.bpm
                    prev_bpm_beat = note.beat
                continue
            
            if isinstance(note, (Single, Directional)): # 如果当前是单键或方向滑键
                # 记录 beat
                if end_beat < note.beat: # 如果当前 beat 更靠后
                    end_beat = note.beat # 始终记录结束 beat
                if start_beat <= 0 or start_beat > note.beat: # 如果未记录起始 beat 或已记录的并不是起始 beat
                    start_beat = note.beat
                
                total_notes += 1 # 累加一个物量
                continue
            
            if isinstance(note, Slide): # 如果是绿条
                # 绿条将会有一个 `connections` 列表用于记录节点
                for connection in note.connections:
                    if not connection.hidden: # 忽略隐藏节点
                        # 记录 beat
                        if end_beat < connection.beat: # 如果当前 beat 更靠后
                            end_beat = connection.beat # 始终记录结束 beat
                        if start_beat <= 0 or start_beat > connection.beat: # 如果未记录起始 beat 或已记录的并不是起始 beat
                            start_beat = connection.beat
                        
                        total_notes += 1 # 累加一个物量
                continue
                    
        # 当走出遍历后表明谱面已遍历至最后一个 note ，进行最后的处理
        if prev_bpm_beat < end_beat: # 如果最后一个 note 在最后一个 BPM 线之前
            bpm_duration = (end_beat - prev_bpm_beat) * 60.0 / prev_bpm # 计算持续时间
            bpm_flag: bool = False # 检测 BPM 表中是否已存在指定 BPM
            for bpm_dict in bpm_list:
                if bpm_dict['bpm'] == prev_bpm:
                    bpm_dict['duration'] += bpm_duration
                    bpm_flag = True
                    break
            if not bpm_flag: # 如果 BPM 未被记录
                bpm_dict = {
                    'bpm': prev_bpm,
                    'duration': bpm_duration
                }
                bpm_list.append(bpm_dict)
                
        # 遍历 BPM 列表，计算总时长并获取 BPM 数值
        duration = 0.0 # 谱面总持续时长
        bpm_main = 0.0 # 主要 BPM
        bpm_main_dura = 0.0 # 主要 BPM 持续时长
        bpm_min = 2147483647.0 # 最低 BPM
        bpm_max = 0.0 # 最高 BPM
        for bpm_info in bpm_list: # 遍历
            if bpm_info['duration'] > bpm_main_dura: # 如果持续时间更长
                bpm_main_dura = bpm_info['duration']
                bpm_main = bpm_info['bpm']
            if bpm_min > bpm_info['bpm']: # 如果更小
                bpm_min = bpm_info['bpm']
            if bpm_max < bpm_info['bpm']: # 如果更大
                bpm_max = bpm_info['bpm']
            duration += bpm_info['duration'] # 累加持续时长
        
        return Statistics(
            duration,
            total_notes,
            [bpm_min, bpm_max] if bpm_min != bpm_max else [bpm_min],
            bpm_main
        )

    # 转换为字典列表对象
    def to_list(self) -> list[dict[str, Any]]:
        '''将 `Chart` 谱面转换为 `list[dict[str, Any]]` 对象'''
        chart_data: list[dict[str, Any]] = []
        for note in self:
            chart_data.append(note.__dict__)
        return chart_data
    
    # 转换为 json 字符串
    def json(self) -> str:
        '''将 `Chart` 谱面转换为 `json` 字符串'''
        return dumps(self.to_list(), ensure_ascii=False)

    # 通过 json 字符串转换为 Chart 谱面
    @classmethod
    def from_json(cls, data: str) -> 'Chart':
        '''通过 `json` 字符串转换为 `Chart` 谱面

        参数:
            data (str): 谱面 `json` 字符串

        返回:
            Chart: 谱面对象 `bestdori.chart.Chart`
        '''
        return cls(loads(data))
    
    # 获取官方谱面
    @classmethod
    def get_chart(
        cls,
        id_: int,
        diff: Literal['easy', 'normal', 'hard', 'expert', 'special']='expert'
    ) -> 'Chart':
        '''获取官方谱面

        参数:
            id_ (int): 谱面 ID
            diff (Literal[&#39;easy&#39;, &#39;normal&#39;, &#39;hard&#39;, &#39;expert&#39;, &#39;special&#39;], optional): 难度名称

        返回:
            Chart: 获取到的谱面对象 `bestdori.chart.Chart`
        '''
        response = Api(API['charts']['info'].format(id=id_, diff=diff)).request('get')
        return cls.normalize(response.json())
