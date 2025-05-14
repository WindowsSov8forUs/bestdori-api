# thumb 缩略图

缩略图资源获取模块。

```python
from bestdori import thumb
```

## def get_chara() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 卡牌 ID |
| resource_set_name | str | - | 资源集名称 |
| type | str | - | 资源类型 |
| server <Badge type="info">keyword</Badge> | [ServerName](/typing/#server-name) | - | 指定获取来源服务器 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

::: details type 可用参数值
| 值 | 描述 |
|:---|:----|
| `'normal'` | 特训前卡面 |
| `'after_training'` | 特训后卡面 |
:::

获取卡牌缩略图资源，返回获取到的字节值。

<Badge type="info">返回值:</Badge> `bytes`

## def get_degree() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| degree_name | str | - | 称号名称 |
| server <Badge type="info">keyword</Badge> | [ServerName](/typing/#server-name) | - | 指定获取来源服务器 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取称号资源，返回获取到的字节值。

<Badge type="info">返回值:</Badge> `bytes`

## def get_costume() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 服装 ID |
| asset_bundle_name | str | - | 资源集名称 |
| server <Badge type="info">keyword</Badge> | [ServerName](/typing/#server-name) | - | 指定获取来源服务器 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取服装缩略图资源，返回获取到的字节值。

<Badge type="info">返回值:</Badge> `bytes`
