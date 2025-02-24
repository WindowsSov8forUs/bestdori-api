
from typing_extensions import NotRequired
from typing import Any, Dict, List, Union, Literal, Optional, TypeAlias, TypedDict

Server: TypeAlias = Literal[0, 1, 2, 3, 4]
'''服务器 ID

`0`: 日服

`1`: 英服

`2`: 台服

`3`: 国服

`4`: 韩服
'''
ServerName: TypeAlias = Literal['jp', 'en', 'tw', 'cn', 'kr']
'''服务器名称'''
Difficulty: TypeAlias = Literal[0, 1, 2, 3, 4]
'''难度

`0`: Easy

`1`: Normal

`2`: Hard

`3`: Expert

`4`: Special
'''

class NoneDict(TypedDict):
    '''空字典'''
    pass

class PostSongCustom(TypedDict):
    '''帖子自定义歌曲信息'''
    type: Literal['custom']
    audio: str
    cover: str

class PostSongProvided(TypedDict):
    '''bestdori 提供歌曲信息'''
    type: Literal['bandori', 'llsif']
    id: int

class Title(TypedDict):
    '''称号'''
    id: int
    type: str
    server: Server

class PostAuthor(TypedDict):
    '''帖子作者信息'''
    username: str
    nickname: Optional[str]
    titles: Optional[List[Title]]

class PostTag(TypedDict):
    '''帖子标签'''
    type: str
    data: str

class PostInfo(TypedDict):
    '''帖子信息'''
    categoryName: str
    categoryId: str
    title: NotRequired[str]
    song: NotRequired[Union[PostSongCustom, PostSongProvided]]
    artists: NotRequired[str]
    diff: NotRequired[Difficulty]
    level: NotRequired[int]
    chart: NotRequired[List[Dict[str, Any]]]
    content: List[Dict[str, Any]]
    time: float
    author: PostAuthor
    likes: int
    liked: bool
    tags: List[PostTag]

class PostDetail(TypedDict):
    '''帖子详情'''
    result: Literal[True]
    post: PostInfo

class PostBasicAuthor(TypedDict):
    username: str

class PostBasic(TypedDict):
    '''帖子简介'''
    result: Literal[True]
    title: Optional[str]
    author: PostBasicAuthor

class PostListPost(TypedDict):
    id: int
    categoryName: str
    categoryId: str
    title: NotRequired[str]
    song: NotRequired[Union[PostSongCustom, PostSongProvided]]
    artists: NotRequired[str]
    diff: NotRequired[Difficulty]
    level: NotRequired[int]
    time: float
    content: List[Dict[str, Any]]
    author: PostAuthor
    likes: int
    liked: bool
    tags: List[PostTag]

class PostList(TypedDict):
    '''帖子列表'''
    result: Literal[True]
    posts: List
    count: int

class PostTagGetResultTag(TypedDict):
    type: str
    data: str
    count: int

class PostTagGetResult(TypedDict):
    result: Literal[True]
    tags: List[PostTagGetResultTag]

class UserPosterCard(TypedDict):
    '''海报'''
    id: int
    offset: int
    trainedArt: bool

class UserServerId(TypedDict):
    id: int
    server: Server

class UserInfo(TypedDict):
    '''用户信息'''
    result: Literal[True]
    followingCount: int
    followeddByCount: int
    followed: bool
    nickname: str
    titles: List[Title]
    posterCard: UserPosterCard
    selfIntro: str
    serverIds: List[UserServerId]
    socialMedia: str
    favCharacters: List[int]
    favCards: List[int]
    favBands: List[int]
    favSongs: List[int]
    favCostumes: List[int]

class UserMeInfo(TypedDict):
    '''自身用户信息'''
    result: Literal[True]
    username: str
    nickname: str
    titles: List[Title]
    email: str
    messageCount: int

class SongAchievement(TypedDict):
    musicId: int
    achievenemtType: str
    rewardType: str
    quantity: int

class SongDifficultyMultiLiveScoreMap(TypedDict):
    musicId: int
    musicDifficulty: str
    multiLiveDifficultyId: int
    scoreS: int
    scoreA: int
    scoreB: int
    scoreC: int
    multiLiveDifficultyType: str
    scoreSS: int
    scoreSSS: int

class SongDifficulty(TypedDict):
    playLevel: int
    multiLiveScoreMap: Dict[str, SongDifficultyMultiLiveScoreMap]
    notesQuantity: int
    scoreC: int
    scoreB: int
    scoreA: int
    scoreS: int
    scoreSS: int
    publishedAt: NotRequired[List[Optional[str]]]

class SongBPM(TypedDict):
    bpm: float
    start: float
    end: float

class SongInfo(TypedDict):
    '''歌曲信息'''
    bgmId: str
    bgmFile: str
    tag: str
    bandId: int
    achievements: List[SongAchievement]
    jacketImage: List[str]
    seq: int
    musicTitle: List[Optional[str]]
    ruby: List[Optional[str]]
    phonetic: List[Optional[str]]
    lyricist: List[Optional[str]]
    composer: List[Optional[str]]
    arranger: List[Optional[str]]
    howToGet: List[Optional[str]]
    publishedAt: List[Optional[str]]
    closedAt: List[Optional[str]]
    description: List[Optional[str]]
    difficulty: Dict[str, SongDifficulty]
    length: float
    notes: Dict[str, int]
    bpm: Dict[str, List[SongBPM]]

class LLSifDifficulty(TypedDict):
    live_setting_id: int
    difficulty: int
    stage_level: int
    notes_setting_asset: str
    s_rank_combo: int
    available: bool
    ac_flag: int
    swing_flag: int
    five_keys_flag: bool

class LLSifSongInfo(TypedDict):
    '''LLSIF 歌曲信息'''
    name: str
    name_kana: str
    keyword: str
    live_icon_asset: str
    sound_asset: str
    attribute_icon_id: int
    live_time: float
    member_tag: str
    unit_type_id: Optional[int]
    member_filter_cond: int
    min_id: int
    max_id: int
    difficulties: List[LLSifDifficulty]

LLSifMisc: TypeAlias = Dict[str, LLSifSongInfo]
'''LLSIF 信息'''
