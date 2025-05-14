
# 快速使用

以下将以获取社区自制谱面 [[FULL] 光の中へ](https://bestdori.com/community/charts/111533/WindowsSov8-FULL) 的信息为例。

首先，使用以下指令安装本模块：
```bash
$ pip3 install bestdori-api
```
接下来在一个 Python 脚本文件中，使用如下代码获取指定帖子的全部信息（这里我们已知该帖子的 ID 为 `111533`）：
```python
from bestdori.post import Post

def main() -> None:
    # 实例化 Post 类
    p = Post(id='111533')
    # 调用方法获取信息
    info = p.get_details()
    # 打印信息
    print(info)

main()
```
得到的输出内容如下：
```python
{
    'categoryName': 'SELF_POST',
    'categoryId': 'chart',
    'title': '[FULL] 光の中へ',
    'song': {
        'type': 'custom',
        'audio': 'https://bestdori.com/api/upload/file/e4a080f84bfa2ca47b23b390a464c819ec17e70b',
        'cover': 'https://bestdori.com/api/upload/file/e3535ebb4c740c4757371026a1df9ffb08010307'
    },
    'artists': '結束バンド',
    'diff': 4,
    'level': 30,
    'chart': [
        {
            'bpm': 191,
            'beat': 0,
            'type': 'BPM'
        },
        {
            'beat': 192,
            'lane': 3.
            'type': 'Single'
        },
        ...
    ],
    ...
}
```
如果想要获取这个自制谱面的谱面，或者想要获取它的音源与封面，以下代码将会进行获取：
```python
from bestdori.post import Post

def main() -> None:
    # 实例化 Post 类
    p = Post(id='111533')
    # 调用方法获取谱面
    chart = p.get_chart() # 获取的将是一个谱面实例
    # 调用方法获取音源与封面
    info = p.get_song() # 获取的将是一个包含了音源与封面的 bytes 字典

main()
```

## 异步/同步适配 {#async-sync}

**Bestdori API** 中的绝大部分方法都同时存在同步与异步方法，且参数与返回值没有区别。

同步方法与异步方法的方法名固定格式为：

::: code-group
```python [sync]
def {method_name}(...):
    ...

{method_name}(...)
```

```python [async]
async def {method_name}_async(...):
    ...

await {method_name}_async(...)
```
:::

文档将以**同步方法**为主，若方法带有 <Badge type="tip">[async](/fast-start/#async-sync)</Badge> 标识，即代表可通过

```python
await {method_name}_async(...)
```

调用方法的异步版本。
