'''`bestdori.ayachan.settings` 设置项模块'''

from typing import Dict, Union, Optional

from bestdori.settings import AsyncClient

proxy: Optional[Union[Dict[str, str], str]] = None
'''代理服务器'''
async_client: AsyncClient = AsyncClient.HTTPX
'''异步客户端

默认为 `httpx`，可选 `aiohttp`
'''
timeout: int = 10
'''超时时间'''
