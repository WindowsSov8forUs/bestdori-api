# 配置

```python
from bestdori import settings
```

## 配置代理服务器

因为 Bestdori! 与 Ayachan 站点服务器位于不同的网络环境中，根据网络环境不同，有可能需要为两者分离设置代理服务器， Bestdori API 提供了分离配置代理服务器的功能。

```python
settings.proxy = "http://proxy.example.com:8080"
# 配置 Bestdori! 代理服务器

settings.ayachan.proxy = "http://proxy.example.com:8080"
# 配置 Ayachan 代理服务器
```

## 请求超时时间

出于同样的原因，超时时间也同样进行了分离。

```python
settings.timeout = 10
# 配置 Bestdori! 请求超时时间

settings.ayachan.timeout = 10
# 配置 Ayachan 请求超时时间
```
