# eventtracker 活动 PT 与排名追踪模块

```python
from bestdori import eventtracker
```

## 类型定义

### EventTrackerData 活动分数线追踪信息 {#data}

活动分数线追踪信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| result | Literal[True] | 是否返回有效信息。值一定为 `True` |
| cutoffs | List[[EventTrackerCutoff](./eventtracker#cutoff)] | 分数线追踪信息列表 |

### Cutoff 单次分数线追踪信息 {#cutoff}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| time | float | 追踪时间时间戳 |
| ep | int | 分数线 |

### EventTrackerRate 各服务器各种类活动各排名计算比率

各服务器各种类活动各排名计算比率，用于进行预测线计算。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | str | 活动种类 |
| server | [Server](/typing#server-id) | 服务器 ID |
| tier | int | 排名 |
| rate | float \| None | 计算比率 |

## def get_rates() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取活动追踪比率列表（已不再接受 `me` 参数，登录态通过全局会话生效）。

<Badge type="info">返回值:</Badge> [`EventTrackerRate`](./eventtracker#rate)

## class EventTracker() 活动 PT 与排名追踪器 {#eventtracker}

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [Server](/typing#server-id) | 服务器 ID |
| event | int | - | 活动 ID |

### def get_top() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| mid | int | 0 | 歌曲 ID 。仅在查询歌曲分数排名时为非 `0` 值 |
| interval <Badge type="info">keyword</Badge> | int | - | 获取最新分数线间隔 |

获取实时 T10 排名分数线追踪信息（无需也不支持 `me` 参数）。

<Badge type="info">返回值:</Badge> [`EventTopData`](./eventtop#data)

### def get_data() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| tier | int | - | 获取排名 |

获取实时分数线追踪信息。

<Badge type="info">返回值:</Badge> [`EventTrackerData`](./eventtracker#data)

### def get_comment() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing#order) | `'TIME_ASC'` |

获取活动追踪器的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post#list)
