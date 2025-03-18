'''`bestdori.ayachan.typing`

Ayachan 类型提示模块'''

from typing_extensions import NotRequired
from typing import List, Literal, TypeAlias, TypedDict

class Version(TypedDict):
    '''API 版本信息'''
    version: str

class ChartDifficultyStandard(TypedDict):
    difficulty: float
    max_screen_nps: float
    total_hps: float
    total_nps: float

class ChartDifficultyExtend(TypedDict):
    finger_max_hps: int
    flick_note_interval: int
    max_speed: int
    note_flick_interval: int

class Distribution(TypedDict):
    hit: List[int]
    note: List[int]

RegularType: TypeAlias = Literal[0, 1, 2]

class NoteCount(TypedDict):
    direction_left: int
    direction_right: int
    flick: int
    single: int
    slide_end: int
    slide_flick: int
    slide_hidden: int
    slide_start: int
    slide_tick: int

class ChartMetricsStandard(TypedDict):
    bpm_high: float
    bpm_low: float
    distribution: Distribution
    irregular: RegularType
    irregular_info: str
    main_bpm: float
    max_screen_nps: float
    note_count: NoteCount
    sp_rhythm: bool
    total_hit_note: int
    total_hps: float
    total_hote: int
    total_nps: float
    total_time: float

class ChartMetricsExtend(TypedDict):
    finger_max_hps: int
    flick_note_interval: int
    left_percent: float
    max_speed: float
    note_flick_interval: int

class ChartMetrics(TypedDict):
    '''谱面分析结果'''
    difficulty: ChartDifficultyStandard
    difficulty_extend: NotRequired[ChartDifficultyExtend]
    metrics: ChartMetricsStandard
    metrics_extend: NotRequired[ChartMetricsExtend]
