'''`bestdori.utils.note`

谱面音符相关模块'''

from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Literal, Optional

@dataclass
class Note:
    '''音符基类'''
    type: str
    '''音符类型'''
    beat: float
    '''音符所在节拍值'''
    
    @property
    def __dict__(self) -> Dict[str, Any]:
        '''字典化'''
        return asdict(self)
    
    def move(self, beat: float) -> None:
        '''移动音符'''
        self.beat += beat

@dataclass
class BPM(Note):
    '''BPM 音符'''
    type: Literal['BPM']
    '''音符类型'''
    bpm: float
    '''BPM 值'''

@dataclass
class Single(Note):
    '''单点音符'''
    type: Literal['Single']
    '''音符类型'''
    lane: float
    '''音符所在轨道'''
    flick: bool = False
    '''是否为 flick'''
    skill: bool = False
    '''是否为技能音符'''
    
    @property
    def __dict__(self) -> Dict[str, Any]:
        '''字典化'''
        _dict = asdict(self)
        for key in list(_dict.keys()):
            if _dict[key] is False:
                _dict.pop(key)
        return _dict

@dataclass
class Directional(Note):
    '''方向滑键音符'''
    type: Literal['Directional']
    '''音符类型'''
    lane: float
    '''音符所在轨道'''
    width: Literal[1, 2, 3]
    '''滑键宽度'''
    direction: Literal['Left', 'Right']
    '''滑键方向'''

@dataclass
class Connection(Note):
    '''滑条节点音符'''
    lane: float
    '''音符所在轨道'''
    hidden: bool = False
    '''是否为隐藏音符'''
    flick: bool = False
    '''是否为 flick'''
    skill: bool = False
    '''是否为技能音符'''
    type: Literal['Connection'] = 'Connection'
    '''音符类型'''
    prev: Optional['Connection'] = None
    '''上一个音符'''
    next: Optional['Connection'] = None
    '''下一个音符'''
    
    @property
    def __dict__(self) -> Dict[str, Any]:
        '''字典化'''
        _dict = asdict(self)
        _dict.pop('type')
        for key in list(_dict.keys()):
            if _dict[key] is False:
                _dict.pop(key)
        return _dict

@dataclass
class Slide(Note):
    '''滑条音符'''
    type: Literal['Slide']
    '''音符类型'''
    connections: List[Connection]
    '''滑条节点音符列表'''
    beat: float = 0
    '''音符所在节拍值'''
    
    def __post_init__(self) -> None:
        self.beat = self.connections[0].beat
        for index, connection in enumerate(self.connections):
            if index == 0:
                continue
            connection.prev = self.connections[index - 1]
            self.connections[index - 1].next = connection
    
    @property
    def __dict__(self) -> Dict[str, Any]:
        '''字典化'''
        return {
            'type': self.type,
            'connections': [connection.__dict__ for connection in self.connections],
        }
    
    def move(self, beat: float) -> None:
        '''移动音符'''
        for connection in self.connections:
            connection.move(beat)
        self.beat += beat

__all__ = [
    'Note',
    'BPM',
    'Single',
    'Directional',
    'Connection',
    'Slide',
]