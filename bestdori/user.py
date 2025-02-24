'''`bestdori.user`

BanG Dream! 歌曲相关操作'''
from http.cookies import SimpleCookie
from typing import TYPE_CHECKING, Self, Literal, Optional

from . import post
from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import PostList, UserInfo, UserMeInfo

API = get_api('bestdori.api')

# 用户类
class User:
    '''用户类

    参数:
        username (str): 用户名
    '''
    # 初始化
    def __init__(self, username: str) -> None:     
        self.username: str = username
        '''用户名'''
        self.__info: Optional['UserInfo'] = None
        '''用户信息'''
        return
    
    # 获取用户实例
    @classmethod
    def get(cls, username: str) -> Self:
        '''获取用户对象

        返回:
            Self: 用户对象
        '''
        user = cls(username)
        user.get_info()
        
        return user
    
    # 异步获取用户实例
    @classmethod
    async def get_async(cls, username: str) -> Self:
        '''获取用户对象

        返回:
            Self: 用户对象
        '''
        user = cls(username)
        await user.get_info_async()
        
        return user
    
    def get_info(self) -> 'UserInfo':
        '''获取用户信息

        返回:
            UserInfo: 用户信息
        '''
        response = Api(
            API['user']['info']
        ).get(params={'username': self.username})
        self.__info = response.json()
        
        return self.info
    
    async def get_info_async(self) -> 'UserInfo':
        '''获取用户信息

        返回:
            UserInfo: 用户信息
        '''
        response = await Api(
            API['user']['info']
        ).aget(params={'username': self.username})
        self.__info = response.json()
        
        return self.info
    
    @property
    def info(self) -> 'UserInfo':
        '''用户信息'''
        if self.__info is None:
            raise ValueError(f'User \'{self.username}\' info were not retrieved.')
        return self.__info
    
    @staticmethod
    def login(username: str, password: str) -> 'Me':
        '''登录用户账号。

        参数:
            username (str): 用户名
            password (str): 密码

        返回:
            Me: 自身用户对象
        '''
        me = Me(username, password)
        
        response = Api(
            API['user']['login']
        ).post(data={'username': me.username, 'password': me.password})
        me.__cookies = response.cookies

        response = Api(API['user']['me']).get(cookies=me.cookies)
        me.__me = response.json()
        
        return me
    
    @staticmethod
    async def login_async(username: str, password: str) -> 'Me':
        '''登录用户账号。

        参数:
            username (str): 用户名
            password (str): 密码

        返回:
            Me: 自身用户对象
        '''
        me = Me(username, password)
        
        response = await Api(
            API['user']['login']
        ).apost(data={'username': me.username, 'password': me.password})
        me.__cookies = response.cookies
        
        response = await Api(API['user']['me']).aget(cookies=me.cookies)
        me.__me = response.json()
        
        return me
    
    # 获取用户帖子
    def get_posts(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> 'PostList':
        '''获取用户帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # List[PostListPost] 列举出的帖子
                }
                ```
        '''
        return post.get_list(
            username=self.username, limit=limit, offset=offset, order=order
        )
    
    # 异步获取用户帖子
    async def get_posts_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> 'PostList':
        '''获取用户帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # List[PostListPost] 列举出的帖子
                }
                ```
        '''
        return await post.get_list_async(
            username=self.username, limit=limit, offset=offset, order=order
        )
    
    # 获取用户谱面
    def get_charts(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
    ) -> 'PostList':
        '''获取用户谱面

        参数:
            limit (int, optional): 展示出的谱面数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个谱面，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 谱面排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的谱面总数
                    "posts": ... # List[PostListPost] 列举出的谱面
                }
                ```
        '''
        return post.get_list(
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
    ) -> 'PostList':
        '''获取用户谱面

        参数:
            limit (int, optional): 展示出的谱面数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个谱面，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 谱面排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的谱面总数
                    "posts": ... # List[PostListPost] 列举出的谱面
                }
                ```
        '''
        return await post.get_list_async(
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
    ) -> 'PostList':
        '''获取用户文本帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # List[PostListPost] 列举出的帖子
                }
                ```
        '''
        return post.get_list(
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
    ) -> 'PostList':
        '''获取用户文本帖子

        参数:
            limit (int, optional): 展示出的帖子数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的帖子总数
                    "posts": ... # List[PostListPost] 列举出的帖子
                }
                ```
        '''
        return await post.get_list_async(
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
    ) -> 'PostList':
        '''获取用户故事

        参数:
            limit (int, optional): 展示出的故事数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个故事，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 故事排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的故事总数
                    "posts": ... # List[PostListPost] 列举出的故事
                }
                ```
        '''
        return post.get_list(
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
    ) -> 'PostList':
        '''获取用户故事

        参数:
            limit (int, optional): 展示出的故事数，默认 20
            offset (int, optional): 忽略前面的 `offset` 个故事，默认 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 故事排序，默认时间倒序

        返回:
            PostList: 获取结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的故事总数
                    "posts": ... # List[PostListPost] 列举出的故事
                }
                ```
        '''
        return await post.get_list_async(
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
        self.__me: Optional['UserMeInfo'] = None
        '''用户自我信息'''
        return
    
    # 用户 Cookies
    @property
    def cookies(self) -> SimpleCookie:
        '''用户 Cookies'''
        if self.__cookies is None:
            raise ValueError(f'User {self.username} has not logged in.')
        return self.__cookies
    
    # 用户自我信息
    @property
    def me(self) -> 'UserMeInfo':
        '''用户自我信息'''
        if self.__me is None:
            raise ValueError(f'User {self.username} has not logged in.')
        return self.__me
    
    def update_info(self, info: 'UserInfo') -> 'UserInfo':
        '''更新用户信息

        参数:
            info (UserInfo): 更新后的用户信息

        返回:
            UserInfo: 更新成功后的用户信息
        '''
        Api(
            API['user']['info']
        ).post(data=dict(info), cookies=self.cookies)
        
        return self.get_info()
    
    async def update_info_async(self, info: 'UserInfo') -> 'UserInfo':
        '''更新用户信息
        
        参数:
            info (UserInfo): 更新后的用户信息
        
        返回:
            UserInfo: 更新成功后的用户信息
        '''
        await Api(
            API['user']['info']
        ).apost(data=dict(info), cookies=self.cookies)
        
        return await self.get_info_async()
