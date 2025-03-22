
from typing_extensions import NotRequired
from typing import (
    Any,
    Dict,
    List,
    Union,
    Literal,
    TypeVar,
    Optional,
    TypeAlias,
    TypedDict,
)

_T = TypeVar('_T')

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
    bandName: List[Optional[str]]

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
    prefix: List[Optional[str]]

CardAll3: TypeAlias = Dict[str, CardAll3Info]

class CardStat(TypedDict):
    performance: int
    technique: int
    visual: int

class CardStatEpisode(TypedDict):
    performance: int
    technique: int
    visual: int

class CardStatTraining(TypedDict):
    levelLimit: int
    performance: int
    technique: int
    visual: int

class CardAll5Info(CardAll3Info):
    rarity: CardRarity
    levelLimit: int
    resourceSetName: str
    releasedAt: List[Optional[str]]
    skillId: int
    type: str
    stat: Dict[str, Union[CardStat, List[CardStatEpisode], CardStatTraining]]

CardAll5: TypeAlias = Dict[str, CardAll5Info]

class CardEpisodesEntireCostsEntire(TypedDict):
    resourceId: int
    resourceType: str
    quantity: int
    lbBonus: int

class CardEpisodesEntireCosts(TypedDict):
    entires: List[CardEpisodesEntireCostsEntire]

class CardEpisodesEntireRewardsEntire(TypedDict):
    resourceType: str
    quantity: int
    lbBonus: int

class CardEpisodesEntireRewards(TypedDict):
    entires: List[CardEpisodesEntireRewardsEntire]

class CardEpisodesEntire(TypedDict):
    episodeId: int
    episodeType: str
    situationId: int
    scenarioId: str
    appendPerformance: int
    appendTechnique: int
    appendVisual: int
    releaseLevel: int
    costs: CardEpisodesEntireCosts
    rewards: CardEpisodesEntireRewards
    title: List[Optional[str]]
    characterId: int

class CardEpisodes(TypedDict):
    entires: List[CardEpisodesEntire]

class CardSourceGacha(TypedDict):
    probability: float

class CardSource(TypedDict):
    gacha: Dict[str, CardSourceGacha]

class CardInfo(CardAll5Info):
    '''卡牌信息'''
    sdResourceName: str
    episodes: CardEpisodes
    costumeId: int
    gachaText: List[Optional[str]]
    skillName: List[Optional[str]]
    source: List[Union[CardSource, NoneDict]]

class CharacterAll2Info(TypedDict):
    characterType: str
    characterName: List[Optional[str]]
    nickname: List[Optional[str]]
    bandId: NotRequired[int]
    colorCode: NotRequired[str]

CharacterAll2: TypeAlias = Dict[str, CharacterAll2Info]

class CharacterSeasonCostumeListMapEntireSeasonEntire(TypedDict):
    characterId: int
    basicSeasonId: int
    costumeType: str
    seasonCostumeType: str
    sdAssetBundleName: str
    live2AssetBundleName: str
    seasonType: str

class CharacterSeasonCostumeListMapEntireSeason(TypedDict):
    entires: List[CharacterSeasonCostumeListMapEntireSeasonEntire]

class CharacterSeasonCostumeListMap(TypedDict):
    entires: Dict[str, CharacterSeasonCostumeListMapEntireSeason]

class CharacterAll5Info(CharacterAll2Info):
    firstName: List[Optional[str]]
    lastName: List[Optional[str]]
    seasonCostumeListMap: NotRequired[CharacterSeasonCostumeListMap]

CharacterAll5: TypeAlias = Dict[str, CharacterAll5Info]

class CharacterMain1Info(TypedDict):
    characterType: str
    bandId: int

CharacterMain1: TypeAlias = Dict[str, CharacterMain1Info]

class CharacterMain2Info(CharacterMain1Info):
    characterName: List[Optional[str]]
    nickname: List[Optional[str]]
    colorCode: str

CharacterMain2: TypeAlias = Dict[str, CharacterMain2Info]

class CharacterMain3Info(CharacterMain2Info):
    firstName: List[Optional[str]]
    lastName: List[Optional[str]]

CharacterMain3: TypeAlias = Dict[str, CharacterMain3Info]

class CharacterProfile(TypedDict):
    characterVoice: List[Optional[str]]
    favoriteFood: List[Optional[str]]
    hatedFood: List[Optional[str]]
    hobby: List[Optional[str]]
    selfIntroduction: List[Optional[str]]
    school: List[Optional[str]]
    schoolCls: List[Optional[str]]
    schoolYear: List[Optional[str]]
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
    title: List[Optional[str]]
    subTitle: List[Optional[str]]
    publicStartAt: List[Optional[Union[str, Literal[1]]]]
    characterId: List[int]

ComicsAll5: TypeAlias = Dict[str, ComicInfo]

class CostumesAll5Info(TypedDict):
    characterId: int
    assetBundleName: str
    description: List[Optional[str]]
    publishedAt: List[Optional[str]]

CostumesAll5: TypeAlias = Dict[str, CostumesAll5Info]

class CostumeInfo(CostumesAll5Info):
    '''服装信息'''
    sdResourceName: str
    howToGet: List[Optional[str]]
    cards: List[int]

class EventArchiveInfo(TypedDict):
    '''活动归档信息'''
    cutoff: List[Union[NoneDict, Dict[str, int]]]
    board: List[int]

EventArchiveAll5: TypeAlias = Dict[str, EventArchiveInfo]

class EventsAll1Info(TypedDict):
    eventName: List[Optional[str]]

EventsAll1: TypeAlias = Dict[str, EventsAll1Info]

class EventsAll3Info(EventsAll1Info):
    eventType: str
    assetBundleName: str
    bannerAssetBundleName: str
    startAt: List[Optional[str]]
    endAt: List[Optional[str]]

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
    caption: List[Optional[str]]
    title: List[Optional[str]]
    synopsis: List[Optional[str]]
    releaseConditions: List[Optional[str]]

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
    enableFlag: List[Optional[Literal[True]]]
    publicStartAt: List[Optional[str]]
    publicEndAt: List[Optional[str]]
    distributionStartAt: List[Optional[str]]
    distributionEndAt: List[Optional[str]]
    bgmAssetBundleName: str
    bgmFileName: str
    aggregateEndAt: List[Optional[str]]
    exchangeEndAt: List[Optional[str]]
    pointRewards: List[Optional[List[EventPointReward]]]
    rankingRewards: List[Optional[List[EventRankingReward]]]
    stories: List[EventStory]
    musics: List[Optional[List[EventMusic]]]

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
    gachaName: List[Optional[str]]

GachaAll1: TypeAlias = Dict[str, GachaAll1Info]

class GachaAll3Info(GachaAll1Info):
    resourceName: str
    bannerAssetBundleName: NotRequired[str]
    publishedAt: List[Optional[str]]
    type: str
    newCards: List[int]

GachaAll3: TypeAlias = Dict[str, GachaAll3Info]

class GachaAll5Info(GachaAll3Info):
    closedAt: List[Optional[str]]

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
    description: List[Optional[str]]
    term: List[Optional[str]]
    newMemberInfo: List[Optional[str]]
    notice: List[Optional[str]]

class GachaInfo(GachaAll5Info):
    '''招募信息'''
    details: List[Optional[Dict[str, GachaDetail]]]
    rates: List[Optional[Dict[str, GachaRate]]]
    paymentMethods: List[GachaPaymentMethod]
    description: List[Optional[str]]
    annotation: List[Optional[str]]
    gachaPeriod: List[Optional[str]]
    information: List[GachaInformation]

class LoginCampaignsAll1Info(TypedDict):
    caption: List[Optional[str]]

LoginCampaignsAll1: TypeAlias = Dict[str, LoginCampaignsAll1Info]

class LoginCampaignsAll5Info(LoginCampaignsAll1Info):
    loginBonusType: str
    assetBundleName: List[str]
    publishedAt: List[Optional[str]]
    closedAt: List[Optional[str]]

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
    assetMap: List[Any]
    details: List[Optional[List[LoginCampaignDetail]]]

class MiracleTicketEnchangeInfo(TypedDict):
    '''自选券兑换信息'''
    name: List[Optional[str]]
    ids: List[Optional[List[int]]]
    exchangeStartAt: List[Optional[str]]
    exchangeEndAt: List[Optional[str]]

MiracleTicketEnchangesAll5: TypeAlias = Dict[str, MiracleTicketEnchangeInfo]

class MissionsAll5Info(TypedDict):
    type: str
    startAt: List[Optional[str]]
    endAt: List[Optional[str]]
    title: List[Optional[str]]

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
    details: List[Optional[List[MissionDetail]]]

class PlayerDataProfileMainDeckUserSituationsEntireUserAppendParameter(TypedDict):
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

class PlayerDataProfileMainDeckUserSituationsEntire(TypedDict):
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
    userAppendParameter: PlayerDataProfileMainDeckUserSituationsEntireUserAppendParameter
    limitBreakRank: int

class PlayerDataProfileMainDeckUserSituations(TypedDict):
    entires: List[PlayerDataProfileMainDeckUserSituationsEntire]

class PlayerDataProfileEnabledUserAreaItemsEntire(TypedDict):
    userId: str
    areaItemId: int
    areaItemCategory: int
    level: int

class PlayerDataProfileEnabledUserAreaItems(TypedDict):
    entires: List[PlayerDataProfileEnabledUserAreaItemsEntire]

class PlayerDataProfileBandRankMap(TypedDict):
    entires: Dict[str, int]

class PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicListEntire(TypedDict):
    musicId: int
    difficulty: DifficultyName
    rating: int

class PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicList(TypedDict):
    entires: List[PlayerDataProfileUserHighScoreRatingUserBandHighScoreMusicListEntire]

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

class PlayerDataProfileUserProfileDegreeMapEntire(TypedDict):
    userId: str
    profileDegreeType: str
    degreeId: int

class PlayerDataProfileUserProfileDegreeMap(TypedDict):
    entires: Dict[str, PlayerDataProfileUserProfileDegreeMapEntire]

class PlayerDataProfileUserTwitter(TypedDict):
    twitterId: str
    twitterName: str
    screenName: str
    url: str
    profileImageUrl: str

class PlayerDataProfileUserDeckTotalRatingMapEntire(TypedDict):
    rank: str
    score: int
    level: int
    lowerRating: int
    upperRating: int

class PlayerDataProfileUserDeckTotalRatingMap(TypedDict):
    entires: Dict[str, PlayerDataProfileUserDeckTotalRatingMapEntire]

class PlayerDataProfileStageChallengeAchievementConditionsMap(TypedDict):
    entires: Dict[str, int]

class PlayerDataProfileUserMusicClearInfoMapEntire(TypedDict):
    clearedMusicCount: int
    fullComboMusicCount: int
    allPerfectMusicCount: int

class PlayerDataProfileUserMusicClearInfoMap(TypedDict):
    entires: Dict[DifficultyName, PlayerDataProfileUserMusicClearInfoMapEntire]

class PlayerDataProfileUserCharacterRankMapEntire(TypedDict):
    rank: int
    exp: str
    addExp: str
    nextExp: str
    totalExp: str
    releasedPotentialLevel: str

class PlayerDataProfileUserCharacterRankMap(TypedDict):
    entires: Dict[str, PlayerDataProfileUserCharacterRankMapEntire]

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
    posts: List
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
    musicTitle: List[Optional[str]]

SongsAll1: TypeAlias = Dict[str, SongsAll1Info]

class SongsAll5Difficulty(TypedDict):
    playLevel: int
    publishedAt: NotRequired[List[Optional[str]]]

class SongsAll5Info(SongsAll1Info):
    tag: str
    bandId: int
    jacketImage: List[str]
    publishedAt: List[Optional[str]]
    closedAt: List[Optional[str]]
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
    ruby: List[Optional[str]]
    phonetic: List[Optional[str]]
    lyricist: List[Optional[str]]
    composer: List[Optional[str]]
    arranger: List[Optional[str]]

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
    publishedAt: NotRequired[List[Optional[str]]]

class SongInfo(SongsAll8Info):
    '''歌曲信息'''
    bgmId: str
    bgmFile: str
    achievements: List[SongAchievement]
    seq: int
    howToGet: List[Optional[str]]
    description: List[Optional[str]]
    difficulty: Dict[_DifficultyString, SongDifficulty]

class StampInfo(TypedDict):
    imageName: str

StampsAll2: TypeAlias = Dict[str, StampInfo]

class SkillsAll2Info(TypedDict):
    simpleDescription: List[Optional[str]]

SkillsAll2: TypeAlias = Dict[str, SkillsAll2Info]

class SkillsAll5Info(SkillsAll2Info):
    description: List[Optional[str]]
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
