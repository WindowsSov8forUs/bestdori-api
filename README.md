<div align="center">

![bestdori-api logo](https://github.com/WindowsSov8forUs/bestdori-api/blob/main/logo.png)

# Bestdori-api

_✨ [Bestdori](https://bestdori.com/) 的各种 API 调用整合，另外附带部分功能 ✨_

**:warning: 该项目仍然急需更新与 Debug ，使用时若遇到 Bug 或其他需要的接口请及时提出**

</div>

<p align="center">

<a href="https://bestdori.com/">
  <img src="https://img.shields.io/badge/bestdori-api-1976D3" alt="license">
</a>

<a href="https://github.com/WindowsSov8forUs/bestdori-api">
  <img src="https://img.shields.io/github/v/release/WindowsSov8forUs/bestdori-api" alt="Latest Release Version">
</a>

<a href="https://github.com/WindowsSov8forUs/bestdori-api/blob/main/LICENSE">
  <img src="https://img.shields.io/github/license/WindowsSov8forUs/bestdori-api" alt="License">
</a>

<a href="https://www.python.org/downloads/">
  <img src="https://img.shields.io/pypi/pyversions/bestdori-api" alt="Python Version">
</a>

<a href="https://pypi.org/project/bestdori-api/">
  <img src="https://img.shields.io/pypi/v/bestdori-api" alt="PyPI Version">
</a>

</p>

> bestdori-api 现已全面支持同步与异步
> 异步使用方法与同步类似，可几乎无缝切换

## 简介

这是一个用 Python 编写的调用 [Bestdori](https://bestdori.com/) 各种 API 与资源下载的库，大致包括了社区帖子的处理以及各种 [BanG Dream！少女乐团派对](https://zh.moegirl.org.cn/BanG_Dream!_%E5%B0%91%E5%A5%B3%E4%B9%90%E5%9B%A2%E6%B4%BE%E5%AF%B9%EF%BC%81) 游戏内资源的获取。
**警告：此模块目前仍然亟待完善与测试，请不要将其当做一个稳定的库使用。**

### 目前已有的 API 与功能

|API 类别|是否完善|支持的内容|
|:-------|:-----:|:------|
|用户|👍👍|登录、查询、帖子获取、信息获取|
|玩家|👍|信息获取|
|帖子|👍👍👍|搜索、获取、发表、评论、喜欢|
|谱面|👍👍👍|社区谱面获取、音源与封面获取、规整化、数据统计、格式互转|
|故事|👍|社区故事获取|
|角色|👍👍|信息获取、资源获取|
|卡牌|👍👍|信息获取、资源获取|
|服装|👍👍|信息获取、资源获取|
|活动|👍👍|信息获取、资源获取|
|活动数据|👍|数据获取|
|招募|👍👍|数据获取、资源获取|
|歌曲|👍👍|信息获取、资源获取|
|歌曲 Meta|👍|数据获取|
|登录奖励|👍👍|信息获取、资源获取|
|自选券|👍|信息获取|
|漫画|👍👍|信息获取、图片获取|
|任务|👍|信息获取|
|ayachan|👍👍👍|谱面分析、测试服上传、难度分析|
|其他资源|👍|部分独立资源的单独获取|

## 快速使用

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
    # 调用方法获取信息（所有属性化方法在使用前必须获取一次信息）
    p.get_details()
    # 通过属性获取谱面
    chart = p.chart # 获取的将是一个谱面实例
    # 调用方法获取音源与封面
    info = p.get_song() # 获取的将是一个包含了音源与封面的 bytes 字典

main()
```