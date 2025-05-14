# logincampaigns 登录奖励

登录奖励信息获取模块。

```python
from bestdori import logincampaigns
```

## 类型定义

### LoginCampaignInfo 登录奖励信息 {#info}

登录奖励信息字典。 `all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| caption | List[str \| None] | 登录奖励标题[定长列表](/typing/#fixed-list) |
| loginBonusType | str | 登录奖励类型 |
| assetBundleName | List[str \| None] | 资源库名称[定长列表](/typing/#fixed-list) |
| publishedAt | List[str \| None] | 开始时间戳[定长列表](/typing/#fixed-list) |
| closedAt | List[str \| None] | 结束时间戳[定长列表](/typing/#fixed-list) |
| assetMap | Dict[str, Any] | 资源信息字典 |
| details | List[List[[Detail](./logincampaigns/#detail)] \| None] | 登录奖励详情[定长列表](/typing/#fixed-list) |

### Detail 登录奖励详情 {#detail}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| loginBonusId | int | 登录奖励 ID |
| days | int | 登录奖励天数 |
| resourceType | str | 登录奖励资源类型 |
| resourceId | int | 登录奖励资源 ID |
| quantity | int | 登录奖励数量 |
| voideId <Badge type="info">NotRequired</Badge> | int | 登录奖励语音 ID |
| seq | int | 登录奖励序号 |
| grantType | str | 登录奖励类型 |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总登录奖励信息，返回以登录奖励 ID 为字段名、 `LoginCampaignsAllInfo` 为字段值的信息字典， `LoginCampaignsAllInfo` 为从 [`LoginCampaignInfo`](./logincampaigns/#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `LoginCampaignsAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以登录奖励 ID 为字段名、 [`NoneDict`](/typing/#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 1 | `caption` |
| 5 | `closedAt` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, LoginCampaignsAllInfo | NoneDict]`

## class LoginCampaigns() {#logincampaigns}

登录奖励类，包含各种登录奖励相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 登录奖励 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取登录奖励信息。

<Badge type="info">返回值:</Badge> [`LoginCampaignInfo`](./logincampaigns/#info)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取登录奖励的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_background() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |

获取登录奖励背景图像资源。

<Badge type="info">返回值:</Badge> `bytes`
