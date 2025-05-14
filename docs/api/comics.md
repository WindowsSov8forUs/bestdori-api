# comics 漫画

漫画信息获取模块。

```python
from bestdori import comics
```

## 类型定义

### ComicInfo 漫画信息 {#info}

漫画详细信息字典。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| assetBundleName | str | 漫画资源库名 |
| title | List[str \| None] | 漫画标题[定长列表](/typing/#fixed-list) |
| subTitle | List[str \| None] | 漫画副标题[定长列表](/typing/#fixed-list) |
| publicStartAt | List[str \| Literal[1] \| None] | 漫画公开时间时间戳[定长列表](/typing/#fixed-list)。若漫画为服务器开放时即开放则此字段值为 `1` ，否则为时间戳字符串 |
| characterId | List[int] | 漫画相关角色 ID 列表 |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | Literal[5] | `5` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总漫画信息，返回以漫画 ID 为字段名、 [`ComicInfo`](./comics/#info) 为字段值的信息字典。

<Badge type="info">返回值:</Badge> `Dict[str, ComicInfo]`

## class Comic()

漫画类。包含各种漫画资源获取。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 漫画 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取漫画信息。

<Badge type="info">返回值:</Badge> [`ComicInfo`](./comics/#info)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取漫画的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_thumbnail() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 获取资源所在服务器 |

获取漫画缩略图资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_asset() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 获取资源所在服务器 |

获取漫画图像资源。

<Badge type="info">返回值:</Badge> `bytes`
