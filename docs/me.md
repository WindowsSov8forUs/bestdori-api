# 登录与会话（vNEXT 重构后）

自重构版本起（参见 README 中的 “破坏性变更” 部分），所有公开 API 已移除历史上的 `me` 形参。取而代之的是：

1. 仅在需要登录态时（如：发表帖子 / 上传资源 / 点赞 / 评论等）手动实例化并登录一次 `Me`；
2. 登录成功后内部通过 `Api.set_cookies(...)` 统一设置全局会话；
3. 其余所有数据获取（卡牌 / 歌曲 / 活动 / 资源下载等）直接调用函数或类方法即可，无需也不支持再传 `me=`。

这样可以：
* 减少冗余参数传递；
* 避免多个 `Me` 对象造成的状态分裂；
* 统一缓存与限流策略；
* 降低调用样板代码。

## 用户登录 {#login}

用户登录仅需要传入用户名与密码即可。

```python
from bestdori.user import Me

me = Me(
    username="username",
    password="password",
)

me.login()
```

## 使用示例

```python
from bestdori.user import Me
from bestdori.post import post

# 1) 登录一次建立全局会话
me = Me("username", "password")
me.login()  # 或: await me.login_async()

# 2) 直接调用其它接口（不再传递 me 参数）
from bestdori.cards import get_all as get_cards
cards = get_cards()          # 获取卡牌汇总

from bestdori.post import Post
p = Post(id='123456')
p.comment(content="test")   # 举例：需要登录态的操作
```

## 迁移旧代码

旧代码中出现的：
```python
get_all(..., me=me)
eventtracker.EventTracker(server, event, me=me)
Upload.from_path(path, me=me)
```
全部改为：
```python
get_all(...)
EventTracker(server, event)
Upload.from_path(path)
```
并确保在首次需要登录操作前已经执行过一次 `me.login()` / `await me.login_async()`。

## Cookies 与刷新

当前仍不内置自动刷新 / 过期检测逻辑；如果会话失效，请再次调用 `login()` / `login_async()` 以更新全局 Cookies。
