# 杂项方法

```python
from bestdori import utils
```

## def hex_to_rgb()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| hex | str | - | 16进制颜色值 |

将 16 进制颜色值转换为 RGB 元组。

<Badge type="info">返回值:</Badge> `tuple[int, int, int]`

## def name()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| obj | Object | - | 任意可以提取名称列表的对象 |

提取对象的名称列表中第一个非空元素。

<Badge type="info">返回值:</Badge> `str`
