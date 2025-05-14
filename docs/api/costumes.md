# costumes 服装

服装信息获取模块。

```python
from bestdori import costumes
```

## 类型定义

### CostumeInfo 服装信息 {#info}

角色详细信息字典。`all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| characterId | int | 服装对应角色 ID |
| assetBundleName | str | 服装资源库名 |
| description | List[str \| None] | 服装描述[定长列表](/typing/#fixed-list) |
| publishedAt | List[str \| None] | 服装上线时间时间戳[定长列表](/typing/#fixed-list) |
| sdResourceName | str | 服装 LIVESD 资源库名 |
| howToGet | List[str \| None] | 服装获取方法[定长列表](/typing/#fixed-list) |
| cards | List[int] | 服装对应卡牌 ID 列表 |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总服装信息，返回以服装 ID 为字段名、 `CostumesAllInfo` 为字段值的信息字典， `CostumesAllInfo` 为从 [`CostumeInfo`](./costumes/#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `CostumesAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以服装 ID 为字段名、 [`NoneDict`](/typing/#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 5 | `publishedAt` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, CostumesAllInfo | NoneDict]`

## class Costume() {#character}

服装类，包含各种服装相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 服装 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取服装信息。

<Badge type="info">返回值:</Badge> [`CostumeInfo`](./costumes/#info)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取服装的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_sdchara() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取服装 LIVESD 图片资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_build_data() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取服装 Live2D 模型资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_icon() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取服装图标资源。

<Badge type="info">返回值:</Badge> `bytes`
