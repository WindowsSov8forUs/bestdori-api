# events 活动

活动信息获取模块。

```python
from bestdori import events
```

## 类型定义

### EventInfo 活动信息 {#info}

活动详细信息字典。 `all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| eventName | List[str \| None] | 活动名[定长列表](/typing/#fixed-list) |
| eventType | str | 活动类型 |
| assetBundleName | str | 资源库名称 |
| startAt | List[str \| None] | 活动起始时间戳[定长列表](/typing/#fixed-list) |
| endAt | List[str \| None] | 活动终止时间戳[定长列表](/typing/#fixed-list) |
| rewardCards | List[int] | 活动奖励卡牌 ID 列表 |
| attributes | List[[Attribute](./events/#attribute)] | 活动加成属性列表 |
| characters | List[[Character](./events/#character)] | 活动加成角色列表 |
| eventAttributeAndCharacterBonus <Badge type="info">NotRequired</Badge> | [EventAttributeAndCharacterBonus](./events/#eventattributeandcharacterbonus) | 活动属性与角色加成 |
| eventCharacterParameterBonus <Badge type="info">NotRequired</Badge> | [EventCharacterParameterBonus](./events/#eventcharacterparameterbonus) | 活动角色数值加成 |
| members | List[[Member](./events/#member)] | - |
| limitBreaks | List[[LimitBreak](./events/#limitbreak)] | - |
| enableFlag | List[Literal[True] \| None] | 活动是否可用[定长列表](/typing/#fixed-list) |
| publicStartAt | List[str \| None] | 活动公开起始时间戳[定长列表](/typing/#fixed-list) |
| publicEndAt | List[str \| None] | 活动公开终止时间戳[定长列表](/typing/#fixed-list) |
| distributionStartAt | List[str \| None] | 发布起始时间戳[定长列表](/typing/#fixed-list) |
| distributionEndAt | List[str \| None] | 发布结束时间戳[定长列表](/typing/#fixed-list) |
| bgmAssetBundleName | str | BGM 资源库名称 |
| bgmFileName | str | BGM 资源文件名称 |
| aggregateEndAt | List[str \| None] | 结果汇总结束时间戳[定长列表](/typing/#fixed-list) |
| exchangeEndAt | List[str \| None] | 交换所结束时间戳[定长列表](/typing/#fixed-list) |
| pointRewards | List[List[[PointReward](./events/#pointreward)] \| None] | 点数奖励列表[定长列表](/typing/#fixed-list) |
| rankingRewards | List[List[[RankingReward](./events/#rankingreward)] \| None] | 排名奖励列表[定长列表](/typing/#fixed-list) |
| stories | List[[Story](./events/#story)] | 活动故事列表 |
| musics | List[[Music](./events/#music)] | 活动音频列表 |

### Attribute 活动加成属性信息 {#attribute}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| eventId <Badge type="info">NotRequired</Badge> | int | 活动 ID |
| attribute | str | 活动加成属性 |
| percent | int | 加成百分比 |

### Character 活动加成角色信息 {#character}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| eventId <Badge type="info">NotRequired</Badge> | int | 活动 ID |
| characterId | int | 活动加成角色 ID |
| percent | int | 加成百分比 |
| seq <Badge type="info">NotRequired</Badge> | int | - |

### EventAttributeAndCharacterBonus

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| eventId <Badge type="info">NotRequired</Badge> | int | 活动 ID |
| pointPercent | int | - |
| parameterPercent | int | - |

### EventCharacterParameterBonus

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| eventId <Badge type="info">NotRequired</Badge> | int | 活动 ID |
| performance | int | - |
| technique | int | - |
| visual | int | - |

### Member

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| eventId | int | 活动 ID |
| situationId | int | - |
| percent | int | - |
| seq | int | - |

### LimitBreak

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| rarity | int | - |
| rank | int | - |
| percent | float | - |

### PointReward

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| point | str | 点数 |
| rewardType | str | 奖励类型 |
| rewardId <Badge type="info">NotRequired</Badge> | int | 奖励 ID |
| rewardQuantity | int | 奖励数量 |

### RankingReward

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| fromRank | int | 奖励起始排名 |
| toRank | int | 奖励终止排名 |
| rewardType | str | 奖励类型 |
| rewardId <Badge type="info">NotRequired</Badge> | int | 奖励 ID |
| rewardQuantity | int | 奖励数量 |

### Story 活动故事 {#story}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| scenarioId | str | 场景 ID |
| coverImage | str | 封面图片链接 |
| backgroundImage | str | 背景图片链接 |
| releasePt | str | 解锁所需点数 |
| rewards | List[[StoryReward](./events/#storyreward)] | 故事奖励 |
| caption | List[str \| None] | 故事说明[定长列表](/typing/#fixed-list) |
| title | List[str \| None] | 故事标题[定长列表](/typing/#fixed-list) |
| synopsis | List[str \| None] | 故事简介[定长列表](/typing/#fixed-list) |
| releaseConditions | List[str \| None] | 解锁条件[定长列表](/typing/#fixed-list) |

### StoryReward

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| rewardType | str | 奖励类型 |
| rewardId <Badge type="info">NotRequired</Badge> | int | 奖励 ID |
| rewardQuantity | int | 奖励数量 |

### Music 活动歌曲 {#music}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| musicId | int | 歌曲 ID |
| musicRankingRewards | List[[MusicRankingReward](./events/#musicrankingreward)] | 歌曲排名奖励 |

### MusicRankingReward

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| fromRank | int | 奖励起始排名 |
| toRank | int | 奖励终止排名 |
| resourceType | str | 资源类型 |
| resourceId | int | 资源 ID |
| Quantity | int | 数量 |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总活动信息，返回以活动 ID 为字段名、 `EventsAllInfo` 为字段值的信息字典， `EventsAllInfo` 为从 [`EventInfo`](./events/#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `EventsAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以活动 ID 为字段名、 [`NoneDict`](/typing/#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 1 | `eventName` |
| 3 | `endAt` |
| 4 | `rewardCards` |
| 5 | `limitBreaks` |
| 6 | `limitBreaks` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, EventsAllInfo | NoneDict]`

## class Event() {#event}

活动类，包含各种活动相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 活动 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def tracker()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [Server](/typing/#server-id) | - | 服务器 ID |

获取活动的 PT 与排名追踪器。

<Badge type="info">返回值:</Badge> [`EventTracker`](./eventtracker/#eventtracker)

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取活动信息。

<Badge type="info">返回值:</Badge> [`EventInfo`](./events/#info)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取活动的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_banner() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |

获取活动缩略图资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_logo() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |

获取活动 LOGO 资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_topscreen() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |
| type | str | - | 主界面图像类型 |

::: details type 可用参数值
| 值 | 描述 |
|:-----:|:-------------------|
| `'bg'` | 背景全图 |
| `'trim'` | 角色图像 |
:::

获取活动主界面图像资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_stamp() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取活动奖励稀有表情资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_top() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

该方法存在多种调用方式：

::: info 获取最终 T10 排名分数线

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [Server](/typing/#server-id) | - | 服务器 ID |
| mid | int | 0 | 歌曲 ID 。仅在查询歌曲分数排名时为非 `0` 值 |
| latest <Badge type="info">keyword</Badge> | Literal[1] | - | 表示获取最终排名分数线 |

获取最终 T10 排名分数线。

:::

::: info 获取最新 T10 排名分数线

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [Server](/typing/#server-id) | - | 服务器 ID |
| mid | int | 0 | 歌曲 ID 。仅在查询歌曲分数排名时为非 `0` 值 |
| interval <Badge type="info">keyword</Badge> | int | - | 获取最新分数线间隔 |

获取最新 T10 排名分数线。

:::

<Badge type="info">返回值:</Badge> [`EventTopData`](./eventtop/#data)

### def get_rotation_musics() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取团队 LIVE 佳节活动歌曲循环数据 [`FestivalRotationMusic`](./festival/#rotation-music) 。仅在活动类型为团队 LIVE 佳节活动时有效。

<Badge type="info">返回值:</Badge> `List[FestivalRotationMusic]`

### def get_stages() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取团队 LIVE 佳节活动舞台数据 [`FestivalStage`](./festival/#stage) 。仅在活动类型为团队 LIVE 佳节活动时有效。

<Badge type="info">返回值:</Badge> `List[FestivalStage]`
