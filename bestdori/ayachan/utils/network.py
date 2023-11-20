'''`bestdori.ayachan.utils.network`

向 ayachan 发送请求相关模块'''
from json import dumps
from io import BufferedReader
from httpx import Response, Request, Client
from typing import Optional, Literal, Union, cast, Any

# 向 ayachan 发送 API 请求类
class Api:
    '''向 ayachan 发送 API 请求类

    参数:
        api (str): 请求的 API 地址
        
        proxy (Optional[str]): 代理服务器'''
    api: str
    '''请求的 API 地址'''
    proxy: Optional[str]=None
    '''代理服务器'''
    # 初始化
    def __init__(
        self,
        api: str,
        proxy: Optional[str]=None
    ) -> None:
        '''初始化'''
        self.api = api
        self.proxy = proxy
        return
    
    # 请求发送
    def request(
        self,
        method: Literal['get', 'post'],
        *,
        params: Optional[dict[str, Any]]=None,
        data: Optional[dict[str, Any]]=None,
        files: Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]]=None
    ) -> Response:
        '''请求发送

        参数:
            method (Literal[&#39;get&#39;, &#39;post&#39;]): API 调用方法
            
            params (Optional[dict[str, Any]], optional): 调用参数
            
            data (Optional[dict[str, Any]], optional): 调用参数，将以 `json` 字符串形式发送
            
            files (Optional[dict[str, tuple[str, BufferedReader, Optional[str]]]], optional): 发送文件参数

        返回:
            Response: 收到的响应
        '''
        # 处理接收到的 API
        if self.api.startswith('http://') or self.api.startswith('https://'):
            self.api = self.api
        else:
            self.api = 'https://api.ayachan.fun/' + self.api
        # 构建一个请求体
        request = Request(
            method,
            self.api,
            params=params,
            data=(
                cast(dict, dumps(data)) if data is not None and 'sonolus' not in self.api
                else data
            ),
            files=files,
            headers={
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxjpDgorEXUAUIbBN'
            } if 'sonolus' in self.api else None
        )
        # 构建代理服务器字典
        if self.proxy is not None:
            proxies = {'http://': self.proxy, 'https://': self.proxy}
        else:
            proxies = None
        
        # 发送请求并获取响应
        with Client(proxies=cast(dict, proxies)) as client:
            response = client.send(request)
            client.close()
        
        # 处理接收到的响应
        response.raise_for_status()
        return response
