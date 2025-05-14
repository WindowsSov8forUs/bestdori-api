# songs 歌曲

歌曲信息获取模块。

```python
from bestdori import songs
```

## 类型定义

### SongInfo 歌曲信息 {#info}

歌曲详细信息字典。 `all.{index}.json` 信息字典为该字典中选取部分字段信息。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| musicTitle | List[str \| None] | 歌曲名[定长列表](/typing#fixed-list) |
| tag | str | 歌曲种类 |
| bandId | int | 歌曲乐队 ID |
| jacketImage | List[str] | 歌曲封面链接列表。某些歌曲会有多个封面 |
| publishedAt | List[str \| None] | 歌曲发布时间戳[定长列表](/typing#fixed-list) |
| closedAt | List[str \| None] | 歌曲下架时间戳[定长列表](/typing#fixed-list) |
| difficulty | Dict[[DifficultyString](/typing#difficulty-string), [Difficulty](#difficulty)] | 歌曲难度信息字典 |
| length | float | 歌曲时长 |
| notes | Dict[[DifficultyString](/typing#difficulty-string), int] | 各难度谱面音符数字典 |
| bpm | Dict[[DifficultyString](/typing#difficulty-string), List[[BPM](#bpm)]] | 各难度谱面 BPM 信息字典 |
| ruby | List[str \| None] | 歌曲名拼写 (平假) [定长列表](/typing#fixed-list) |
| phonetic | List[str \| None] | 歌曲名拼写 (片假) [定长列表](/typing#fixed-list) |
| lyricist | List[str \| None] | 作词者名[定长列表](/typing#fixed-list) |
| composer | List[str \| None] | 作曲者名[定长列表](/typing#fixed-list) |
| arranger | List[str \| None] | 编曲者名[定长列表](/typing#fixed-list) |
| bgmId | int | 歌曲资源文件 ID |
| bgmFile | str | 歌曲资源文件名 |
| achievements | List[[Achievement](#achievement)] | 歌曲成就信息 |
| seq | int | 歌曲序列号 |
| howToGet | List[str \| None] | 获取方式[定长列表](/typing#fixed-list) |
| description | List[str \| None] | 歌曲描述[定长列表](/typing#fixed-list) |

### Difficulty 歌曲难度 {#difficulty}

在该类型结构中，所有标识为 <Badge type="info">NotRequired</Badge> 的字段中，除字段 `publishedAt` 以外的字段都不会出现在通过 [`get_all()`](#get-all) 方法获取到的返回值中，而必定会出现在由 [`get_info()`](#get-info) 方法获取到的返回值中。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| playLevel | int | 难度等级 |
| publishedAt <Badge type="info">NotRequired</Badge> | List[str \| None] | 难度发布时间戳[定长列表](/typing#fixed-list) ，仅对额外添加的 SPECIAL 难度存在 |
| notesQuantity <Badge type="info">NotRequired</Badge> | int | 音符数 |
| scoreC <Badge type="info">NotRequired</Badge> | int | C 判定分数线 |
| scoreB <Badge type="info">NotRequired</Badge> | int | B 判定分数线 |
| scoreA <Badge type="info">NotRequired</Badge> | int | A 判定分数线 |
| scoreS <Badge type="info">NotRequired</Badge> | int | S 判定分数线 |
| scoreSS <Badge type="info">NotRequired</Badge> | int | SS 判定分数线 |
| scoreSSS <Badge type="info">NotRequired</Badge> | int | SSS 判定分数线 |
| multiLiveScore <Badge type="info">NotRequired</Badge> | Dict[[MultiLiveDifficultyField](#multilivedifficultyid-type), [MultiLiveScoreMap](#multilivescoremap)] | 协力演出分数信息 |

### MultiLiveScoreMap 协力演出分数信息 {#multilivescoremap}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| musicId | int | 歌曲 ID |
| musicDifficulty | str | 谱面难度 |
| multiLiveDifficultyId | [MultiLiveDifficultyId](#multilivedifficultyid-type) | 协力演出难度 ID |
| multiLiveDifficultyType | [MultiLiveDifficultyType](#multilivedifficultyid-type) | 协力演出难度类型 |
| scoreC | int | C 判定分数线 |
| scoreB | int | B 判定分数线 |
| scoreA | int | A 判定分数线 |
| scoreS | int | S 判定分数线 |
| scoreSS | int | SS 判定分数线 |
| scoreSSS | int | SSS 判定分数线 |

#### MultiLiveDifficultyId - Type 协力演出难度 ID 与名称对照 {#multilivedifficultyid-type}

`MultiLiveDifficultyId` / `MultiLiveDifficultyField` 与 `MultiLiveDifficultyType` 的对应关系。在获取到的信息中，两者的值总是一一对应的。

| MultiLiveDifficultyId | MultiLiveDifficultyField | MultiLiveDifficultyType |
|:----------------------|:-------------------------|:------------------------|
| `2001` | `'2001'` | `'daredemo'` |
| `2011` | `'2011'` | `'standard'` |
| `2021` | `'2021'` | `'grand'` |
| `2031` | `'2031'` | `'legend'` |

### BPM 歌曲 BPM 信息 {#bpm}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| bpm | float | BPM 值 |
| start | float | BPM 起始节拍值 |
| end | float | BPM 结束节拍值 |

### Achievement 歌曲成就 {#achievement}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| musicId | int | 歌曲 ID |
| achievementType | str | 成就类型 |
| rewardType | str | 奖励类型 |
| quantity | int | 奖励数量 |

## def get_all() <Badge type="tip">[async](/fast-start#async-sync)</Badge> {#get-all}

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `0` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

获取总歌曲信息，返回以歌曲 ID 为字段名、 `SongsAllInfo` 为字段值的信息字典， `SongsAllInfo` 为从 [`SongInfo`](#info) 中截取出的部分信息。根据 `index` 参数值不同，获取到的 `SongsAllInfo` 所包含的信息也不同。

特别地，当 `index` 值为 `0` 时，返回值为以歌曲 ID 为字段名、 [`NoneDict`](/typing#nonedict) 为字段值的字典

::: details index 可用参数值
| 参数值 | 获取字段值末项字段名 |
|:-----:|:-------------------|
| 0 | - |
| 1 | `musicTitle` |
| 5 | `publishedAt` |
| 7 | `bpm` |
| 8 | `arranger` |
:::

<Badge type="info">返回值:</Badge> `Dict[str, SongsAllInfo | NoneDict]`

## class Jacket() {#jacket}

歌曲封面类，包含歌曲封面相关资源整合。

| 属性名 | 类型 | 描述 |
|:------|:----:|:-----|
| url | str | 封面图片链接 |

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | - | 数据包序列号 |
| jacket_image | str | - | 封面图片文件名 |
| server | [ServerName](/typing#server-name) | - | 封面所在服务器名称 |

### def get_bytes() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取封面字节数据。

<Badge type="info">返回值:</Badge> `bytes`

## class Song() {#song}

歌曲类，包含歌曲相关资源整合。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 歌曲 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user#me)] | `None` | 登录用户类 |

### def get_info() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取歌曲信息。

<Badge type="info">返回值:</Badge> [`SongInfo`](#info)

### def get_jacket() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取歌曲封面对象列表 [`Jacket`](#jacket) 。

<Badge type="info">返回值:</Badge> `List[Jacket]`

### def get_chart() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| diff | [DifficultyName](/typing#difficulty-name) | `'expert'` | 难度名称 |

获取歌曲指定难度的谱面对象。

<Badge type="info">返回值:</Badge> [`Chart`](./chart#chart)

### def get_bgm() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取歌曲音频资源文件字节数据。

<Badge type="info">返回值:</Badge> `bytes`

### def get_comment() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| limit | int | 20 | 获取到的帖子数量上限 |
| offset | int | 0 | 获取帖子时的偏移量 |
| order | [Order](/typing#order) | `'TIME_DESC'` | 帖子排序方式 |

获取歌曲的社区评论列表。

<Badge type="info">返回值:</Badge> [`PostList`](./post#list)
