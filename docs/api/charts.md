# charts 谱面

谱面相关操作模块。

```python
from bestdori import charts
```

## class Statistics() <Badge type="info">dataclass</Badge> {#statistics}

谱面数据统计类。谱面统计时用以统计存储统计数据。

| 属性名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| time | float | - | 谱面总时长 |
| notes | int | - | 谱面音符总数 |
| bpm | List[float] | - | 谱面 BPM 列表 |
| main_bpm | float | - | 谱面主要 BPM |

## class Chart() {#chart}

谱面类，包含谱面相关操作与资源获取。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| chart | List[Dict[str, Any]] | - | 原始谱面结构。通过 `json.loads()` 方法处理谱面原始代码可得 |

### def standardize()

谱面规范化处理。返回进行规范化处理后的谱面。

<Badge type="info">返回值:</Badge> [`Chart`](./charts#chart)

### def count()

谱面数据统计。返回统计后的详细数据。

<Badge type="info">返回值:</Badge> [`Statistics`](./charts#statistics)

### def to_list()

将谱面转换为原始谱面结构。返回值可通过 `json.dummps()` 处理得到谱面原始代码。

<Badge type="info">返回值:</Badge> `List[Dict[str, Any]]`

### def json()

将谱面转换为谱面原始代码 `JSON` 字符串。

<Badge type="info">返回值:</Badge> `str`

### def from_python() <Badge type="info">classmethod</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| data | List[Dict[str, Any]] | - | 原始谱面结构。通过 `json.loads()` 方法处理谱面原始代码可得 |

将原始谱面数据转换为谱面类，并进行规范化处理。

<Badge type="info">返回值:</Badge> [`Chart`](./charts#chart)

### def from_json() <Badge type="info">classmethod</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| data | str | - | 谱面原始代码 |

将谱面原始代码转换为谱面类，并进行规范化处理。

<Badge type="info">返回值:</Badge> [`Chart`](./charts#chart)

### def get_chart() <Badge type="info">classmethod</Badge> <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 歌曲 ID |
| diff | [DifficultyName](/typing#difficulty-name) | `'expert'` | 获取的谱面难度 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取 BanG Dream! 游戏内谱面。

<Badge type="info">返回值:</Badge> [`Chart`](./charts#chart)
