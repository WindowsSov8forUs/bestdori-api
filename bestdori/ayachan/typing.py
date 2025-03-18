'''`bestdori.ayachan.typing`

Ayachan 类型提示模块'''

from typing_extensions import NotRequired
from typing import Any, List, Literal, TypeAlias, TypedDict

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

class LevelItemEngineSkinThumbnail(TypedDict):
    hash: str
    url: str

class LevelItemEngineSkinData(TypedDict):
    hash: str
    url: str

class LevelItemEngineSkinTexture(TypedDict):
    hash: str
    url: str

class LevelItemEngineSkin(TypedDict):
    name: str
    source: str
    version: int
    title: str
    subtitle: str
    author: str
    tags: List[Any]
    thumbnail: LevelItemEngineSkinThumbnail
    data: LevelItemEngineSkinData
    texture: LevelItemEngineSkinTexture

class LevelItemEngineBackgroundThumbnail(TypedDict):
    hash: str
    url: str

class LevelItemEngineBackgroundData(TypedDict):
    hash: str
    url: str

class LevelItemEngineBackgroundImage(TypedDict):
    hash: str
    url: str

class LevelItemEngineBackgroundConfiguration(TypedDict):
    hash: str
    url: str

class LevelItemEngineBackground(TypedDict):
    name: str
    source: str
    version: int
    title: str
    subtitle: str
    author: str
    tags: List[Any]
    thumbnail: LevelItemEngineBackgroundThumbnail
    data: LevelItemEngineBackgroundData
    image: LevelItemEngineBackgroundImage
    configuration: LevelItemEngineBackgroundConfiguration

class LevelItemEngineEffectThumbnail(TypedDict):
    hash: str
    url: str

class LevelItemEngineEffectData(TypedDict):
    hash: str
    url: str

class LevelItemEngineEffectAudio(TypedDict):
    hash: str
    url: str

class LevelItemEngineEffect(TypedDict):
    name: str
    source: str
    version: int
    title: str
    subtitle: str
    author: str
    tags: List[Any]
    thumbnail: LevelItemEngineEffectThumbnail
    data: LevelItemEngineEffectData
    audio: LevelItemEngineEffectAudio

class LevelItemEngineParticleThumbnail(TypedDict):
    hash: str
    url: str

class LevelItemEngineParticleData(TypedDict):
    hash: str
    url: str

class LevelItemEngineParticleTexture(TypedDict):
    hash: str
    url: str

class LevelItemEngineParticle(TypedDict):
    name: str
    source: str
    version: int
    title: str
    subtitle: str
    author: str
    tags: List[Any]
    thumbnail: LevelItemEngineParticleThumbnail
    data: LevelItemEngineParticleData
    texture: LevelItemEngineParticleTexture

class LevelItemEngineThumbnail(TypedDict):
    hash: str
    url: str

class LevelItemEnginePlayData(TypedDict):
    hash: str
    url: str

class LevelItemEngineWatchData(TypedDict):
    hash: str
    url: str

class LevelItemEnginePreviewData(TypedDict):
    hash: str
    url: str

class LevelItemEngineTutorialData(TypedDict):
    hash: str
    url: str

class LevelItemEngineConfiguration(TypedDict):
    hash: str
    url: str

class LevelItemEngine(TypedDict):
    name: str
    source: str
    version: int
    title: str
    subtitle: str
    author: str
    tags: List[str]
    skin: LevelItemEngineSkin
    background: LevelItemEngineBackground
    effect: LevelItemEngineEffect
    particle: LevelItemEngineParticle
    thumbnail: LevelItemEngineThumbnail
    playData: LevelItemEnginePlayData
    watchData: LevelItemEngineWatchData
    previewData: LevelItemEnginePreviewData
    tutorialData: LevelItemEngineTutorialData
    configuration: LevelItemEngineConfiguration

class LevelItemUseSkin(TypedDict):
    useDefault: bool

class LevelItemUseBackground(TypedDict):
    useDefault: bool

class LevelItemUseEffect(TypedDict):
    useDefault: bool

class LevelItemUseParticle(TypedDict):
    useDefault: bool

class LevelItemCover(TypedDict):
    hash: str
    url: str

class LevelItemBgm(TypedDict):
    hash: str
    url: str

class LevelItemData(TypedDict):
    hash: str
    url: str

class LevelItem(TypedDict):
    name: str
    source: str
    version: int
    rating: int
    title: str
    artists: str
    author: str
    tags: List[Any]
    engine: LevelItemEngine
    useSkin: LevelItemUseSkin
    useBackground: LevelItemUseBackground
    useEffect: LevelItemUseEffect
    useParticle: LevelItemUseParticle
    cover: LevelItemCover
    bgm: LevelItemBgm
    data: LevelItemData

class Level(TypedDict):
    '''测试服谱面信息'''
    item: LevelItem
    description: str
    hasCommunity: bool
    leaderboards: List[Any]
    actions: List[Any]
    sections: List[Any]
