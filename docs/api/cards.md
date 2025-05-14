# cards 卡牌

卡牌信息获取模块。

```python
from bestdori import cards
```

## 类型定义

### CardInfo 卡牌信息 {#info}

卡牌详细信息字典。 `all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| characterId | int | 角色 ID |
| attribute | [Attribute](./cards/#attribute) | 卡牌属性 |
| prefix | List[str \| None] | 卡牌名称[定长列表](/typing/#fixed-list) |
| rarity | [Rarity](./cards/#rarity) | 卡牌稀有度 |
| levelLimit | int | 卡牌等级上限 |
| resourceSetName | str | 卡牌资源所在集合名。提取卡面等资源时需要提供。 |
| releasedAt | List[str \| None] | 卡牌上线时间戳[定长列表](/typing/#fixed-list) |
| skillId | int | 卡牌技能 ID |
| type | str | 卡牌类型 |
| stat | [Stat](./cards/#stat) | 卡牌数据信息 |
| sdResourceName | str | 卡牌 LIVE 服装资源名 |
| episodes | [Episodes](./cards/#episodes) | 卡牌故事 |
| costumeId | int | 卡牌服装 ID |
| gachaText | List[str \| None] | 卡牌上线招募名[定长列表](/typing/#fixed-list) |
| skillName | List[str \| None] | 卡牌技能名[定长列表](/typing/#fixed-list) |
| source | List[[Source](./cards/#source) \| [NoneDict](/typing/#nonedict)] | 卡牌招募信息[定长列表](/typing/#fixed-list) |

### Attribute 属性 {#attribute}

卡牌属性枚举类。

| 值 | 描述 |
|:--:|:----|
| `powerful` | <img src="/powerful.svg" class="text-icon"> POWERFUL 属性卡牌 |
| `pure` | <img src="/pure.svg" class="text-icon"> PURE 属性卡牌 |
| `cool` | <img src="/cool.svg" class="text-icon"> COOL 属性卡牌 |
| `happy` | <img src="/happy.svg" class="text-icon"> HAPPY 属性卡牌 |

### Rarity 稀有度 {#rarity}

卡牌稀有度枚举类。

| 值 | 描述 |
|:--:|:----|
| `1` | <img src="/star_1.png" class="text-icon"> ★1 卡牌 |
| `2` | <img src="/star_2.png" class="text-icon"> ★2 卡牌 |
| `3` | <img src="/star_3.png" class="text-icon"> ★3 卡牌 |
| `4` | <img src="/star_4.png" class="text-icon"> ★4 卡牌 |
| `5` | <img src="/star_5.png" class="text-icon"> ★5 卡牌 |

### Stat 卡牌数据 {#stat}

卡牌数据字典。该字典中字段 `episodes` 与 `training` 并非必定存在。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| 1, 2, ... | [StatInfo](./cards/#stat-training) | 卡牌各等级下数据值。在 `all.5.json` 中只会包括最低等级与最高等级，在 `CardInfo` 中则会包括所有等级。 |
| episodes | List[[StatInfo](./cards/#stat-training)] | 卡牌故事阅读后增加数据值。数量为卡牌所有的卡牌故事数量，若没有卡牌故事则不存在该字段。 |
| training | [StatTraining](./cards/#stat-training) | 卡牌特训增加数据值。若卡牌无特训则不存在该字段。 |

### StatInfo {#stat-info}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| performance | int | 卡牌演出值 |
| technique | int | 卡牌技巧值 |
| visual | int | 卡牌形象值 |

### StatTraining {#stat-training}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| levelLimit | int | 特训等级上限 |
| performance | int | 卡牌演出值 |
| technique | int | 卡牌技巧值 |
| visual | int | 卡牌形象值 |

### Episodes 卡牌故事 {#episodes}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | List[[EpisodesEntry](./cards/#episodesentry)] | - |

### EpisodesEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| episodeId | int | 故事 ID |
| episodeType | str | 故事类型 |
| situationId | str | - |
| scenarioId | int | 场景 ID |
| appendPerformancce | int | 增加演出值 |
| appendTechnique | int | 增加技巧值 |
| appendVisual | int | 增加形象值 |
| releaseLevel | int | 开放等级 |
| costs | [EpisodesEntryCosts](./cards/#episodesentrycosts) | 故事解锁所需道具 |
| rewards | [EpisodesEntryRewards](./cards/#episodesentryrewards) | 故事奖励 |
| title | List[str \| None] | 故事标题[定长列表](/typing/#fixed-list) |
| characterId | int | 故事角色 ID |

### EpisodesEntryCosts

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | List[[EpisodesEntryCostsEntry](./cards/#episodesentrycostsentry)] | - |

### EpisodesEntryCostsEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| resourceId | int | - |
| resourceType | str | - |
| quantity | int | - |
| lbBonus | int | - |

### EpisodesEntryRewards

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | List[[EpisodesEntryRewardsEntry](./cards/#episodesentryrewardsentry)] | - |

### EpisodesEntryRewardsEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| resourceType | str | - |
| quantity | int | - |
| lbBonus | int | - |

### Source 卡牌招募信息 {#source}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| gacha | Dict[str, [SourceGacha](./cards/#sourcegacha)] | 招募 ID 与抽取概率字典 |

### SourceGacha

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| probability | float | 招募抽取概率 |

### TrainType 特训种类 {#train-type}

| 值 | 描述 |
|:---|:----|
| `'normal'` | 特训前 |
| `'after_training'` | 特训后 |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总卡牌信息，返回以卡牌 ID 为字段名、 `CardAllInfo` 为字段值的信息字典， `CardAllInfo` 为从 [`CardInfo`](./cards/#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `CardAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以卡牌 ID 为字段名、 [`NoneDict`](/typing/#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 2 | `attribute` |
| 3 | `prefix` |
| 5 | `stat` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, CardAllInfo | NoneDict]`

## def get_attribute_icon() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| attribute | [Attribute](./cards/#attribute) | - | 属性名称 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取属性图标资源。

<Badge type="info">返回值:</Badge> `bytes`

## def get_star_icon() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| star | str | - | 星标种类 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

::: details type 可用参数值
| 值 | 描述 |
|:---|:----|
| `'star'` | 特训前星标 |
| `'star_trained'` | 特训后星标 |
:::

获取星标图标资源。

<Badge type="info">返回值:</Badge> `bytes`

## def get_frame() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| level | [Rarity](./cards/#rarity) | - | 边框星级 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取指定稀有度卡牌边框资源。

<Badge type="info">返回值:</Badge> `bytes`

## def get_card_frame() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| level | [Rarity](./cards/#rarity) | - | 边框星级 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取指定稀有度卡牌缩略图边框资源。

<Badge type="info">返回值:</Badge> `bytes`

## class Card() {#card}

卡牌类，包含各种卡牌资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 卡牌 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取卡牌信息。

<Badge type="info">返回值:</Badge> [`CardInfo`](./cards/#info)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取卡牌的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_card() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| type | [TrainType](./cards/#train-type) | - | 卡面种类。指定特训前或特训后 |

获取卡牌完整卡面图片资源。部分卡牌（如 <img src="/star_1.png" class="text-icon"> 、 <img src="/star_2.png" class="text-icon"> 卡牌）不存在特训后卡面，部分卡牌（如 KiraFes 卡牌）不存在特训前卡面，此时若尝试获取不存在的卡面会抛出异常。

<Badge type="info">返回值:</Badge> `bytes`

### def get_trim() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| type | [TrainType](./cards/#train-type) | - | 卡面种类。指定特训前或特训后 |

获取卡牌无背景卡面图片资源。部分卡牌（如 <img src="/star_1.png" class="text-icon"> 、 <img src="/star_2.png" class="text-icon"> 卡牌）不存在特训后卡面，部分卡牌（如 KiraFes 卡牌）不存在特训前卡面，此时若尝试获取不存在的卡面会抛出异常。

<Badge type="info">返回值:</Badge> `bytes`

### def get_thumb() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| type | [TrainType](./cards/#train-type) | - | 缩略图种类。指定特训前或特训后 |

获取卡牌缩略图图片资源。部分卡牌（如 <img src="/star_1.png" class="text-icon"> 、 <img src="/star_2.png" class="text-icon"> 卡牌）不存在特训后缩略图，部分卡牌（如 KiraFes 卡牌）不存在特训前缩略图，此时若尝试获取不存在的缩略图会抛出异常。

<Badge type="info">返回值:</Badge> `bytes`

### def get_livesd() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取 LIVE 服装图片。获取到的图片为多张图片放在一起的透明背景图片，需要进行额外拆分操作。

<Badge type="info">返回值:</Badge> `bytes`
