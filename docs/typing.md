# 类型

```python
from bestdori import typing
```

## 枚举类 {#enum-type}

一些特殊的枚举类数据类型，部分函数参数值与信息字典字段值只会为枚举项中的一项。

### Server 服务器 ID {#server-id}

| 值 | 描述 |
|:---|:----|
| 0 | 日本服务器 |
| 1 | 国际服务器 |
| 2 | 台湾服务器 |
| 3 | 大陆服务器 |
| 4 | 韩国服务器 |

### ServerName 服务器名称 {#server-name}

服务器对应的字符串标识。

| 值 | 描述 |
|:---|:----|
| `'jp'` | 日本服务器 |
| `'en'` | 国际服务器 |
| `'tw'` | 台湾服务器 |
| `'cn'` | 大陆服务器 |
| `'kr'` | 韩国服务器 |

### Difficulty 难度 ID {#difficulty-id}

| 值 | 描述 |
|:---|:----|
| 0 | EASY 难度 |
| 1 | NORMAL 难度 |
| 2 | HARD 难度 |
| 3 | EXPERT 难度 |
| 4 | SPECIAL 难度 |

::: details  难度 ID 字符串

#### DifficultyString 难度 ID 字符串 {#difficulty-str}

难度 ID 的字符串，在特定数据中作为字段名使用。

| 值 | 描述 |
|:---|:----|
| `'0'` | EASY 难度 |
| `'1'` | NORMAL 难度 |
| `'2'` | HARD 难度 |
| `'3` | EXPERT 难度 |
| `'4'` | SPECIAL 难度 |

:::

### DifficultyName 难度名称 {#difficulty-name}

| 值 | 描述 |
|:---|:----|
| `'easy'` | EASY 难度 |
| `'normal'` | NORMAL 难度 |
| `'hard'` | HARD 难度 |
| `expert` | EXPERT 难度 |
| `special` | SPECIAL 难度 |

### Order 排序方式 {#order}

| 值 | 描述 |
|:---|:----|
| `'TIME_DESC'` | 时间降序 |
| `'TIME_ASC'` | 时间升序 |

## 定长列表 {#fixed-list}

类型: `List[T | None]` / `List[T | NoneDict]`

从 Bestdori 获取到的信息中会出现的列表类型。列表的长度固定为 5 ，依次对应 5 个服务器中所使用的数据内容。列表中非空元素在绝大多数情况下总是一致的，若对应的服务器不存在相对应的数据，则该项元素值为 `None` 、 [`NoneDict`](./typing#nonedict) 或空列表。

| 下标 | 对应服务器 |
|:-----|:----------|
| 0 | `JP` 日本服务器 |
| 1 | `EN` 国际服务器 |
| 2 | `TW` 台湾服务器 |
| 3 | `CN` 大陆服务器 |
| 4 | `KR` 韩国服务器 |

## 字典

类型: `Dict[str, Any]`

从 Bestdori 获取到的信息中，绝大多数都为字典。 Bestdori API 选择使用 `TypedDict` 为获取到的信息进行类型注释，实际使用中与普通字典数据类型没有区别。

### NoneDict 空字典 {#nonedict}

值恒为 `{}` 的字典。大部分类似 `get_{name}_all()` / `get_{name}_all_async()` 的函数，当传入 `index=0` 参数或其他小值时，会返回仅有以 ID 为字段名、以此种字典为字段值的数据字典。此时字段值不包含任何信息，仅供遍历有效 ID 使用。

### Title 称号 {#title}

称号信息字典。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| id | int | 称号 ID |
| type | str | 称号类型 |
| server | [Server](./typing#server-id) | 称号所在服务器 |

## models 数据模型

Bestdori API 数据模型模块。定义 Bestdori API 中使用的复杂数据模型。

```python
from bestdori import models
```

### content 帖子内容 {#content}

帖子内容数据模型模块。以消息元素形式存储帖子内容。

```python
from models import content
```

#### class Content() <Badge type="info">dataclass</Badge> 基础内容元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | str | 内容元素类型 |

#### class Text() <Badge type="info">dataclass</Badge> 文本元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['text'] | 内容元素类型 |
| data | str | 文本内容 |

#### class Br() <Badge type="info">dataclass</Badge> 换行元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['br'] | 内容元素类型 |

#### class Emoji() <Badge type="info">dataclass</Badge> 表情元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['emoji'] | 内容元素类型 |
| data | str | 表情 ID |

#### class Mention() <Badge type="info">dataclass</Badge> 提及元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['mention'] | 内容元素类型 |
| data | str | 提及用户名 |

#### class Heading() <Badge type="info">dataclass</Badge> 标题元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['heading'] | 内容元素类型 |
| data | str | 标题内容 |
| margin | Literal['top'] | 页边空白位置 |

#### class Image() <Badge type="info">dataclass</Badge> 图片元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['image'] | 内容元素类型 |
| display | int | 显示类型 |
| object | List[str] | 图片网址列表 |

::: details display 可用属性值
| 值 | 描述 |
|:---|:----|
| `0` | 大图 |
| `1` | 缩略图 |
| `2` | 图标 |
:::

#### class Link() <Badge type="info">dataclass</Badge> 链接元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['link'] | 内容元素类型 |
| data | str | 链接地址 |
| target | str | 链接对象 |

::: details target 可用属性值
| 值 | 描述 |
|:---|:----|
| `'url'` | 链接 URL |
| `'character-single'` | 链接角色 |
| `'card-single'` | 链接卡牌 |
| `'costume-single'` | 链接服装 |
| `'event-single'` | 链接活动 |
| `'gacha-single'` | 链接招募 |
| `'song-single'` | 链接歌曲 |
| `'logincampaign-single'` | 链接登录奖励 |
| `'comic-single'` | 链接漫画 |
| `'mission-single'` | 链接任务 |
:::

#### class ListContent() <Badge type="info">dataclass</Badge> 列表元素

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['list'] | 内容元素类型 |
| target | str | 列表对象 |
| display | int | 显示类型 |
| object | List[str] | 列表对象 ID 列表 |

::: details target 可用属性值
| 值 | 描述 |
|:---|:----|
| `'character-info'` | 角色信息 |
| `'card-info'` | 卡牌信息 |
| `'card-icon'` | 卡牌图标 |
| `'costume-info'` | 服装信息 |
| `'event-info'` | 活动信息 |
| `'gacha-info'` | 招募信息 |
| `'song-info'` | 歌曲信息 |
| `'logincampaign-info'` | 登录奖励信息 |
| `'comic-info'` | 漫画信息 |
| `'mission-info'` | 任务信息 |
:::

::: details display 可用属性值
| 值 | 描述 |
|:---|:----|
| `0` | - |
| `1` | - |
| `2` | - |
:::

### note 音符 {#note}

音符数据模型模块。谱面构成的基本元素， [`Chart`](/api/chart#chart) 的基础构成即为 `List[Note]` 。

```python
from models import note
```

#### class BPM() <Badge type="info">dataclass</Badge> BPM 线

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['BPM'] | 音符类型 |
| bpm | float | BPM 值 |
| beat | float | BPM 线所在节拍值 |

#### class Single() <Badge type="info">dataclass</Badge> 单键音符

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['Single'] | 音符类型 |
| beat | float | 节拍值 |
| lane | float | 音符所在轨道 |
| flick | bool | 是否为滑键 |
| skill | bool | 是否为技能音符 |

#### class Directional() <Badge type="info">dataclass</Badge> 方向滑键音符

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['Directional'] | 音符类型 |
| beat | float | 节拍值 |
| lane | float | 音符所在轨道 |
| width | int | 音符宽度 |
| direction | int | 滑键方向 |

::: details direction 可用属性值
| 值 | 描述 |
|:---|:----|
| `'Left'` | 左滑键 |
| `'Right'` | 右滑键 |
:::

#### class Connection() <Badge type="info">dataclass</Badge> 滑条音符节点 {#connection}

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| beat | float | 节拍值 |
| flick | bool | 是否为滑键 |
| skill | bool | 是否为技能音符 |
| hidden | bool | 是否为隐藏音符 |
| lane | float | 音符所在轨道 |
| prev | Optional[[Connection](#connection)] | 前一个音符 |
| next | Optional[[Connection](#connection)] | 后一个音符 |

#### class Slide() <Badge type="info">dataclass</Badge> 滑条音符

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | Literal['Slide'] | 音符类型 |
| connections | List[[Connection](#connection)] | 滑条节点列表 |
| head | [Connection](#connection) | 滑条头 |
| tail | [Connection](#connection) | 滑条尾 |
