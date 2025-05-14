# eventarchives 活动数据

活动数据信息获取模块。

```python
from bestdori import eventarchives
```

## 类型定义

### EventArchiveInfo 活动数据信息 {#info}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| cutoff | List[[NoneDict](/typing#nonedict) \| Dict[str, int]] | 活动分数线[定长列表](/typing#fixed-list) |
| board | List[List[int]] | [定长列表](/typing#fixed-list)，此处空项值为空列表 |

## def get_all() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | Literal[5] | `5` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取总乐队信息，返回以乐队 ID 为字段名、[EventArchiveInfo](./eventarchives#info)为字段值的信息字典。

<Badge type="info">返回值:</Badge> `Dict[str, EventArchiveInfo]`

## class EventArchive() {#eventarchive}

活动数据类，包含各种活动数据相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 活动 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取活动数据信息。

<Badge type="info">返回值:</Badge> [`EventArchiveInfo`](./eventarchives#info)

### def get_top() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [Server](/typing#server-id) | - | 指定活动服务器 |
| mid | int | 0 | 歌曲 ID 。仅在查询歌曲分数排名时为非 `0` 值 |

获取活动的最终排名分数线数据。

<Badge type="info">返回值:</Badge> [`EventTopData`](./eventtop#data)

### def get_comment() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing#order) | `'TIME_ASC'` |

获取活动数据的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post#list)
