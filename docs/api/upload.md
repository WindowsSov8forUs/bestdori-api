# upload 文件

文件下载上传操作模块。

```python
from bestdori import upload
```

## download() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| hash | str | - | 文件名 (哈希值) |
| me <Badge type="info">keyword</Badge> | Optional[[Me](./user/#me)] | `None` | 登录用户类 |

获取文件字节数据。

<Badge type="info">返回值:</Badge> `bytes`

## hash_to_url()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| hash | str | - | 文件名 (哈希值) |

构建 Bestdori! 数据库的文件下载链接。

<Badge type="info">返回值:</Badge> `str`


## class Upload()

文件上传类，包含上传文件的相关操作。

### def __init__()

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| file_bytes | bytes | - | 文件字节数据 |
| name | str | - | 文件名 |
| reader | BufferedReader | - | 文件读取流 |
| me <Badge type="info">keyword</Badge> | [Me](./user/#me) | - | 登录用户类 |

### def from_path() <Badge type="info">classmethod</Badge>

| 参数名 | 类型 | 默认值 | 描述 |
|:------|:----:|:-----:|:-----|
| path | str \| Path | - | 文件路径 |
| me <Badge type="info">keyword</Badge> | [Me](./user/#me) | - | 登录用户类 |

通过文件路径创建上传类。

<Badge type="info">返回值:</Badge> [`Upload`](#upload)

### def upload() <Badge type="tip">[async](/fast-start/#async-sync)</Badge>

上传文件。返回值为上传后的文件哈希值 (可用以构建下载链接) 。

<Badge type="info">返回值:</Badge> `str`
