# player 玩家

玩家信息获取模块。

```python
from bestdori import player
```

## 类型定义

### Profile 玩家个人信息 {#data-profile}

玩家个人信息字典。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| userId | int | 玩家 ID |
| userName | str | 玩家名称 |
| rank | int | 玩家等级 |
| degree | int | 称号 ID |
| introduction | str | 玩家简介 |
| searchableFlg | bool | 是否允许搜索 |
| friendApplicableFlg | bool | 是否允许好友申请 |
| publishTotalDeckPowerFlg | bool | 是否公开卡组综合值 |
| publishBandRankFlg | bool | 是否公开乐队等级 |
| publishMusicClearedFlg | bool | 是否公开已通关歌曲 |
| publishMusicFullComboFlg | bool | 是否公开已全连歌曲 |
| publishMusicAllPerfectFlg | bool | 是否公开已 AP 歌曲 |
| publishHighScoreRatingFlg | bool | 是否公开分数排名 |
| publishUserIdFlg | bool | 是否公开玩家 ID |
| publishUpdatedAtFlg | bool | 是否公开最后更新时间 |
| publishStageChallengeAchievementConditionsFlg | bool | 是否公开已达成舞台挑战条件 |
| publishStageChallengeFriendRankingFlg | bool | 是否公开舞台挑战好友排名 |
| publishCharacterRankFlg | bool | 是否公开角色等级 |
| enabledUserAreaItems | [EnabledUserAreaItems](#enableduserareaitems) | 玩家区域道具信息 |
| bandRankMap | [BandRankMap](#bandrankmap) | 乐队 ID 与乐队等级的映射 |
| stageChallengeAchievementConditionsMap | [StageChallengeAchievementConditionsMap](#stagechallengeachievementconditionsmap) | 舞台挑战达成状态 |
| mainDeckUserSituations | [MainDeckUserSituations](#data-profile-main-deck-user-situations) | 玩家主场景信息 |
| mainUserDeck | [MainUserDeck](#maindeck) | 玩家主乐队信息 |
| userHighScoreRating | [UserHighScoreRating](#userhighscoerating) | 玩家分数排名信息 |
| userProfileSituation | [UserProfileSituation](#userprofilesituation) | 玩家个人信息场景信息 |
| userProfileDegreeMap | [UserProfileDegreeMap](#userprofiledegreemap) | 玩家个人信息称号 ID 映射 |
| userTwitter | [UserTwitter](#usertwitter) | 玩家 Twitter 信息 |
| userDeckTotalRatingMap | [UserDeckTotalRatingMap](#userdecktotalratingmap) | 玩家乐队综合力评级信息 |
| userMusicClearInfoMap | [UserMusicClearInfoMap](#usermusicclearinfomap) | 玩家歌曲通关信息 |
| userCharacterRankMap | [UserCharacterRankMap](#usercharacterrankmap) | 玩家角色等级信息 |

### EnabledUserAreaItems

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | List[[EnabledUserAreaItemsEntry](#enableduserareaitemsentry)] | 玩家区域道具信息列表 |

### EnabledUserAreaItemsEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| userId | int | 玩家 ID |
| areaItemId | int | 区域道具 ID |
| areaItemCategory | int | 区域道具分类 ID |
| level | int | 区域道具等级 |

### BandRankMap

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | Dict[str, int] | 乐队 ID 与乐队等级的映射 |

### StageChallengeAchievementConditionsMap

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | Dict[str, int] | 舞台挑战 ID 与达成状态映射 |

### MainDeckUserSituations 玩家主场景信息 {#main-deck-user-situations}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | List[[MainDeckUserSituationsEntry](#maindeckusersituationsentry)] | 玩家主场景信息列表 |

### MainDeckUserSituationsEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| userId | int | 玩家 ID |
| situationId | int | 场景 ID |
| level | int | 场景等级 |
| exp | int | 场景经验 |
| createdAt | str | 创建时间 |
| addExp | int | 添加经验 |
| trainingStatus | str | 特训状态 |
| duplicateCount | int | 重复次数 |
| illust | str | 卡面状态 |
| skillExp | int | 技能经验 |
| skillLevel | int | 技能等级 |
| userAppendParameter | [MainDeckUserSituationsEntryUserAppendParameter](#maindeckusersituationsentryuserappendparameter) | 玩家附加数值 |
| limitBreakRank | int | 限界突破等级 |

### MainDeckUserSituationsEntryUserAppendParameter

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| userId | int | 玩家 ID |
| situationId | int | 场景 ID |
| performance | int | 演出数值 |
| technique | int | 技巧数值 |
| visual | int | 视觉数值 |
| characterPotentialPerformance | int | 角色潜力演出数值 |
| characterPotentialTechnique | int | 角色潜力技巧数值 |
| characterPotentialVisual | int | 角色潜力视觉数值 |
| characterBonusPerformance | int | 角色加成演出数值 |
| characterBonusTechnique | int | 角色加成技巧数值 |
| characterBonusVisual | int | 角色加成视觉数值 |

### MainUserDeck

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| deckId | int | 主乐队编队序号 |
| deckName | str | 主乐队名称 |
| deckType | str | 主乐队类型 |
| leader | int | 队长卡牌 ID |
| member1 | int | 成员 1 卡牌 ID |
| member2 | int | 成员 2 卡牌 ID |
| member3 | int | 成员 3 卡牌 ID |
| member4 | int | 成员 4 卡牌 ID |

### UserHighScoreRating

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| userPopppinPartyHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 Poppin'Party 歌曲分数排名列表 |
| userAfterglowHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 Afterglow 歌曲分数排名列表 |
| userPastelPalettesHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 Pastel*Palettes 歌曲分数排名列表 |
| userRoseliaHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 Roselia 歌曲分数排名列表 |
| userHelloHappyWorldHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 Hello, Happy World! 歌曲分数排名列表 |
| userMorfonicaHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 Morfonica 歌曲分数排名列表 |
| userRaiseASuilenHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 Raise A Suilen 歌曲分数排名列表 |
| userMyGOHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家 MyGO!!!!! 歌曲分数排名列表 |
| userOtherHighScoreMusicList | [UserHighScoreRatingUserBandHighScoreMusicList](#userhighscoeratinguserbandhighscoremusiclist) | 玩家其他乐队歌曲分数排名列表 |

### UserHighScoreRatingUserBandHighScoreMusicList

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | List[[UserHighScoreRatingUserBandHighScoreMusicListEntry](#userhighscoeratinguserbandhighscoremusiclistentry)] | 玩家乐队分数排名列表 |

### UserHighScoreRatingUserBandHighScoreMusicListEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| musicId | int | 歌曲 ID |
| difficulty | [DifficultyName](/typing#difficulty-name) | 难度名称 |
| rating | int | 排名 |

### UserProfileSituation

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| userId | int | 玩家 ID |
| situationId | int | 场景 ID |
| illust | str | 卡面状态 |
| viewProfileSituationStatus | str | 个人信息页面场景状态 |

### UserProfileDegreeMap

| 字段名 | 类型 | 描述 |
| :------|:----:|:-----|
| entries | Dict[Literal['first', 'second'], [UserProfileDegreeMapEntry](#userprofiledegreemapentry)] | 个人信息称号 ID 映射 |

### UserProfileDegreeMapEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| userId | int | 玩家 ID |
| profileDegreeType | str | 个人信息称号类型 |
| degreeId | int | 称号 ID |

### UserTwitter

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| twitterId | str | Twitter ID |
| twitterName | str | Twitter 名称 |
| screenName | str | Twitter 昵称 |
| url | str | Twitter 主页链接 |
| profileImageUrl | str | Twitter 头像链接 |

### UserDeckTotalRatingMap

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | Dict[str, [UserDeckTotalRatingMapEntry](#userdecktotalratingmapentry)] | 乐队 ID 与综合力评级信息映射 |

### UserDeckTotalRatingMapEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| rank | int | 评级 |
| score | int | 分数 |
| level | int | 等级 |
| lowerRating | int | 当前评级分数下限 |
| upperRating | int | 当前评级分数上限 |

### UserMusicClearInfoMap

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | Dict[[DifficultyName](/typing#difficulty-name), [UserMusicClearInfoMapEntry](#usermusicclearinfomapentry)] | 难度名称与通关信息映射 |

### UserMusicClearInfoMapEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| clearedMusicCount | int | 已通关歌曲数 |
| fullComboMusicCount | int | 已全连歌曲数 |
| allPerfectMusicCount | int | 已 AP 歌曲数 |

### UserCharacterRankMap

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | Dict[str, [UserCharacterRankMapEntry](#usercharacterrankmapentry)] | 角色 ID 与角色等级映射 |

### UserCharacterRankMapEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| rank | int | 角色等级 |
| exp | int | 角色经验 |
| addExp | int | 添加经验 |
| nextExp | int | 下一级经验 |
| totalExp | int | 总经验 |
| releasedPotentialLevel | int | 已释放潜力等级 |

## class Player() {#player}

玩家数据信息获取类。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 玩家 ID |
| server | [Server](/typing#server-id) | - | 服务器 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

### def get_profile() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| mode | int | - | 获取模式 |

::: details mode 可用参数值

| 值 | 描述 |
|:---|:----|
| `0` | 立即返回缓存数据 |
| `1` | 立即返回缓存数据，同时请求数据更新 |
| `2` | 请求并等待数据更新并返回更新后数据，若耗时过长则返回缓存数据 |
| `3` | 请求并持续等待数据更新，返回更新后数据 |

:::

获取玩家个人信息。

<Badge type="info">返回值:</Badge> [`PlayerDataProfile`](#data-profile)
