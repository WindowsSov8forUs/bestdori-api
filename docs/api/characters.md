# characters 角色

角色信息获取模块。

```python
from bestdori import characters
```

## 类型定义

### CharacterInfo 角色信息 {#info}

角色详细信息字典。 `all.{index}.json` / `main.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| characterType | str | 角色类型 |
| characterName | List[str \| None] | 角色姓名[定长列表](/typing/#fixed-list) |
| nickname | List[str \| None] | 角色昵称[定长列表](/typing/#fixed-list) |
| bandId <Badge type="info">NotRequired</Badge> | int | 角色所在乐队 ID 。非主要角色不存在此项 |
| colorCode <Badge type="info">NotRequired</Badge> | str | 角色代表色十六进制码。非主要角色不存在此项 |
| firstName | str | 角色名[定长列表](/typing/#fixed-list) |
| lastName | str | 角色姓氏[定长列表](/typing/#fixed-list) |
| seasonCostumeListMap <Badge type="info">NotRequired</Badge> | [SeasonCostumeListMap](./characters/#seasoncostumelistmap) | 角色某季服装列表映射表 |
| sdAssetBundleName | str | 角色 SD 资源资源库名 |
| defaultCostumeId <Badge type="info">NotRequired</Badge> | int | 默认服装 ID 。非主要角色不存在此项 |
| ruby | List[str \| None] | 角色读音注释[定长列表](/typing/#fixed-list) |
| profile <Badge type="info">NotRequired</Badge> | [Profile](./characters/#profile) | 角色个人资料 |

### SeasonCostumeListMap

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | [SeasonCostumeListMapentrieseason](./characters/#seasoncostumelistmapentrieseason) | 季 ID 与服装列表映射字典 |

### SeasonCostumeListMapentrieseason

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| entries | List[[SeasonCostumeListMapentrieseasonEntry](./characters/#seasoncostumelistmapentrieseasonentry)] | 服装列表 |

### SeasonCostumeListMapentrieseasonEntry

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| characterId | int | 角色 ID |
| basicSeasonId | int | - |
| costumeType | str | 服装类型 |
| seasonCostumeType | str | - |
| sdAssetBundleName | str | LIVESD 资源资源库名 |
| live2dAssetBundleName | str | Live2D 资源资源库名 |
| seasonType | str | 季 ID |

### Profile 角色个人资料 {#profile}

角色个人信息字典。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| characterVoice | List[str \| None] | 角色声优名[定长列表](/typing/#fixed-list) |
| favoriteFood | List[str \| None] | 角色喜好食物[定长列表](/typing/#fixed-list) |
| hatedFood | List[str \| None] | 角色厌恶食物[定长列表](/typing/#fixed-list) |
| hobby | List[str \| None] | 角色习惯[定长列表](/typing/#fixed-list) |
| selfIntroduction | List[str \| None] | 角色自我介绍[定长列表](/typing/#fixed-list) |
| school | List[str \| None] | 角色学校名称[定长列表](/typing/#fixed-list) |
| schoolCls | List[str \| None] | 角色所在班级[定长列表](/typing/#fixed-list) |
| schoolYear | List[str \| None] | 角色所在学年[定长列表](/typing/#fixed-list) |
| part | str | 角色担当 |
| birthday | str | 角色生日时间戳 |
| constellation | str | 角色星座名 |
| height | float | 角色身高 (cm) |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总角色信息，返回以角色 ID 为字段名、 `CharacterAllInfo` 为字段值的信息字典， `CharacterAllInfo` 为从 [`CharacterInfo`](./characters/#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `CharacterAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以角色 ID 为字段名、 [`NoneDict`](/typing/#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 2 | `colorCode` |
| 5 | `seasonCostumeListMap` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, CharacterAllInfo | NoneDict]`

## def get_main() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取主要角色信息，返回以卡牌 ID 为字段名、 `CharacterMainInfo` 为字段值的信息字典， `CharacterMainInfo` 为从 [`CharacterInfo`](./characters/#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `CharacterMainInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以角色 ID 为字段名、 [`NoneDict`](/typing/#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值相对新增字段名 |
|:-----:|:-----------------------|
| 0 | - |
| 1 | `characterType`, `bandId` |
| 2 | `characterName`, `nickname`, `colorCode` |
| 3 | `firstName`, `lastName` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, CharacterMainInfo | NoneDict]`

## class Character() {#character}

角色类，包含各种角色相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 角色 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取角色信息。

<Badge type="info">返回值:</Badge> [`CharactersInfo`](./characters/#info)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取角色的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_icon() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取角色图标资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_kv_image() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取角色主视觉图资源。

<Badge type="info">返回值:</Badge> `bytes`
