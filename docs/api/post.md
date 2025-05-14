# post 帖子

社区帖子操作模块。

```python
from bestdori import post
```

## 类型定义

### PostBasic 帖子基础信息 {#basic}

调用获取帖子列表方法时返回的数据结构。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| result | Literal[True] | 是否返回有效信息。值一定为 `True` |
| title | str \| None | 帖子标题 |
| author | [BasicAuthor](#basicauthor) | 帖子作者基础信息 |

### BasicAuthor

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| username | str | 用户名 |

### PostInfo 帖子详细信息 {#info}

调用获取帖子详细信息方法时返回的数据结构。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| categoryName | str | 帖子所在的画廊名 |
| categoryId | str | 帖子的分类 ID |
| title <Badge type="info">NotRequired</Badge> | str | 帖子标题，若帖子为 `'COMMENT'` 评论类则不存在 |
| song <Badge type="info">NotRequired</Badge> | [SongCustom](./post/#song-custom) \| [SongProvided](./post/#song-provided) | 社区谱面歌曲信息，若不是社区谱面帖子则不存在 |
| artists <Badge type="info">NotRequired</Badge> | str | 社区谱面艺术家信息，若不是社区谱面帖子则不存在 |
| diff <Badge type="info">NotRequired</Badge> | [Difficulty](/typing/#difficulty-id) | 社区谱面难度分级信息，若不是社区谱面帖子则不存在 |
| level <Badge type="info">NotRequired</Badge> | int | 社区谱面难度等级信息，若不是社区谱面帖子则不存在 |
| chart <Badge type="info">NotRequired</Badge> | [Chart](./charts/#chart) | 社区谱面数据，若不是社区谱面帖子则不存在 |
| content | List[[Content](/typing/#content)] | 帖子内容 |
| time | float | 帖子发布时间戳 |
| author | [Author](./post/#author) | 帖子作者信息 |
| likes | int | 帖子获得的喜欢数 |
| liked | bool | 是否已喜欢。根据请求时传入的登录信息判断，若未传入则默认为 `false` |
| tags | List[[Tag](./post/#tag)] | 帖子标签 |

### PostList 帖子列表 {#list}

调用获取帖子列表方法时返回的数据结构。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| result | Literal[True] | 是否返回有效信息。值一定为 `True` |
| posts | [PostListPost](./post/#postlistpost) | 获取到的帖子列表 |
| count | int | 获取到的帖子数量 |

### PostListPost

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| id | int | 帖子 ID |
| categoryName | str | 帖子所在的画廊名 |
| categoryId | str | 帖子的分类 ID |
| title <Badge type="info">NotRequired</Badge> | str | 帖子标题，若帖子为 `'COMMENT'` 评论类则不存在 |
| song <Badge type="info">NotRequired</Badge> | [SongCustom](./post/#song-custom) \| [SongProvided](./post/#song-provided) | 社区谱面歌曲信息，若不是社区谱面帖子则不存在 |
| artists <Badge type="info">NotRequired</Badge> | str | 社区谱面艺术家信息，若不是社区谱面帖子则不存在 |
| diff <Badge type="info">NotRequired</Badge> | [Difficulty](/typing/#difficulty-id) | 社区谱面难度分级信息，若不是社区谱面帖子则不存在 |
| level <Badge type="info">NotRequired</Badge> | int | 社区谱面难度等级信息，若不是社区谱面帖子则不存在 |
| time | float | 帖子发布时间戳 |
| content | List[[Content](/typing/#content)] | 帖子内容 |
| author | [Author](./post/#author) | 帖子作者信息 |
| likes | int | 帖子获得的喜欢数 |
| liked | bool | 是否已喜欢。根据请求时传入的登录信息判断，若未传入则默认为 `false` |
| tags | List[[Tag](./post/#tag)] | 帖子标签 |

### SongCustom 自定义歌曲信息 {#song-custom}

社区谱面自定义歌曲信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['custom'] | 社区谱面歌曲信息，此时固定为 `'custom'` |
| audio | str | 自定义歌曲音频链接 |
| cover | str | 自定义歌曲封面链接 |

### SongProvided 服务器提供歌曲信息 {#song-provided}

Bestdori 提供的歌曲信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | str | Bestdori 所提供的歌曲种类 |
| id | int | 歌曲 ID |

::: details type 可用字段值

| 值 | 描述 |
|:---|:----|
| `'bandori'` | BanG Dream! 歌曲，由 Bestdori! 提供 |
| `'llsif'` | LoveLive! School Idol Festival 歌曲，由 LLSIF 查卡器提供 |

:::

### Author 作者信息 {#author}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| username | str | 用户名 |
| nickname | str \| None | 昵称 |
| titles | List[[Title](/typing/#title)] \| None | 用户展示的称号列表 |

### Tag 标签 {#tag}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | str | 标签类型 |
| data | str | 标签数据 |

### TagGetResultTag

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | str | 标签类型 |
| data | str | 标签数据 |
| count | int | 使用该标签的帖子数量 |

## class SongResource() <Badge type="info">dataclass</Badge> {#song-resource}

歌曲资源类。用于存取获取到的歌曲的音频和封面链接。

| 属性名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| audio | bytes \| None | - | 音频资源字节，若未获取到则为 None |
| cover | bytes \| None | - | 封面资源字节，若未获取到则为 None |

## def get_list() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取帖子列表。该方法有多种调用方式：

::: info 获取社区谱面列表

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| search <Badge type="info">keyword</Badge> | str | `''` | 搜索关键字 |
| category_name <Badge type="info">keyword</Badge> | Literal['SELF_POST'] | `'SELF_POST'` | 帖子分类 |
| category_id <Badge type="info">keyword</Badge> | Literal['chart'] | 'chart' | 帖子分类 ID |
| tags <Badge type="info">keyword</Badge> | List[[Tag](#tag)] | `[]` | 搜索标签 |
| order <Badge type="info">keyword</Badge> | [Order](/typing/#order) | `'TIME_DESC'` | 排序方式 |
| limit <Badge type="info">keyword</Badge> | int | `20` | 获取到的帖子数量上限 |
| offset <Badge type="info">keyword</Badge> | int | `0` | 获取帖子时的偏移量 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取社区谱面列表。该方法会返回符合条件的社区谱面列表。

:::

::: info 获取指定用户帖子列表

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| username <Badge type="info">keyword</Badge> | str | - | 用户名 |
| order <Badge type="info">keyword</Badge> | [Order](/typing/#order) | `'TIME_DESC'` | 排序方式 |
| limit <Badge type="info">keyword</Badge> | int | `20` | 获取到的帖子数量上限 |
| offset <Badge type="info">keyword</Badge> | int | `0` | 获取帖子时的偏移量 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取指定用户帖子列表。该方法会返回符合条件的帖子列表。

:::

::: info 获取符合条件的帖子列表

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| search <Badge type="info">keyword</Badge> | Optional[str] | `None` | 搜索关键字 |
| following <Badge type="info">keyword</Badge> | Optional[bool] | `None` | 是否获取关注的用户的帖子 |
| category_name <Badge type="info">keyword</Badge> | Optional[str] | `None` | 帖子分类 |
| category_id <Badge type="info">keyword</Badge> | Optional[str] | `None` | 帖子分类 ID |
| tags <Badge type="info">keyword</Badge> | Optional[List[Tag](#tag)] | `None` | 搜索标签 |
| username <Badge type="info">keyword</Badge> | Optional[str] | `None` | 用户名 |
| order <Badge type="info">keyword</Badge> | [Order](/typing/#order) | `'TIME_DESC'` | 排序方式 |
| limit <Badge type="info">keyword</Badge> | int | `20` | 获取到的帖子数量上限 |
| offset <Badge type="info">keyword</Badge> | int | `0` | 获取帖子时的偏移量 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取符合条件的帖子列表。该方法会返回符合条件的帖子列表。

:::

## def search_tags() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| type | str | - | 标签类型 |
| data | str | - | 标签数据 |
| fuzzy | bool | `False` | 是否模糊搜索 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取符合条件的已有标签列表。该方法会返回符合条件的标签列表 [`TagGetResultTag`](#taggetresulttag) 。

<Badge type="info">返回值:</Badge> `List[TagGetResultTag]`

## def post() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

::: info 发布谱面

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| me <Badge type="info">keyword</Badge> | [Me](./user/#me) | `None` | 登录用户类 |
| artists <Badge type="info">keyword</Badge> | str | - | 歌曲艺术家名称 |
| category_id <Badge type="info">keyword</Badge> | Literal['chart'] | `'chart'` | 帖子分类 ID |
| category_name <Badge type="info">keyword</Badge> | Literal['SELF_POST'] | `'SELF_POST'` | 帖子分类 |
| chart <Badge type="info">keyword</Badge> | [Chart](./charts/#chart) | - | 谱面类 |
| content <Badge type="info">keyword</Badge> | List[[Content](/typing/#content)] | - | 帖子内容 |
| diff <Badge type="info">keyword</Badge> | [Difficulty](/typing/#difficulty-id) | - | 谱面难度分级信息 |
| level <Badge type="info">keyword</Badge> | int | - | 谱面难度等级信息 |
| song <Badge type="info">keyword</Badge> | [SongCustom](./post/#song-custom) \| [SongProvided](./post/#song-provided) | - | 社区谱面歌曲信息 |
| tags <Badge type="info">keyword</Badge> | List[[Tag](./post/#tag)] | `[]` | 帖子标签 |
| title <Badge type="info">keyword</Badge> | str | - | 帖子标题 |

发布谱面。该方法会返回发布成功的帖子 ID。

:::

::: info 发表文本帖子

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| me <Badge type="info">keyword</Badge> | [Me](./user/#me) | `None` | 登录用户类 |
| category_id <Badge type="info">keyword</Badge> | Literal['text'] | `'text'` | 帖子分类 ID |
| category_name <Badge type="info">keyword</Badge> | Literal['SELF_POST'] | `'SELF_POST'` | 帖子分类 |
| content <Badge type="info">keyword</Badge> | List[[Content](/typing/#content)] | - | 帖子内容 |
| tags <Badge type="info">keyword</Badge> | List[[Tag](./post/#tag)] | `[]` | 帖子标签 |
| title <Badge type="info">keyword</Badge> | str | - | 帖子标题 |

发表文本帖子。该方法会返回发布成功的帖子 ID。

:::

::: info 发表帖子

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |
| artists <Badge type="info">keyword</Badge> | str | - | 歌曲艺术家名称 |
| category_id <Badge type="info">keyword</Badge> | str | - | 帖子分类 ID |
| category_name <Badge type="info">keyword</Badge> | str | - | 帖子分类 |
| chart <Badge type="info">keyword</Badge> | Optional[[Chart](./charts/#chart)] | - | 谱面类 |
| content <Badge type="info">keyword</Badge> | List[[Content](/typing/#content)] | - | 帖子内容 |
| diff <Badge type="info">keyword</Badge> | Optional[[Difficulty](/typing/#difficulty-id)] | - | 谱面难度分级信息 |
| level <Badge type="info">keyword</Badge> | Optional[int] | - | 谱面难度等级信息 |
| song <Badge type="info">keyword</Badge> | Optional[[SongCustom](./post/#song-custom) \| [SongProvided](./post/#song-provided)] | - | 社区谱面歌曲信息 |
| tags <Badge type="info">keyword</Badge> | List[[Tag](./post/#tag)] | `[]` | 帖子标签 |
| title <Badge type="info">keyword</Badge> | str | - | 帖子标题 |

发表帖子。该方法会返回发布成功的帖子 ID。

:::

<Badge type="info">返回值:</Badge> `int`

## def find_post() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| category_name | str | - | 画廊名称 |
| category_id | str | - | 画廊 ID |
| id | int | - | 查询的帖子 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

查询帖子在该画廊的时间顺序。

<Badge type="info">返回值:</Badge> `int`

## class Post() {#post}

帖子类，包含帖子相关操作与资源获取。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 帖子 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_basic() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取帖子基础信息。

<Badge type="info">返回值:</Badge> [`PostBasic`](#basic)

### def get_details() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取帖子详细信息。

<Badge type="info">返回值:</Badge> [`PostInfo`](#info)

### def get_chart() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取社区谱面对象。只有当帖子为社区谱面时才可用。

<Badge type="info">返回值:</Badge> [`Chart`](./charts/#chart)

### def get_tags() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取帖子标签 [`Tag`](./post/#tag) 列表。

<Badge type="info">返回值:</Badge> `List[Tag]`

### def get_content() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取帖子内容字符串。

<Badge type="info">返回值:</Badge> `str`

### def get_song() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取帖子歌曲信息。仅在帖子为社区谱面时可用。

<Badge type="info">返回值:</Badge> [`SongResource`](#song-resource)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取帖子的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| content | List[[Content](/typing/#content)] | - | 帖子内容 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

发表帖子评论。返回评论帖子的 ID 。

<Badge type="info">返回值:</Badge> `int`

### def like() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| value | bool | `True` | 喜欢或取消喜欢 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

喜欢或取消喜欢帖子。
