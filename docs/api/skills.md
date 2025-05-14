# skills 技能

社区技能操作模块。

```python
from bestdori import skills
```

## 类型定义

### SkillInfo 技能信息 {#info}

技能详细信息字典。 `all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| simpleDescription | List[str \| None] | 技能描述[定长列表](/typing/#fixed-list) |
| description | List[str \| None] | 技能详细描述[定长列表](/typing/#fixed-list) |
| duration | List[float] | 技能持续时间列表 |
| activationEffect | [ActivationEffect](#activation-effect) | 激活效果 |

### ActivationEffect 激活效果 {#activation-effect}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| activationEffectTypes | [ActivationEffectTypes](#activationeffecttypes) | 激活效果类型 |

### ActivationEffectTypes

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| score | [ActivationEffectTypesScore](#activationeffecttypesscore) | 激活效果数值 |

### ActivationEffectTypesScore

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| activateEffectValue | List[int] | 激活效果数值 |
| activateEffectValueType | str | 激活效果数值类型 |
| activateConfition | str | 激活条件 |

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `10` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取总技能信息，返回以技能 ID 为字段名、 `SkillsAllInfo` 为字段值的信息字典， `SkillsAllInfo` 为从 [`SkillInfo`](#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `SkillsAllInfo` 所包含的信息也不同。

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 2 | `simpleDescription` |
| 5 | `duration` |
| 10 | `activationEffect` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, SkillsAllInfo]`
