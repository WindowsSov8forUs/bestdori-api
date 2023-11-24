'''`bestdori.utils.note`

谱面音符相关模块'''
from typing import Literal, Any
from typing_extensions import override

# 谱面音符类
class NoteType:
    '''谱面音符类'''
    type_: str
    '''音符类型'''
    beat: float
    '''节拍数'''
    # 初始化
    def __init__(self, **values) -> None:
        '''初始化'''
        for key, value in values.items():
            if key == 'type':
                continue
            setattr(self, key, value)
        return
    
    # 节拍数增减
    def beat_move(self, beat: float) -> None:
        '''节拍数增减

        参数:
            beat (float): 移动的节拍数
        '''
        self.beat += beat

# 滑条节点
class Connection:
    '''滑条节点类

    参数:
        beat (float): 节拍数
        
        lane (int): 轨道数
        
        hidden (bool, optional): 是否隐藏'''
    beat: float
    '''节拍数'''
    lane: int
    '''轨道数'''
    hidden: bool = False
    '''是否隐藏'''
    flick: bool = False
    '''是否为滑键'''
    skill: bool = False
    '''是否为技能键'''
    # 初始化
    def __init__(self, **values) -> None:
        '''初始化'''
        for key, value in values.items():
            setattr(self, key, value)
        return
    
    # 字典化
    @property
    def __dict__(self) -> dict[str, Any]:
        '''字典化'''
        note = {'beat': self.beat, 'lane': self.lane}
        if self.hidden:
            note['hidden'] = self.hidden
        if self.flick:
            note['flick'] = self.flick
        if self.skill:
            note['skill'] = self.skill
        return note

# BPM
class BPM(NoteType):
    '''BPM

    参数:
        bpm (float): BPM 值
        
        beat (float): 节拍数'''
    type_: str = 'BPM'
    '''音符类型'''
    bpm: float
    '''BPM 值'''
    # 字典化
    @property
    def __dict__(self) -> dict:
        '''字典化'''
        return {
            'bpm': self.bpm,
            'beat': self.beat,
            'type': self.type_
        }

# 单键
class Single(NoteType):
    '''单键

    参数:
        beat (float): 节拍数
        
        lane (int): 轨道数
        
        flick (bool, optional): 是否为滑键
        
        skill (bool, optional): 是否为技能键'''
    type_: str = 'Single'
    '''音符类型'''
    lane: int
    '''轨道数'''
    flick: bool = False
    '''是否为滑键'''
    skill: bool = False
    '''是否为技能键'''
    # 字典化
    @property
    def __dict__(self) -> dict:
        '''字典化'''
        note = {
            'beat': self.beat,
            'lane': self.lane,
            'type': self.type_
        }
        if self.flick:
            note['flick'] = self.flick
        if self.skill:
            note['skill'] = self.skill
        return note

# 方向滑键
class Directional(NoteType):
    '''方向滑键

    参数:
        beat (float): 节拍数
        
        lane (int): 轨道数
        
        width (int): 滑键宽度
        
        direction (Literal[&#39;Left&#39;, &#39;Right&#39;]): 滑键方向'''
    type_: str = 'Directional'
    '''音符类型'''
    lane: int
    '''轨道数'''
    width: int
    '''滑键宽度'''
    direction: Literal['Left', 'Right']
    '''滑键方向'''
    # 字典化
    @property
    def __dict__(self) -> dict:
        '''字典化'''
        note = {
            'beat': self.beat,
            'lane': self.lane,
            'type': self.type_,
            'width': self.width,
            'direction': self.direction
        }
        return note

# 滑条
class Slide(NoteType):
    '''滑条

    参数:
        connections (list[Connection]): 滑键节点'''
    type_: str = 'Slide'
    '''音符类型'''
    connections: list[Connection]
    '''滑键节点'''
    # 初始化
    def __init__(self, **values) -> None:
        '''初始化'''
        for key, value in values.items():
            if key == 'type':
                continue
            if key == 'connections':
                connections: list[Connection] = []
                # 提取起始节拍数
                self.beat = value[0]['beat']
                
                for connection in value:
                    connections.append(Connection(**connection))
                value = connections
            setattr(self, key, value)
        return
    
    # 字典化
    @property
    def __dict__(self) -> dict:
        '''字典化'''
        note: dict[str, Any] = {
            'type': self.type_
        }
        if self.connections:
            note['connections'] = [connection.__dict__ for connection in self.connections]
        return note
    
    # 节拍数增减
    @override
    def beat_move(self, beat: float) -> None:
        for connection in self.connections:
            connection.beat += beat
        self.beat = self.connections[0].beat
        return

__all__ = [
    'NoteType',
    'BPM',
    'Single',
    'Directional',
    'Slide'
]