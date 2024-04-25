'''`bestdori.user`

BanG Dream! 歌曲相关操作'''
from http.cookies import SimpleCookie
from typing import Any, Literal, Optional

from httpx import Response

from . import settings
from .utils.utils import API
from .utils.network import Api
from .post import get_list, get_list_async

# 用户类
class User:
    '''用户类

    参数:
        username (str): 用户名
    '''
    # 初始化
    def __init__(self, username: str) -> None:
        '''用户类

        参数:
            username (str): 用户名
        '''        
        self.username: str = username
        '''用户名'''
        self.__info: dict[str, Any] = {}
        '''用户信息'''
        return
    
    # 获取用户详细信息
    def get_info(self) -> dict[str, Any]:
        '''获取用户详细信息

        返回:
            dict[str, Any]: 用户详细信息
        '''
        response = Api(
            API['user']['info']
        ).get(params={'username': self.username})
        self.__info = dict(response.json())
        return self.__info
    
    # 异步获取用户详细信息
    async def get_info_async(self) -> dict[str, Any]:
        '''获取用户详细信息

        返回:
            dict[str, Any]: 用户详细信息
        '''
        response = await Api(
            API['user']['info']
        ).aget(params={'username': self.username})
        if isinstance(response, Response):
            self.__info = dict(response.json())
        else:
            self.__info = dict(await response.json())
        return self.__info
    
    # 获取用户帖子
    def get_posts(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # list[dict[str, Any]] 列举出的帖子
                }
                ```
        '''
        return get_list(
            username=self.username, limit=limit, offset=offset, order=order
        )
    
    # 异步获取用户帖子
    async def get_posts_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # list[dict[str, Any]] 列举出的帖子
                }
                ```
        '''
        return await get_list_async(
            username=self.username, limit=limit, offset=offset, order=order
        )
    
    # 获取用户谱面
    def get_charts(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户谱面

        参数:
            limit (int, optional): 展示出的谱面数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个谱面，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 谱面排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的谱面总数
                    "posts": ... # list[dict[str, Any]] 列举出的谱面
                }
                ```
        '''
        return get_list(
            username=self.username,
            category_name='SELF_POST',
            category_id='chart',
            limit=limit,
            offset=offset,
            order=order
        )
    
    # 异步获取用户谱面
    async def get_charts_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户谱面

        参数:
            limit (int, optional): 展示出的谱面数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个谱面，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 谱面排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的谱面总数
                    "posts": ... # list[dict[str, Any]] 列举出的谱面
                }
                ```
        '''
        return await get_list_async(
            username=self.username,
            category_name='SELF_POST',
            category_id='chart',
            limit=limit,
            offset=offset,
            order=order
        )
    
    # 获取用户文本帖子
    def get_texts(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户文本帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # list[dict[str, Any]] 列举出的帖子
                }
                ```
        '''
        return get_list(
            username=self.username,
            category_name='SELF_POST',
            category_id='text',
            limit=limit,
            offset=offset,
            order=order
        )
    
    # 异步获取用户文本帖子
    async def get_texts_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户文本帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # list[dict[str, Any]] 列举出的帖子
                }
                ```
        '''
        return await get_list_async(
            username=self.username,
            category_name='SELF_POST',
            category_id='text',
            limit=limit,
            offset=offset,
            order=order
        )
    
    # 获取用户故事
    def get_storys(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户故事

        参数:
            limit (int, optional): 展示出的故事数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个故事，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 故事排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的故事总数
                    "posts": ... # list[dict[str, Any]] 列举出的故事
                }
                ```
        '''
        return get_list(
            username=self.username,
            category_name='SELF_POST',
            category_id='story',
            limit=limit,
            offset=offset,
            order=order
        )
    
    # 异步获取用户故事
    async def get_storys_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> dict[str, Any]:
        '''获取用户故事

        参数:
            limit (int, optional): 展示出的故事数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个故事，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 故事排序，默认时间倒序

        返回:
            dict[str, Any]: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的故事总数
                    "posts": ... # list[dict[str, Any]] 列举出的故事
                }
                ```
        '''
        return await get_list_async(
            username=self.username,
            category_name='SELF_POST',
            category_id='story',
            limit=limit,
            offset=offset,
            order=order
        )

# 自身用户类
class Me(User):
    '''自身用户类

    参数:
        username (str): 用户名
        password (str): 密码
    '''
    # 初始化
    def __init__(self, username: str, password: str) -> None:
        '''自身用户类

        参数:
            username (str): 用户名
            password (str): 密码
        '''
        super().__init__(username)
        self.password: str = password
        '''密码'''
        self.__cookies: Optional[SimpleCookie] = None
        '''用户 Cookies'''
        self.__me: dict[str, Any] = {}
        '''用户自我信息'''
        return
    
    # 用户登录
    @classmethod
    def login(cls, username: str, password: str) -> 'Me':
        '''用户登录

        参数:
            username (str): 用户名
            password (str): 密码

        返回:
            Me: 自身用户对象
        '''
        me = cls(username, password)
        response = Api(
            API['user']['login']
        ).post(data={'username': me.username, 'password': me.password})
        me.__cookies = SimpleCookie(response.cookies)
        me.me()
        settings._me = me
        return me
    
    # 用户异步登录
    @classmethod
    async def alogin(cls, username: str, password: str) -> 'Me':
        '''用户登录

        参数:
            username (str): 用户名
            password (str): 密码

        返回:
            Me: 自身用户对象
        '''
        me = cls(username, password)
        response = await Api(
            API['user']['login']
        ).apost(data={'username': me.username, 'password': me.password})
        if isinstance(response, Response):
            me.__cookies = SimpleCookie(response.cookies)
        else:
            me.__cookies = response.cookies
        await me.ame()
        settings._me = me
        return me
    
    # 获取用户 Cookies
    @property
    def cookies(self) -> SimpleCookie:
        '''获取用户 Cookies'''
        if self.__cookies is None:
            raise ValueError(f'用户 {self.username} 未登录。')
        return self.__cookies
    
    # 获取用户自我信息
    def me(self) -> dict[str, Any]:
        '''获取用户自我信息

        返回:
            dict[str, Any]: 自我信息
        '''
        if len(self.__me) == 0:
            response = Api(API['user']['me']).get(cookies=self.cookies)
            self.__me = dict(response.json())
        return self.__me
    
    # 异步获取用户自我信息
    async def ame(self) -> dict[str, Any]:
        '''获取用户自我信息

        返回:
            dict[str, Any]: 自我信息
        '''
        if len(self.__me) == 0:
            response = await Api(API['user']['me']).aget(cookies=self.cookies)
            if isinstance(response, Response):
                self.__me = dict(response.json())
            else:
                self.__me = dict(await response.json())
        return self.__me
