'''`bestdori.utils.note`

谱面音符相关模块'''
from dataclasses import dataclass, field
from typing import Dict, List, Type, Union, Literal, ClassVar, TypeAlias

@dataclass(kw_only=True)
class Connection:
    '''节点音符'''
    beat: float
    lane: float
    flick: bool = False
    skill: bool = False
    hidden: bool = False

@dataclass(kw_only=True)
class _Note:
    type: Literal['Single', 'Slide', 'Long', 'BPM', 'Directional']

@dataclass(kw_only=True)
class Single(_Note):
    beat: float
    lane: float
    flick: bool = False
    skill: bool = False
    hidden: bool = False

@dataclass(kw_only=True)
class Slide(_Note):
    connections: List[Connection] = field(default_factory=list)

@dataclass(kw_only=True)
class BPM(_Note):
    beat: float
    bpm: float

@dataclass(kw_only=True)
class Directional(_Note):
    beat: float
    lane: float
    direction: Literal['Left', 'Right']

Note: TypeAlias = Union[Single, Slide, BPM, Directional]
FlattenedNote: TypeAlias = Union[Single, Connection, BPM, Directional]

NOTE_TYPE: Dict[str, Type[Note]] = {
    'Single': Single,
    'Slide': Slide,
    'Long': Slide,
    'BPM': BPM,
    'Directional': Directional,
}
