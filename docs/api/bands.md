# bands 乐队

乐队信息获取模块。

```python
from bestdori import bands
```

## 类型定义

### BandsInfo {#info}

乐队名称信息字典。实际获取到的字典为以**乐队 ID**为字段、该字典为值的字典。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| bandName | List[str \| None] | 乐队名称[定长列表](/typing#fixed-list) |

## def get_all() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | Literal[1] | `1` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取总乐队信息，返回以乐队 ID 为字段名、[BandsInfo](./bands#info)为字段值的信息字典。

<Badge type="info">返回值:</Badge> `Dict[str, BandsInfo]`

## def get_main() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | Literal[1] | `1` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取主要乐队信息，返回以乐队 ID 为字段名、[BandsInfo](./bands#info)为字段值的信息字典。

<Badge type="info">返回值:</Badge> `Dict[str, BandsInfo]`

## def get_logo() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 获取的乐队 ID |
| type | str | - | 指定获取的 Logo 类型 |
| server | [ServerName](/typing#server-name) | - | 指定获取来源服务器 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

::: details type 可用参数值
| 值 | 描述 |
|:---|:----|
| `'logoS'` | 较小大小 Logo |
| `'logoL'` | 较大大小 Logo |
| `'LogoL_Mask'` | 较大大小 Logo 黑白遮罩 |
:::

获取乐队 Logo 资源，返回获取到的字节值。

<Badge type="info">返回值:</Badge> `bytes`
