# songmeta 歌曲 Meta

歌曲 Meta 数据获取模块。

```python
from bestdori import songmeta
```

## 类型定义

### SongMetaInfo 歌曲 Meta 信息 {#info}

歌曲 Meta 信息为一个有着固定格式的字典对象。

对于歌曲 Meta 信息的如下固定格式：

`Dict[SongId, Dict[DifficultyString, Dict[Field, List[float]]]]`

其中 `SongId` 为对应歌曲 ID 的字符串， [`DifficultyString`](/typing/#difficulty-string) 区分同一歌曲不同难度下的不同数值 (仅记录歌曲存在的难度) 。对于内层具体数值字典，字段名 `Field` 值根据 [`get_all()`](#get-all) 方法传入参数不同有不同的可取值，对应的字段值则为对应的数值列表。

## def get_all() <Badge type="tip">[async](/fast-start/#async-sync)</Badge> {#get-all}

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| index | int | `5` | 指定获取的 `JSON` 信息 |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取歌曲 Meta 信息，返回 [`SongMetaInfo`](#info) 信息字典。

::: details index 可用参数值
| 参数值 | `Field` 可取值 |
|:-----:|:-------------------|
| 2 | `7` |
| 5 | `3`, `4`, `5`, `6`, `7`, `8`, `3.5`, `4.5`, `5.5`, `5.6`, `5.7`, `6.2`, `6.4`, `6.5`, `6.8`, `7.2`, `7.5` |
:::

<Badge type="info">返回值:</Badge> [`SongMetaInfo`](#info)
