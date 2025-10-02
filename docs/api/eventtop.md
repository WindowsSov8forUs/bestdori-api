# eventtop 活动 T10 排名数据

活动 T10 排名数据获取模块。

```python
from bestdori import eventtop
```

## 类型定义

### EventTopData 活动排名信息 {#data}

活动排名信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| points | List[[Point](#point)] | 活动排名分数列表 |
| users | List[[User](#user)] | 活动排名玩家列表 |

### Point

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| time | float | 分数时间戳 |
| uid | int | 玩家 ID |
| value | int | 分数 |

### User

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| uid | int | 玩家 ID |
| name | str | 玩家名 |
| introduction | str | 玩家自我介绍 |
| rank | int | 玩家排名 |
| sid | int | - |
| strained | int | - |
| degrees | List[int] | 玩家称号 ID |

## def get_data() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取活动 T10 排名分数线。该方法存在两种调用方式，分别获取两种情况下的数据：

::: info 获取活动最终 T10 排名分数线

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [Server](/typing#server-id) | - | 服务器 ID |
| event | int | - | 活动 ID |
| mid | int | 0 | 歌曲 ID 。仅在查询歌曲分数排名时为非 `0` 值 |
| latest <Badge type="info">keyword</Badge> | Literal[1] | - | 表示获取最终排名分数线 |
| latest <Badge type="info">keyword</Badge> | Literal[1] | - | 表示获取最终排名分数线 |

获取活动最终 T10 排名分数线（已不再支持 `me` 参数，登录态自动生效）。

:::

::: info 获取活动最新 T10 排名分数线

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [Server](/typing#server-id) | - | 服务器 ID |
| event | int | - | 活动 ID |
| mid | int | 0 | 歌曲 ID 。仅在查询歌曲分数排名时为非 `0` 值 |
| interval <Badge type="info">keyword</Badge> | int | - | 获取最新分数线间隔 |
| interval <Badge type="info">keyword</Badge> | int | - | 获取最新分数线间隔 |

获取活动最新 T10 排名分数线（已不再支持 `me` 参数，登录态自动生效）。

:::

<Badge type="info">返回值:</Badge> [`EventTopData`](./eventtop#data)
