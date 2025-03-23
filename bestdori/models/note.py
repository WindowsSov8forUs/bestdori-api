'''`bestdori.utils.note`

谱面音符相关模块'''

from typing_extensions import override
from dataclasses import field, asdict, dataclass
from typing import Any, Dict, List, Literal, Optional, Generator

@dataclass
class BasicNote:
    '''音符基类'''
    
    beat: float
    '''音符所在节拍值'''
    flick: bool
    '''是否为 flick'''
    skill: bool
    '''是否为技能音符'''
    hidden: bool
    '''是否为隐藏音符'''
    lane: float
    '''音符所在轨道'''

    def to_dict(self) -> Dict[str, Any]:
        '''字典化'''
        _dict = {
            'beat': self.beat,
            'lane': self.lane,
        }
        if self.flick:
            _dict['flick'] = self.flick
        if self.skill:
            _dict['skill'] = self.skill
        if self.hidden:
            _dict['hidden'] = self.hidden
        return _dict
    
    def move(self, beat: float) -> None:
        '''移动音符'''
        self.beat += beat

@dataclass
class Note(BasicNote):
    '''音符类'''
    type: str
    '''音符类型'''
    beat: float = field(default=0, init=False)
    '''音符所在节拍值'''
    bpm: Optional[float] = field(default=None, init=False)
    '''BPM 值'''
    connections: Optional[List[BasicNote]] = field(default=None, init=False)
    '''滑条节点音符列表'''
    direction: Optional[Literal['Left', 'Right']] = field(default=None, init=False)
    '''滑键方向'''
    flick: Optional[bool] = field(default=None, init=False)
    '''是否为 flick'''
    skill: Optional[bool] = field(default=None, init=False)
    '''是否为技能音符'''
    hidden: Optional[bool] = field(default=None, init=False)
    '''是否为隐藏音符'''
    lane: Optional[float] = field(default=None, init=False)
    '''音符所在轨道'''
    width: Optional[Literal[1, 2, 3]] = field(default=None, init=False)
    '''滑键宽度'''

    @override
    def to_dict(self) -> Dict[str, Any]:
        '''字典化'''
        return asdict(self)

@dataclass
class BPM(Note):
    '''BPM 音符'''
    type: Literal['BPM'] = field(default='BPM')
    '''音符类型'''
    bpm: float = field(default=120)
    '''BPM 值'''
    beat: float = field(default=0)
    '''音符所在节拍值'''

    @override
    def __init__(
        self,
        *,
        type: Literal['BPM'],
        bpm: float,
        beat: float,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            type=type,
        )

        self.bpm = bpm
        self.beat = beat

@dataclass
class Single(Note):
    '''单点音符'''
    type: Literal['Single'] = field(default='Single')
    '''音符类型'''
    beat: float = field(default=0)
    '''音符所在节拍值'''
    lane: float = field(default=0)
    '''音符所在轨道'''
    flick: bool = field(default=False)
    '''是否为 flick'''
    skill: bool = field(default=False)
    '''是否为技能音符'''

    @override
    def __init__(
        self,
        *,
        type: Literal['Single'],
        beat: float,
        lane: float,
        flick: bool = False,
        skill: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            type=type,
        )
        
        self.beat = beat
        self.lane = lane
        self.flick = flick
        self.skill = skill

@dataclass
class Directional(Note):
    '''方向滑键音符'''
    type: Literal['Directional'] = field(default='Directional')
    '''音符类型'''
    beat: float = field(default=0)
    '''音符所在节拍值'''
    lane: float = field(default=0)
    '''音符所在轨道'''
    width: Literal[1, 2, 3] = field(default=1)
    '''滑键宽度'''
    direction: Literal['Left', 'Right'] = field(default='Left')
    '''滑键方向'''

    @override
    def __init__(
        self,
        *,
        type: Literal['Directional'],
        beat: float,
        lane: float,
        width: Literal[1, 2, 3],
        direction: Literal['Left', 'Right'],
        **kwargs: Any,
    ) -> None:
        super().__init__(
            type=type,
        )

        self.beat = beat
        self.lane = lane
        self.width = width
        self.direction = direction

@dataclass
class Connection(BasicNote):
    '''滑条节点音符'''
    prev: Optional['Connection'] = field(default=None)
    '''上一个滑条节点音符'''
    next: Optional['Connection'] = field(default=None)
    '''下一个滑条节点音符'''

    @override
    def __init__(
        self,
        *,
        beat: float,
        lane: float,
        flick: bool = False,
        skill: bool = False,
        hidden: bool = False,
        **kwargs: Any,
    ) -> None:
        self.beat = beat
        self.lane = lane
        self.flick = flick
        self.skill = skill
        self.hidden = hidden
    
    @override
    def __eq__(self, other: 'Connection') -> bool:
        '''判断是否相等'''
        if self is other:
            return True
        else:
            return (
                self.beat == other.beat and
                self.lane == other.lane and
                self.flick == other.flick and
                self.skill == other.skill and
                self.hidden == other.hidden and
                self.prev == other.prev and
                self.next == other.next
            )

@dataclass
class Slide(Note):
    '''滑条音符'''
    type: Literal['Slide'] = field(default='Slide')
    '''音符类型'''
    head: Optional[Connection] = field(default=None, init=False)
    '''滑条头节点'''
    tail: Optional[Connection] = field(default=None, init=False)
    '''滑条尾节点'''

    @override
    def __init__(
        self,
        *,
        type: Literal['Slide', 'Long'],
        connections: List[Dict[str, Any]],
        **kwargs: Any,
    ) -> None:
        type = 'Slide' if type == 'Long' else type
        super().__init__(
            type=type,
        )

        for connection in connections:
            self.append(**connection)
    
    def __iter__(self) -> Generator[Connection, None, None]:
        '''迭代器'''
        current = self.head
        while current:
            yield current
            current = current.next
    
    @property
    def connections(self) -> List[Connection]:
        '''滑条节点音符列表'''
        return list(self)

    @property
    def beat(self) -> float:
        '''音符所在节拍值'''
        return self.head.beat if self.head else 0

    @beat.setter
    def beat(self, value: float) -> None:
        '''设置音符所在节拍值'''
        move = value - self.beat
        self.move(move)

    def append(self, **kwargs: Any) -> None:
        '''添加滑条节点音符到尾部'''
        connection = Connection(**kwargs)

        if not self.head or not self.tail:
            self.head = connection
            self.tail = connection
        else:
            self.tail.next = connection
            connection.prev = self.tail
            self.tail = connection
    
    def prepend(self, **kwargs: Any) -> None:
        '''添加滑条节点音符到头部'''
        connection = Connection(**kwargs)
        connection.next = self.head
        self.head = connection
    
    def delete(self, connection: Connection) -> None:
        '''删除滑条节点音符'''
        if not self.head:
            return
        
        if self.head == connection:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next != connection:
            current = current.next
        
        if current.next:
            current.next = current.next.next

    def to_dict(self) -> Dict[str, Any]:
        '''字典化'''
        return {
            'type': self.type,
            'connections': [connection.to_dict() for connection in self],
        }
    
    def move(self, beat: float) -> None:
        '''移动音符'''
        for connection in self:
            connection.move(beat)

__all__ = [
    'BasicNote',
    'Note',
    'BPM',
    'Single',
    'Directional',
    'Connection',
    'Slide',
]
