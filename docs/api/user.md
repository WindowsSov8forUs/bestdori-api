# user 用户

用户信息处理模块。

```python
from bestdori import user
```

## 类型定义

### UserInfo 用户信息 {#info}

从 Bestdori 中获取到的用户信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| result | Literal[True] | 是否返回有效信息。值一定为 `True` |
| followingCount | int | 跟随数 |
| followedByCount | int | 跟随者数 |
| followed | bool | 是否已跟随。根据请求时传入的登录信息判断，若未传入则默认为 `false` |
| nickname | str | 昵称 |
| titles | List[[Title](/typing/#title)] | 用户展示的称号 |
| posterCard | [PosterCard](./user/#poster-card) | 用户使用的海报信息 |
| selfIntro | str | 用户个人简介 |
| serverIds | [ServerId](./user/#server-id) | 用户绑定的玩家信息 |
| favCharacters | List[int] | 用户喜爱的角色 ID |
| favCards | List[int] | 用户喜爱的卡牌 ID |
| favBands | List[int] | 用户喜爱的乐队 ID |
| favSongs | List[int] | 用户喜爱的歌曲 ID |
| favCostumes | List[int] | 用户喜爱的服装 ID |

### PosterCard 海报信息 {#poster-card}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| id | int | 海报所用卡牌 ID |
| offset | int | 海报位置修正 |
| trainedArt | bool | 是否使用训练后卡面 |

### ServerId 绑定服务器信息 {#server-id}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| id | int | 绑定的玩家 ID |
| server | [Server](/typing/#server-id) | 绑定的服务器 ID |

### MeInfo 登录用户信息 {#me-info}

登录 Bestdori 后获取到的登录用户信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| result | Literal[True] | 是否返回有效信息。值一定为 `True` |
| username | str | 用户名 |
| nickname | str | 昵称 |
| titles | List[[Title](/typing/#title)] | 用户展示的称号 |
| email | str | 用户邮箱 |
| messsageCount | int | 未读消息数 |

## User 用户类 {#user}

用户数据信息获取类。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| username | str | - | 用户的用户名 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取用户信息。

<Badge type="info">返回值:</Badge> [`UserInfo`](#info)

### def get_posts() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_DESC'` | 帖子排序方式 |

获取用户的社区帖子列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_charts() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_DESC'` | 帖子排序方式 |

获取用户的社区谱面列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_texts() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_DESC'` | 帖子排序方式 |

获取用户的社区文本帖子列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_stories() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_DESC'` | 帖子排序方式 |

获取用户的社区故事列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

## Me 登录用户类 {#me}

登录用户操作类，同时负责用户权限登录认证。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| username | str | - | 登录用户名 |
| password | str | - | 登录密码 |

### def login() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

登录账号获取 Cookies 。

### def update_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| info | [UserInfo](#info) | - | 更新后的用户信息 |

更新该用户的信息。返回更新成功后的用户信息。

<Badge type="info">返回值:</Badge> [`UserInfo`](#info)
