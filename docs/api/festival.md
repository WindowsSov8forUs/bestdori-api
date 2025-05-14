# festival 团队佳节活动数据

团队佳节活动数据获取模块。

```python
from bestdori import festival
```

## 类型定义

### FestivalRotationMusic 团队佳节活动歌曲循环数据 {#rotation-music}

团队佳节活动歌曲循环数据。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| musicId | int | 歌曲 ID |
| startAt | str | 起始时间戳 |
| endAt | str | 终止时间戳 |

### FestivalStage 团队佳节活动舞台数据 {#stage}

团队佳节活动歌曲循环数据。

| 字段名 | 类型 | 描述 |
|:------|:----:|:-----|
| type | str | 舞台类型 |
| startAt | str | 起始时间戳 |
| endAt | str | 终止时间戳 |

## def get_rotation_musics() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 活动 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取团队 LIVE 佳节活动歌曲循环数据 [`FestivalRotationMusic`](./festival/#rotation-music) 。仅在活动类型为团队 LIVE 佳节活动时有效。

<Badge type="info">返回值:</Badge> `List[FestivalRotationMusic]`

## def get_stages() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| id | int | - | 活动 ID |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取团队 LIVE 佳节活动舞台数据 [`FestivalStage`](./festival/#stage) 。仅在活动类型为团队 LIVE 佳节活动时有效。

<Badge type="info">返回值:</Badge> `List[FestivalStage]`
