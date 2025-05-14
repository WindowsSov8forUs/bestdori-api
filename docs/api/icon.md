# icon 图标

图标资源获取模块。

```python
from bestdori import icon
```

## def get_band() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 乐队 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取乐队图标资源。

<Badge type="info">返回值:</Badge> `bytes`

## def get_server() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing#server-name) | - | 服务器名 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取服务器图标资源。

<Badge type="info">返回值:</Badge> `bytes`
