# gacha 招募

招募信息处理模块。

```python
from bestdori import gacha
```

## 类型定义

### GachaInfo 招募信息 {#info}

招募详细信息字典。 `all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| gachaName | List[str \| None] | 招募名[定长列表](/typing/#fixed-list) |
| resourceName | str | 资源库名称 |
| bannerAssetBundleName | str | 横幅图片资源库名称 |
| publishedAt | List[str \| None] | 招募发布时间戳[定长列表](/typing/#fixed-list) |
| type | str | 招募类型 |
| newCards | List[int] | 新卡牌 ID 列表 |
| closedAt | List[str \| None] | 招募结束时间戳[定长列表](/typing/#fixed-list) |
| details | List[Dict[str, [Detail](./gacha/#detail)] \| None] | 招募详细信息字典[定长列表](/typing/#fixed-list) |
| rate | List[Dict[str, [Rate](./gacha/#rate)] \| None] | 招募比率字典[定长列表](/typing/#fixed-list) |
| paymentMethods | List[[PaymentMethod](./gacha/#payment-method)] | 付费方式列表 |
| description | List[str \| None] | 招募描述[定长列表](/typing/#fixed-list) |
| annotation | List[str \| None] | 招募注释[定长列表](/typing/#fixed-list) |
| gachaPeriod | List[str \| None] | 招募时间戳[定长列表](/typing/#fixed-list) |
| information | [Information](./gacha/#information) | 招募信息 |

### Detail 招募详细信息 {#detail}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| rarityIndex | int | 稀有度索引 |
| weight | int | 权重 |
| pickup | bool | 是否为 UP 卡 |

### Rate 招募比率 {#rate}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| rate | float | 招募比率 |
| weightTotal | int | 权重总和 |

### PaymentMethod 付费方式 {#payment-method}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| gachaId | int | 招募 ID |
| paymentMethod | str | 付费方式 |
| quantity | int | 购买数量 |
| paymentMethodId | int | 付费方式 ID |
| count | int | 购买次数 |
| behavior | str | 购买行为 |
| pickup | bool | 是否为 UP 卡 |
| costItemQuantity | int | 消耗物品数量 |
| discountType | int | 折扣类型 |
| ticketId <Badge type="info">NotRequired</Badge> | int | 票券 ID |

### Information 招募信息 {#information}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| description | List[str \| None] | 招募详细描述[定长列表](/typing/#fixed-list) |
| term | List[str \| None] | 招募时期说明[定长列表](/typing/#fixed-list) |
| newMemberInfo | List[str \| None] | 新成员说明[定长列表](/typing/#fixed-list) |
| notice | List[str \| None] | 招募备注信息[定长列表](/typing/#fixed-list) |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总招募信息，返回以招募 ID 为字段名、 `GachaAllInfo` 为字段值的信息字典， `GachaAllInfo` 为从 [`GachaInfo`](./gacha/#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `GachaAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以招募 ID 为字段名、 [`NoneDict`](/typing/#nonedict) 为字段值的字典

::: details index 可用参数值

| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 1 | `gachaName` |
| 3 | `newCards` |
| 5 | `closedAt` |

:::

<Badge type="info">返回值:</Badge> `Dict[str, GachaAllInfo | NoneDict]`

## class Gacha() {#gacha}

招募类，包含各种招募相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 招募 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

获取招募信息。

<Badge type="info">返回值:</Badge> [`GachaInfo`](./gacha/#info)

### def get_comment() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing/#order) | `'TIME_ASC'` |

获取招募的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post/#list)

### def get_banner() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |

获取招募缩略图资源。

<Badge type="info">返回值:</Badge> `bytes`

### def get_pickups() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |

获取招募 pickup 图像资源。

<Badge type="info">返回值:</Badge> `List[bytes]`

### def get_logo() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| server | [ServerName](/typing/#server-name) | - | 服务器名 |

获取招募 LOGO 图像资源。

<Badge type="info">返回值:</Badge> `bytes`
