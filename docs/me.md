# 登录用户验证

对于 Bestdori API 的大部分请求方法都会有一个 `me` 参数，接受一个 [`Me`](/api/user/#me) 对象。在请求时若传入 `me` 参数，则会将用户登录时获取的 `Cookies` 用作请求时的 `Cookies` ，这样有可能会在进行大批量请求时避免被 Bestdori! 服务器限制请求；对于部分获取的用户指定型数据（如是否喜欢了某个帖子），传入 `me` 参数也能够正确地获取对应的数据；在进行如发表帖子、发表谱面、发表评论等用户指定操作时，`me` 参数的传入是必须的。

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

## 用户验证

Bestdori! 的用户验证仅通过验证 `Cookies` 完成。实际上在[登录](#login)时， `me.login()` 并不是必须的。 `Me` 对象会存储获取到的 `Cookies` ，而当 Bestdori API 使用 `Me` 对象时会检测其是否保存了 `Cookies` ，如果未保存则会自动调用 `login()` / `login_async()` 方法，否则不会进行调用。也就是说，只要能够确保每次使用的都是同一个 `Me` 对象，用户便不需要自行调用任意一次 `login()` / `login_async()` 方法。

不过目前 Bestdori API 未实现 `Cookies` 自动更新，因此当需要更新 `Cookies` 时，仍然需要手动调用 `login()` / `login_async()` 方法。
