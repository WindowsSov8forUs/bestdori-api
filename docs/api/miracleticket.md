# miracleticket 自选券

自选券信息获取模块。

```python
from bestdori import miracleticket
```

## 类型定义

### MiracleTicketExchangeInfo 自选券信息 {#info}

自选券详细信息字典。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| name | List[str \| None] | 自选券名称[定长列表](/typing/#fixed-list) |
| ids | List[List[int] \| None] | 自选券包含卡牌 ID [定长列表](/typing/#fixed-list) |
| exchangeStartAt | List[str \| None] | 自选券兑换开始时间戳[定长列表](/typing/#fixed-list) |
| exchangeEndAt | List[str \| None] | 自选券兑换结束时间戳[定长列表](/typing/#fixed-list) |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | Literal[5] | `5` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总自选券信息，返回以自选券 ID 为字段名、[MiracleTicketExchangeInfo](./miracleticket/#info)为字段值的信息字典。

<Badge type="info">返回值:</Badge> `Dict[str, MiracleTicketExchangeInfo]`

## class MiracleTicketExchange() {#miracleticketexchange}

自选券类，包含自选券相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 自选券 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取自选券信息。

<Badge type="info">返回值:</Badge> [`MiracleTicketExchangeInfo`](./miracleticket/#info)

### def get_ids() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |

获取自选券 ID 列表。

<Badge type="info">返回值:</Badge> `List[int]`
