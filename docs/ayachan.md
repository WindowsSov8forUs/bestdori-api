# ayachan

Ayachan 站点 API 接口统合，提供了对 Ayachan 站点，包括 Sonolus 测试服在内的 API 的包装。

```python
from bestdori import ayachan
```

## 类型定义

### Version 版本信息 {#version}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| version | str | 版本号 |

### ChartMetrics 谱面分析结果 {#chart-metrics}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| difficulty | [ChartDifficultyStandard](#chart-difficulty-standard) | 难度评级 |
| difficulty_extend | [ChartDifficultyExtend](#chart-difficulty-extend) | 难度评级扩展 |
| metrics | [ChartMetricsStandard](#chart-metrics-standard) | 谱面分析结果 |
| metrics_extend | [ChartMetricsExtend](#chart-metrics-extend) | 谱面分析结果扩展 |

### ChartDifficultyStandard

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| difficulty | float | 加权平均难度评级 |
| max_screen_nps | float | 最大音符密度评级 |
| total_hps | float | 整体每秒击打评级 |
| total_nps | float | 整体每秒音符评级 |

### ChartDifficultyExtend

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| finger_max_hps | int | 最大单手每秒击打相对难度 |
| flick_note_interval | int | 粉键-下个键间隔相对难度 |
| note_flick_interval | int | 上个键-粉键间隔相对难度 |
| max_speed | int | 最大单手移动速度相对难度 |

::: details 可用字段值
| 值 | 描述 |
|:---|:----|
| `-1` | 难度相对加权平均难度偏低 |
| `0` | 难度相对加权平均难度正常 |
| `1` | 难度相对加权平均难度偏高 |
:::

### ChartMetricsStandard

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| bpm_high | float | 最大 BPM |
| bpm_low | float | 最小 BPM |
| distribution | [Distribution](#distribution) | 谱面分布信息 |
| irregular | [RegularType](#regulartype) | 谱面分析情况 |
| irregular_info | str | 无法分析时出现的第一个错误信息 |
| main_bpm | float | 主 BPM |
| max_screen_nps | float | 最大音符密度 |
| note_count | [NoteCount](#notecount) | 音符数量 |
| sp_rhythm | bool | 是否使用了 SP 键 |
| total_hit_note | int | 总击打音符数量 |
| total_hps | float | 每秒击打数量 |
| total_note | int | 总音符数量 |
| total_nps | float | 每秒音符数量 |
| total_time | float | 总时间 |

### Distribution

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| hit | List[int] | 击打分布 |
| note | List[int] | 音符分布 |

### RegularType

| 值 | 描述 |
|:---|:----|
| `0` | 谱面分析失败 |
| `1` | 标准谱面 |
| `2` | 非标准谱面 |

### NoteCount

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| direction_left | int | 左滑方向键数量 |
| direction_right | int | 右滑方向键数量 |
| flick | int | 粉键数量 |
| single | int | 单键数量 |
| slide_end | int | 滑键尾键数量 |
| slide_flick | int | 滑键粉键数量 |
| slide_hidden | int | 滑键隐藏键数量 |
| slide_start | int | 滑键头键数量 |
| slide_tick | int | 滑键中间键数量 |

### ChartMetricsExtend

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| finger_max_hps | int | 最大单手每秒击打数量 |
| flick_note_interval | int | 粉键-下个键间隔 |
| note_flick_interval | int | 上个键-粉键间隔 |
| left_percent | float | 左手击打音符占比 |
| max_speed | int | 最大单手移动速度 |

### Level Sonolus 测试服关卡信息 {#level}

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| item | [LevelItem](#levelitem) | 关卡信息 |
| description | str | 关卡描述 |
| hasCommunity | bool | 是否有社区 |
| leaderboards | List[str] | 排行榜 |
| actions | List[str] | 动作 |
| sections | List[str] | 章节 |

### LevelItem

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| name | str | 名称 |
| source | str | 资源 |
| version | int | 版本 |
| rating | int | 难度等级 |
| title | str | 标题 |
| artists | str | 艺术家 |
| author | str | 谱面作者 |
| tags | List[str] | 标签 |
| engine | [LevelItemEngine](#levelitemengine) | 引擎 |
| useSkin | [EngineUseUnit](#engineuseunit) | 使用的皮肤 |
| useBackground | [EngineUseUnit](#engineuseunit) | 使用的背景 |
| useEffect | [EngineUseUnit](#engineuseunit) | 使用的特效 |
| useParticle | [EngineUseUnit](#engineuseunit) | 使用的粒子 |
| cover | [EngineDataUnit](#enginedataunit) | 封面 |
| bgm | [EngineDataUnit](#enginedataunit) | 背景音乐 |
| data | [EngineDataUnit](#enginedataunit) | 数据 |

### LevelItemEngine

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| name | str | 名称 |
| source | str | 资源 |
| version | int | 版本 |
| title | str | 标题 |
| subtitle | str | 副标题 |
| author | str | 作者 |
| tags | List[str] | 标签 |
| skin | [LevelItemEngineSkin](#levelitemengineskin) | 皮肤 |
| background | [LevelItemEnginBackground](#levelitemenginbackground) | 背景 |
| effect | [LevelItemEngineEffect](#levelitemengineeffect) | 特效 |
| particle | [LevelItemEngineParticle](#levelitemengineparticle) | 粒子 |
| thumbnail | [EngineDataUnit](#enginedataunit) | 缩略图 |
| playData | [EngineDataUnit](#enginedataunit) | 游玩数据 |
| watchData | [EngineDataUnit](#enginedataunit) | 观看数据 |
| previewData | [EngineDataUnit](#enginedataunit) | 预览数据 |
| tutorialData | [EngineDataUnit](#enginedataunit) | 教程数据 |
| configuration | [EngineDataUnit](#enginedataunit) | 配置 |

### LevelItemEngineSkin

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| name | str | 名称 |
| source | str | 资源 |
| version | int | 版本 |
| title | str | 标题 |
| subtitle | str | 副标题 |
| author | str | 作者 |
| tags | List[str] | 标签 |
| thumbnail | [EngineDataUnit](#enginedataunit) | 缩略图 |
| data | [EngineDataUnit](#enginedataunit) | 数据 |
| texture | [EngineDataUnit](#enginedataunit) | 纹理 |

### LevelItemEnginBackground

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| name | str | 名称 |
| source | str | 资源 |
| version | int | 版本 |
| title | str | 标题 |
| subtitle | str | 副标题 |
| author | str | 作者 |
| tags | List[str] | 标签 |
| thumbnail | [EngineDataUnit](#enginedataunit) | 缩略图 |
| data | [EngineDataUnit](#enginedataunit) | 数据 |
| image | [EngineDataUnit](#enginedataunit) | 图片 |
| configuration | [EngineDataUnit](#enginedataunit) | 配置 |

### LevelItemEngineEffect

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| name | str | 名称 |
| source | str | 资源 |
| version | int | 版本 |
| title | str | 标题 |
| subtitle | str | 副标题 |
| author | str | 作者 |
| tags | List[str] | 标签 |
| thumbnail | [EngineDataUnit](#enginedataunit) | 缩略图 |
| data | [EngineDataUnit](#enginedataunit) | 数据 |
| audio | [EngineDataUnit](#enginedataunit) | 音频 |

### LevelItemEngineParticle

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| name | str | 名称 |
| source | str | 资源 |
| version | int | 版本 |
| title | str | 标题 |
| subtitle | str | 副标题 |
| author | str | 作者 |
| tags | List[str] | 标签 |
| thumbnail | [EngineDataUnit](#enginedataunit) | 缩略图 |
| data | [EngineDataUnit](#enginedataunit) | 数据 |
| texture | [EngineDataUnit](#enginedataunit) | 纹理 |

### EngineDataUnit

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| hash | str | 数据哈希值 |
| url | str | 数据链接 |

### EngineUseUnit

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| useDefault | bool | 是否使用默认项 |

## def get_version() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

获取 Ayachan API 版本信息。

<Badge type="info">返回值:</Badge> [`Version`](#version)

## chartmetrics 谱面分析

Ayachan 谱面信息分析获取模块。

```python
from ayachan import chartmetrics
```

### def chart_metrics_bandori() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| chart_id | int | - | 谱面 ID |
| diff_str | [DifficultyName](/typing#difficulty-name) | - | 难度名称 |

分析 BanG Dream! 游戏内谱面。

<Badge type="info">返回值:</Badge> [`ChartMetrics`](#chart-metrics)

### def chart_metrics_bestdori() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| chart_id | int | - | 谱面 ID |

分析 Bestdori! 社区谱面。

<Badge type="info">返回值:</Badge> [`ChartMetrics`](#chart-metrics)

### def chart_metrics_custom() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| diff_str | [DifficultyName](/typing#difficulty-name) | - | 难度名称 |
| chart | [Chart](#chart) \| List[Dict[str, Any]] | - | 谱面对象或原始谱面结构 |

分析自定义谱面。

<Badge type="info">返回值:</Badge> [`ChartMetrics`](#chart-metrics)

## sonolus Sonolus 测试服信息获取模块。

```python
from ayachan import sonolus
```

### def levels_post() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| title | str | - | 标题 |
| bgm | str \| Path | - | 上传歌曲 |
| chart | [Chart](#chart) \| List[Dict[str, Any]] | - | 谱面对象或原始谱面结构 |
| difficulty | int | 25 | 难度等级 |
| hidden | bool | `False` | 是否隐藏 |
| lifetime | int | 21600 | 关卡有效期 (s) |

上传测试服关卡。返回值为上传的测试服关卡 ID 。

<Badge type="info">返回值:</Badge> `int`

### def levels_get() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| uid | int | - | 测试服关卡 ID |

获取测试服关卡谱面。

<Badge type="info">返回值:</Badge> [`Chart`](./chart#chart)

### def levels() <Badge type="tip">[async](/fast-start#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| uid | int | - | 测试服关卡 ID |

获取测试服关卡信息。

<Badge type="info">返回值:</Badge> [`Level`](#level)
