# missions 任务

任务信息获取模块。

```python
from bestdori import missions
```

## 类型定义

### MissionInfo 任务信息 {#info}

任务详细信息字典。 `all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | str | 任务类型 |
| startAt | List[str \| None] | 任务起始时间戳[定长列表](/typing#fixed-list) |
| endAt | List[str \| None] | 任务终止时间戳[定长列表](/typing#fixed-list) |
| title | List[str \| None] | 任务标题[定长列表](/typing#fixed-list) |
| details | List[List[[Detail](/missions#detail)] \| None] | 任务详细信息列表[定长列表](/typing#fixed-list) |

### Detail 任务详细信息 {#detail}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| seq | int | 任务阶段序号 |
| title | str | 任务标题 |
| description | str | 任务描述 |
| maxProgress | int | 任务最大进度 |
| reward | [DetailReward](/missions#detail-reward) | 任务奖励信息 |

### DetailReward 任务奖励信息 {#detail-reward}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| missionId <Badge type="info">NotRequired</Badge> | int | 任务 ID |
| seq <Badge type="info">NotRequired</Badge> | int | 任务阶段序号 |
| missionRewardId <Badge type="info">NotRequired</Badge> | int | 任务奖励 ID |
| resourceType | str | 资源类型 |
| resourceId | int | 资源 ID |
| quantity | int | 数量 |

## def get_all() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取总任务信息，返回以任务 ID 为字段名、 `MissionsAllInfo` 为字段值的信息字典， `MissionsAllInfo` 为从 [`MissionInfo`](./missions#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `MissionsAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以任务 ID 为字段名、 [`NoneDict`](/typing#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 5 | `title` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, MissionsAllInfo | NoneDict]`

## class Mission() {#mission}

任务类，包含各种任务相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 任务 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取任务信息。

<Badge type="info">返回值:</Badge> [`MissionInfo`](./missions#info)

### def get_comment() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing#order) | `'TIME_ASC'` |

获取任务的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post#list)
