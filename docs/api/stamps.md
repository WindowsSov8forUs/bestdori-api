# stamps 贴纸

贴纸资源获取模块。

```python
from bestdori import stamps
```

## 类型定义

### StampInfo 贴纸信息 {#info}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| imageName | str | 贴纸资源文件名 |

## def get_all() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | Literal[2] | `2` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取总贴纸信息，返回以贴纸 ID 为字段名、[StampInfo](#info)为字段值的信息字典。

## class Stamp() {#stamp}

贴纸类，包含贴纸相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 贴纸 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取贴纸信息。

<Badge type="info">返回值:</Badge> [`StampInfo`](#info)

### def get_stamp() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing#server-name) | - | 指定获取来源服务器 |

获取贴纸资源，返回获取到的字节值。

<Badge type="info">返回值:</Badge> `bytes`
