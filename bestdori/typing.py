from typing_extensions import NotRequired
from typing import (
    Any,
    Dict,
    List,
    Tuple,
    Union,
    Literal,
    TypeVar,
    Optional,
    TypeAlias,
    TypedDict,
)

_T = TypeVar('_T')

PerServer: TypeAlias = Tuple[_T, _T, _T, _T, _T]
'''服务器相关的五元组'''
Emptiable: TypeAlias = Union[_T, 'NoneDict']
'''可为空字典的某类型'''
PerServerType: TypeAlias = PerServer[Optional[_T]]
'''基础类型的五元组'''
PerServerDict: TypeAlias = PerServer[Emptiable[_T]]
'''字典类型的五元组'''

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
DifficultyName: TypeAlias = Literal['easy', 'normal', 'hard', 'expert', 'special']
'''难度名称'''
_DifficultyString: TypeAlias = Literal['0', '1', '2', '3', '4']

class NoneDict(TypedDict):
    '''空字典'''
    pass

class BandsAll1Info(TypedDict):
    bandName: PerServerType[str]

BandsAll1: TypeAlias = Dict[str, BandsAll1Info]

BandsMain1: TypeAlias = BandsAll1

CardRarity: TypeAlias = Literal[1, 2, 3, 4, 5]
'''卡牌稀有度'''

CardAttribute: TypeAlias = Literal['powerful', 'pure', 'cool', 'happy']
'''卡牌属性'''

class CardAll2Info(TypedDict):
    characterId: int
    attribute: CardAttribute

CardAll2: TypeAlias = Dict[str, CardAll2Info]

class CardAll3Info(CardAll2Info):
    prefix: PerServerType[str]

CardAll3: TypeAlias = Dict[str, CardAll3Info]

class CardStat(TypedDict):
    performance: int
    technique: int
    visual: int

class CardStatTraining(CardStat):
    levelLimit: int

class CardAll5Info(CardAll3Info):
    rarity: CardRarity
    levelLimit: int
    resourceSetName: str
    releasedAt: PerServerType[str]
    skillId: int
    type: str
    stat: Dict[str, Union[CardStat, List[CardStat], CardStatTraining]]

CardAll5: TypeAlias = Dict[str, CardAll5Info]

class CardEpisodesEntryCostsEntry(TypedDict):
    resourceId: int
    resourceType: str
    quantity: int
    lbBonus: int

class CardEpisodesEntryCosts(TypedDict):
    entries: List[CardEpisodesEntryCostsEntry]

class CardEpisodesEntryRewardsEntry(TypedDict):
    resourceType: str
    quantity: int
    lbBonus: int

class CardEpisodesEntryRewards(TypedDict):
    entries: List[CardEpisodesEntryRewardsEntry]

class CardEpisodesEntry(TypedDict):
    episodeId: int
    episodeType: str
    situationId: int
    scenarioId: str
    appendPerformance: int
    appendTechnique: int
    appendVisual: int
    releaseLevel: int
    costs: CardEpisodesEntryCosts
    rewards: CardEpisodesEntryRewards
    title: PerServerType[str]
    characterId: int

class CardEpisodes(TypedDict):
    entries: List[CardEpisodesEntry]

class CardSourceGacha(TypedDict):
    probability: float

class CardSource(TypedDict):
    gacha: Dict[str, CardSourceGacha]

class CardInfo(CardAll5Info):
    '''卡牌信息'''
    sdResourceName: str
    episodes: CardEpisodes
    costumeId: int
    gachaText: PerServerType[str]
    skillName: PerServerType[str]
    source: PerServerDict[CardSource]

class CharacterAll2Info(TypedDict):
    characterType: str
    characterName: PerServerType[str]
    nickname: PerServerType[str]
    bandId: NotRequired[int]
    colorCode: NotRequired[str]

CharacterAll2: TypeAlias = Dict[str, CharacterAll2Info]

class CharacterSeasonCostumeListMapEntrySeasonEntry(TypedDict):
    characterId: int
    basicSeasonId: int
    costumeType: str
    seasonCostumeType: str
    sdAssetBundleName: str
    live2dAssetBundleName: str
    seasonType: str

class CharacterSeasonCostumeListMapEntrySeason(TypedDict):
    entries: List[CharacterSeasonCostumeListMapEntrySeasonEntry]

class CharacterSeasonCostumeListMap(TypedDict):
    entries: Dict[str, CharacterSeasonCostumeListMapEntrySeason]

class CharacterAll5Info(CharacterAll2Info):
    firstName: PerServerType[str]
    lastName: PerServerType[str]
    seasonCostumeListMap: NotRequired[CharacterSeasonCostumeListMap]

CharacterAll5: TypeAlias = Dict[str, CharacterAll5Info]

class CharacterMain1Info(TypedDict):
    characterType: str
    bandId: int

CharacterMain1: TypeAlias = Dict[str, CharacterMain1Info]

class CharacterMain2Info(CharacterMain1Info):
    characterName: PerServerType[str]
    nickname: PerServerType[str]
    colorCode: str

CharacterMain2: TypeAlias = Dict[str, CharacterMain2Info]

class CharacterMain3Info(CharacterMain2Info):
    firstName: PerServerType[str]
    lastName: PerServerType[str]

CharacterMain3: TypeAlias = Dict[str, CharacterMain3Info]

class CharacterProfile(TypedDict):
    characterVoice: PerServerType[str]
    favoriteFood: PerServerType[str]
    hatedFood: PerServerType[str]
    hobby: PerServerType[str]
    selfIntroduction: PerServerType[str]
    school: PerServerType[str]
    schoolCls: PerServerType[str]
    schoolYear: PerServerType[str]
    part: str
    birthday: str
    constellation: str
    height: float

class CharacterInfo(CharacterAll5Info):
    '''角色信息'''
    sdAssetBundleName: str
    defaultCostumeId: NotRequired[int]
    ruby: List[Optional[str]]
    profile: NotRequired[CharacterProfile]

class ComicInfo(TypedDict):
    '''漫画信息'''
    assetBundleName: str
    title: PerServerType[str]
    subTitle: PerServerType[str]
    publicStartAt: PerServerType[Union[str, Literal[1]]]
    characterId: List[int]

ComicsAll5: TypeAlias = Dict[str, ComicInfo]

class CostumesAll5Info(TypedDict):
    characterId: int
    assetBundleName: str
    description: PerServerType[str]
    publishedAt: PerServerType[str]

CostumesAll5: TypeAlias = Dict[str, CostumesAll5Info]

class CostumeInfo(CostumesAll5Info):
    '''服装信息'''
    sdResourceName: str
    howToGet: PerServerType[str]
    cards: List[int]

class EventArchiveInfo(TypedDict):
    '''活动归档信息'''
    cutoff: PerServerDict[Dict[str, int]]
    board: List[List[int]]

EventArchiveAll5: TypeAlias = Dict[str, EventArchiveInfo]

class EventsAll1Info(TypedDict):
    eventName: PerServerType[str]

EventsAll1: TypeAlias = Dict[str, EventsAll1Info]

class EventsAll3Info(EventsAll1Info):
    eventType: str
    assetBundleName: str
    bannerAssetBundleName: str
    startAt: PerServerType[str]
    endAt: PerServerType[str]

EventsAll3: TypeAlias = Dict[str, EventsAll3Info]

class EventsAll4Info(EventsAll3Info):
    rewardCards: List[int]

EventsAll4: TypeAlias = Dict[str, EventsAll4Info]

class EventAttribute(TypedDict):
    eventId: NotRequired[int]
    attribute: str
    percent: int

class EventCharacter(TypedDict):
    eventId: NotRequired[int]
    characterId: int
    percent: int
    seq: NotRequired[int]

class EventAttributeAndCharacterBonus(TypedDict):
    eventId: NotRequired[int]
    pointPercent: int
    parameterPercent: int

class EventCharacterParameterBonus(TypedDict):
    eventId: NotRequired[int]
    performance: int
    technique: int
    visual: int

class EventMember(TypedDict):
    eventId: int
    situationId: int
    percent: int
    seq: int

class EventLimitBreak(TypedDict):
    rarity: int
    rank: int
    percent: float

class EventsAll5Info(EventsAll4Info):
    attributes: List[EventAttribute]
    characters: List[EventCharacter]
    eventAttributeAndCharacterBonus: NotRequired[EventAttributeAndCharacterBonus]
    eventCharacterParameterBonus: NotRequired[EventCharacterParameterBonus]
    members: List[EventMember]
    limitBreaks: List[EventLimitBreak]

EventsAll5: TypeAlias = Dict[str, EventsAll5Info]

EventsAll6Info = EventsAll5Info

EventsAll6: TypeAlias = Dict[str, EventsAll6Info]

class EventPointReward(TypedDict):
    point: str
    rewardType: str
    rewardId: NotRequired[int]
    rewardQuantity: int

class EventRankingReward(TypedDict):
    fromRank: int
    toRank: int
    rewardType: str
    rewardId: int
    rewardQuantity: int

class EventStoryReward(TypedDict):
    rewardType: str
    rewardId: NotRequired[int]
    rewardQuantity: int

class EventStory(TypedDict):
    scenarioId: str
    coverImage: str
    backgroundImage: str
    releasePt: str
    rewards: List[EventStoryReward]
    caption: PerServerType[str]
    title: PerServerType[str]
    synopsis: PerServerType[str]
    releaseConditions: PerServerType[str]

class EventMusicRankingReward(TypedDict):
    fromRank: int
    toRank: int
    resourceType: str
    resourceId: int
    quantity: int

class EventMusic(TypedDict):
    musicId: int
    musicRankingRewards: List[EventMusicRankingReward]

class EventInfo(EventsAll6Info):
    '''活动信息'''
    enableFlag: PerServerType[Literal[True]]
    publicStartAt: PerServerType[str]
    publicEndAt: PerServerType[str]
    distributionStartAt: PerServerType[str]
    distributionEndAt: PerServerType[str]
    bgmAssetBundleName: str
    bgmFileName: str
    aggregateEndAt: PerServerType[str]
    exchangeEndAt: PerServerType[str]
    pointRewards: PerServerType[List[EventPointReward]]
    rankingRewards: PerServerType[List[EventRankingReward]]
    stories: List[EventStory]
    musics: PerServerType[List[EventMusic]]

class EventTopPoint(TypedDict):
    time: float
    uid: int
    value: int

class EventTopUser(TypedDict):
    uid: int
    name: str
    introduction: str
    rank: int
    sid: int
    strained: int
    degrees: List[int]

class EventTopData(TypedDict):
    '''活动排名信息'''
    points: List[EventTopPoint]
    users: List[EventTopUser]

class EventTrackerRate(TypedDict):
    '''各服务器各活动种类各排名比率'''
    type: str
    server: Server
    tier: int
    rate: Optional[float]

class EventTrackerCutoff(TypedDict):
    time: float
    ep: int

class EventTrackerData(TypedDict):
    '''活动分数线追踪信息'''
    result: Literal[True]
    cutoffs: List[EventTrackerCutoff]

class FestivalRotationMusic(TypedDict):
    '''团队佳节活动歌曲循环数据'''
    musicId: int
    startAt: str
    endAt: str

class FestivalStage(TypedDict):
    '''团队佳节活动舞台数据'''
    type: str
    startAt: str
    endAt: str

class GachaAll1Info(TypedDict):
    gachaName: PerServerType[str]

GachaAll1: TypeAlias = Dict[str, GachaAll1Info]

class GachaAll3Info(GachaAll1Info):
    resourceName: str
    bannerAssetBundleName: NotRequired[str]
    publishedAt: PerServerType[str]
    type: str
    newCards: List[int]

GachaAll3: TypeAlias = Dict[str, GachaAll3Info]

class GachaAll5Info(GachaAll3Info):
    closedAt: PerServerType[str]

GachaAll5: TypeAlias = Dict[str, GachaAll5Info]

class GachaDetail(TypedDict):
    rarityIndex: int
    weight: int
    pickup: bool

class GachaRate(TypedDict):
    rate: float
    weightTotal: int

class GachaPaymentMethod(TypedDict):
    gachaId: int
    paymentMethod: str
    quantity: int
    paymentMethodId: int
    count: int
    behavior: str
    pickup: bool
    costItemQuantity: int
    discountType: int
    ticketId: NotRequired[int]

class GachaInformation(TypedDict):
    description: PerServerType[str]
    term: PerServerType[str]
    newMemberInfo: PerServerType[str]
    notice: PerServerType[str]

class GachaInfo(GachaAll5Info):
    '''招募信息'''
    details: PerServerType[Dict[str, GachaDetail]]
    rates: PerServerType[Dict[str, GachaRate]]
    paymentMethods: List[GachaPaymentMethod]
    description: PerServerType[str]
    annotation: PerServerType[str]
    gachaPeriod: PerServerType[str]
    information: GachaInformation

class LoginCampaignsAll1Info(TypedDict):
    caption: PerServerType[str]

LoginCampaignsAll1: TypeAlias = Dict[str, LoginCampaignsAll1Info]

class LoginCampaignsAll5Info(LoginCampaignsAll1Info):
    loginBonusType: str
    assetBundleName: PerServerType[str]
    publishedAt: PerServerType[str]
    closedAt: PerServerType[str]

LoginCampaignsAll5: TypeAlias = Dict[str, LoginCampaignsAll5Info]

class LoginCampaignDetail(TypedDict):
    loginBonusId: int
    days: int
    resourceType: str
    resourceId: int
    quantity: int
    voiceId: NotRequired[str]
    seq: int
    grantType: str

class LoginCampaignInfo(LoginCampaignsAll5Info):
    '''登录奖励信息'''
    assetMap: Dict[str, Any]
    details: PerServerType[List[LoginCampaignDetail]]

class MiracleTicketExchangeInfo(TypedDict):
    '''自选券兑换信息'''
    name: PerServerType[str]
    ids: PerServerType[List[int]]
    exchangeStartAt: PerServerType[str]
    exchangeEndAt: PerServerType[str]

MiracleTicketExchangesAll5: TypeAlias = Dict[str, MiracleTicketExchangeInfo]

class MissionsAll5Info(TypedDict):
    type: str
    startAt: PerServerType[str]
    endAt: PerServerType[str]
    title: PerServerType[str]

MissionsAll5: TypeAlias = Dict[str, MissionsAll5Info]

class MissionDetailReward(TypedDict):
    missionId: NotRequired[int]
    seq: NotRequired[int]
    missionRewardId: NotRequired[int]
    resourceType: str
    resourceId: int
    quantity: int

class MissionDetail(TypedDict):
    seq: int
    title: str
    description: str
    maxProgress: int
    reward: MissionDetailReward

class MissionInfo(MissionsAll5Info):
    '''任务信息'''
    details: PerServerType[List[MissionDetail]]

class PlayerDataProfileMainDeckUserSituationsEntryUserAppendParameter(TypedDict):
    userId: str
    situationId: int
    performance: int
    technique: int
    visual: int
    characterPotentialPerformance: int
    characterPotentialTechnique: int
    characterPotentialVisual: int
    characterBonusPerformance: int
    characterBonusTechnique: int
    characterBonusVisual: int

class PlayerDataProfileMainDeckUserSituationsEntry(TypedDict):
    userId: str
    situationId: int
    level: int
    exp: int
    createdAt: str
    addExp: int
    trainingStatus: str
    duplicateCount: int
    illust: str
    skillExp: int
    skillLevel: int
    userAppendParameter: PlayerDataProfileMainDeckUserSituationsEntryUserAppendParameter
    limitBreakRank: int

class PlayerDataProfileMainDeckUserSituations(TypedDict):
    entries: List[PlayerDataProfileMainDeckUserSituationsEntry]

class PlayerDataProfileEnabledUserAreaItemsEntry(TypedDict):
    userId: str
    areaItemId: int
    areaItemCategory: int
    level: int

class PlayerDataProfileEnabledUserAreaItems(TypedDict):
    entries: List[PlayerDataProfileEnabledUserAreaItemsEntry]

class PlayerDataProfileBandRankMap(TypedDict):
    entries: Dict[str, int]

class PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicListEntry(TypedDict):
    musicId: int
    difficulty: DifficultyName
    rating: int

class PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList(TypedDict):
    entries: List[PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicListEntry]

class PlayerDataProfileUserHighScoreRating(TypedDict, total=False):
    userPoppinPartyHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userAfterglowHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userPastelPalettesHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userHelloHappyWorldHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userRoseliaHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userOtherHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userMorfonicaHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userRaiseASuilenHighScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList
    userMyGOScoreMusicList: PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList

class PlayerDataProfileMainUserDeck(TypedDict):
    deckId: int
    deckName: str
    leader: int
    member1: int
    member2: int
    member3: int
    member4: int
    deckType: str

class PlayerDataProfileUserProfileSituation(TypedDict):
    userId: str
    situationId: int
    illust: str
    viewProfileSituationStatus: str

class PlayerDataProfileUserProfileDegreeMapEntry(TypedDict):
    userId: str
    profileDegreeType: str
    degreeId: int

class PlayerDataProfileUserProfileDegreeMap(TypedDict):
    entries: Dict[Literal['first', 'second'], PlayerDataProfileUserProfileDegreeMapEntry]

class PlayerDataProfileUserTwitter(TypedDict):
    twitterId: str
    twitterName: str
    screenName: str
    url: str
    profileImageUrl: str

class PlayerDataProfileUserDeckTotalRatingMapEntry(TypedDict):
    rank: str
    score: int
    level: int
    lowerRating: int
    upperRating: int

class PlayerDataProfileUserDeckTotalRatingMap(TypedDict):
    entries: Dict[str, PlayerDataProfileUserDeckTotalRatingMapEntry]

class PlayerDataProfileStageChallengeAchievementConditionsMap(TypedDict):
    entries: Dict[str, int]

class PlayerDataProfileUserMusicClearInfoMapEntry(TypedDict):
    clearedMusicCount: int
    fullComboMusicCount: int
    allPerfectMusicCount: int

class PlayerDataProfileUserMusicClearInfoMap(TypedDict):
    entries: Dict[DifficultyName, PlayerDataProfileUserMusicClearInfoMapEntry]

class PlayerDataProfileUserCharacterRankMapEntry(TypedDict):
    rank: int
    exp: str
    addExp: str
    nextExp: str
    totalExp: str
    releasedPotentialLevel: str

class PlayerDataProfileUserCharacterRankMap(TypedDict):
    entries: Dict[str, PlayerDataProfileUserCharacterRankMapEntry]

class PlayerDataProfile(TypedDict):
    userId: str
    userName: str
    rank: int
    degree: int
    introduction: str
    publishTotalDeckPowerFlg: bool
    publishBandRankFlg: bool
    publishMusicClearedFlg: bool
    publishMusicFullComboFlg: bool
    publishHighScoreRatingFlg: bool
    publishUserIdFlg: bool
    searchableFlg: bool
    publishUpdatedAtFlg: bool
    friendApplicableFlg: bool
    publishMusicAllPerfectFlg: bool
    publishDeckRankFlg: bool
    publishStageChallengeAchievementConditionsFlg: bool
    publishStageChallengeFriendRankingFlg: bool
    publishCharacterRankFlg: bool
    mainDeckUserSituations: PlayerDataProfileMainDeckUserSituations
    enabledUserAreaItems: PlayerDataProfileEnabledUserAreaItems
    bandRankMap: PlayerDataProfileBandRankMap
    userHighScoreRating: PlayerDataProfileUserHighScoreRating
    mainUserDeck: PlayerDataProfileMainUserDeck
    userProfileSituation: PlayerDataProfileUserProfileSituation
    userProfileDegreeMap: PlayerDataProfileUserProfileDegreeMap
    userTwitter: PlayerDataProfileUserTwitter
    userDeckTotalRatingMap: PlayerDataProfileUserDeckTotalRatingMap
    stageChallengeAchievementConditionsMap: PlayerDataProfileStageChallengeAchievementConditionsMap
    userMusicClearInfoMap: PlayerDataProfileUserMusicClearInfoMap
    userCharacterRankMap: PlayerDataProfileUserCharacterRankMap

class PlayerData(TypedDict):
    cache: bool
    time: float
    profile: Optional[PlayerDataProfile]

class PlayerInfo(TypedDict):
    '''玩家信息'''
    result: Literal[True]
    data: PlayerData

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
    posts: List[PostListPost]
    count: int

class PostTagGetResultTag(TypedDict):
    type: str
    data: str
    count: int

class PostTagGetResult(TypedDict):
    result: Literal[True]
    tags: List[PostTagGetResultTag]

_SongsMetaAll: TypeAlias = Dict[
    str,
    Dict[
        _DifficultyString,
        Dict[
            _T,
            List[float]
        ]
    ]
]

SongsMetaAll2 = _SongsMetaAll[Literal['7']]

_SongsMetaAll5Field: TypeAlias = Literal[
    '3', '4', '5', '6', '7', '8',
    '3.5', '4.5', '5.5', '5.6', '5.7', '6.2', '6.4', '6.5', '6.8', '7.2', '7.5',
]

SongsMetaAll5 = _SongsMetaAll[_SongsMetaAll5Field]

class SongsAll1Info(TypedDict):
    musicTitle: PerServerType[str]

SongsAll1: TypeAlias = Dict[str, SongsAll1Info]

class SongsAll5Difficulty(TypedDict):
    playLevel: int
    publishedAt: NotRequired[PerServerType[str]]

class SongsAll5Info(SongsAll1Info):
    tag: str
    bandId: int
    jacketImage: List[str]
    publishedAt: PerServerType[str]
    closedAt: PerServerType[str]
    difficulty: Dict[_DifficultyString, SongsAll5Difficulty]

SongsAll5: TypeAlias = Dict[str, SongsAll5Info]

class SongBPM(TypedDict):
    bpm: float
    start: float
    end: float

class SongsAll7Info(SongsAll5Info):
    length: float
    notes: Dict[_DifficultyString, int]
    bpm: Dict[_DifficultyString, List[SongBPM]]

SongsAll7: TypeAlias = Dict[str, SongsAll7Info]

class SongsAll8Info(SongsAll7Info):
    ruby: PerServerType[str]
    phonetic: PerServerType[str]
    lyricist: PerServerType[str]
    composer: PerServerType[str]
    arranger: PerServerType[str]

SongsAll8: TypeAlias = Dict[str, SongsAll8Info]

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
    publishedAt: NotRequired[PerServerType[str]]

class SongInfo(SongsAll8Info):
    '''歌曲信息'''
    bgmId: str
    bgmFile: str
    achievements: List[SongAchievement]
    seq: int
    howToGet: PerServerType[str]
    description: PerServerType[str]
    difficulty: Dict[_DifficultyString, SongDifficulty]

class StampInfo(TypedDict):
    imageName: str

StampsAll2: TypeAlias = Dict[str, StampInfo]

class SkillsAll2Info(TypedDict):
    simpleDescription: PerServerType[str]

SkillsAll2: TypeAlias = Dict[str, SkillsAll2Info]

class SkillsAll5Info(SkillsAll2Info):
    description: PerServerType[str]
    duration: List[float]

SkillsAll5: TypeAlias = Dict[str, SkillsAll5Info]

class SkillsAll10ActivationEffectTypesScore(TypedDict):
    activateEffectValue: List[int]
    activateEffectValueType: str
    activateCondition: str

class SkillsAll10ActivationEffectTypes(TypedDict):
    score: SkillsAll10ActivationEffectTypesScore

class SkillsAll10ActivationEffect(TypedDict):
    activateEffectTypes: SkillsAll10ActivationEffectTypes

class SkillsAll10Info(SkillsAll5Info):
    activationEffect: SkillsAll10ActivationEffect

SkillsAll10: TypeAlias = Dict[str, SkillsAll10Info]

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
    followedByCount: int
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
