'''`bestdori.post`

社区帖子相关操作'''

from dataclasses import dataclass
from typing_extensions import overload
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Union,
    Literal,
    Optional,
)

from .charts import Chart
from .models.content import Content
from .utils import get_api
from .utils.network import Api
from .exceptions import (
    NoDataException,
    PostHasNoSongError,
    AssetsNotExistError,
    PostHasNoChartError,
)

if TYPE_CHECKING:
    from .user import Me
    from .typing import (
        PostTag,
        PostInfo,
        PostList,
        SongInfo,
        LLSifMisc,
        PostBasic,
        PostDetail,
        PostSongCustom,
        PostSongProvided,
        PostTagGetResult,
        PostTagGetResultTag,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 歌曲资源类
@dataclass
class SongResource:
    '''歌曲资源类'''
    audio: Optional[bytes] = None
    '''音频字节'''
    cover: Optional[bytes] = None
    '''封面字节'''

# 搜索社区谱面
@overload
def get_list(
    *,
    search: str='',
    category_name: Literal['SELF_POST']='SELF_POST',
    category_id: Literal['chart']='chart',
    tags: List['PostTag']=[],
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC',
    limit: int=20,
    offset: int=0,
    me: Optional['Me']=None,
) -> 'PostList':
    '''搜索社区谱面
        ```python
        # 以 'Arghena' 为关键词，搜索社区谱面
        Post.search(search='Arghena', caregory_name='SELF_POST', category_id='chart')
        ```

    参数:
        search (str, optional): 搜索关键词，默认为空
        category_name (Literal[&#39;SELF_POST&#39;], optional): 搜索的帖子类型 `SELF_POST`
        category_id (Literal[&#39;chart&#39;, &#39;text&#39;], optional): 搜索的画廊种类 `chart`
        tags (List[PostTag], optional): 搜索的标签，默认为空
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
        me (Optional[Me], optional): 用户验证对象

    返回:
        PostList: 搜索结果
            ```python
            result: bool # 是否有响应
            count: int # 搜索到的谱面总数
            posts: List[PostListPost] # 列举出的谱面
            ```
    '''
    ...
# 搜索用户帖子
@overload
def get_list(
    *,
    username: str,
    limit: int=20,
    offset: int=0,
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC',
    me: Optional['Me']=None,
) -> 'PostList':
    '''搜索用户帖子

    参数:        
        username (str): 用户名
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序
        me (Optional[Me], optional): 用户验证对象

    返回:
        PostList: 搜索结果
            ```python
            result: bool # 是否有响应
            count: int # 搜索到的帖子总数
            posts: List[PostListPost] # 列举出的帖子
            ```
    '''
    ...
# 搜索帖子
@overload
def get_list(
    *,
    search: Optional[str]=None,
    following: Optional[bool]=None,
    category_name: Optional[str]=None,
    category_id: Optional[str]=None,
    tags: Optional[List['PostTag']]=None,
    username: Optional[str]=None,
    order: Literal['TIME_DESC', 'TIME_ASC'],
    limit: int=20,
    offset: int=0,
    me: Optional['Me']=None,
) -> 'PostList':
    '''搜索帖子

    参数:        
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;]): 帖子排序
        search (Optional[str], optional): 搜索关键词
        following (Optional[bool], optional): 是否关注
        category_name (Optional[str], optional): 画廊名称
        category_id (Optional[str], optional): 画廊 ID
        tags (Optional[List[PostTag]], optional): 帖子标签
        username (Optional[str], optional): 用户名
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
        me (Optional[Me], optional): 用户验证对象

    返回:
        PostList: 搜索结果
    '''
    ...

# 搜索帖子
def get_list(**kwargs: Any) -> 'PostList':
    me: 'Me' = kwargs.pop('me', None)
    # 去除 None 值字段
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    # 将下划线字段名转换为小驼峰字段名
    kwargs = {
        (
            "".join(x.capitalize() if i > 0 else x for i, x in enumerate(key.split("_")))
        ): value for key, value in kwargs.items() if value is not None
    }
    response = Api(API['post']['list']).post(
        cookies=me.__get_cookies__() if me else None,
        data=kwargs,
    )
    return response.json()

# 异步搜索社区谱面
@overload
async def get_list_async(
    *,
    search: str='',
    category_name: Literal['SELF_POST']='SELF_POST',
    category_id: Literal['chart']='chart',
    tags: List['PostTag']=[],
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC',
    limit: int=20,
    offset: int=0,
    me: Optional['Me']=None,
) -> 'PostList':
    '''搜索社区谱面
        ```python
        # 以 'Arghena' 为关键词，搜索社区谱面
        Post.search(search='Arghena', caregory_name='SELF_POST', category_id='chart')
        ```

    参数:
        search (str, optional): 搜索关键词，默认为空
        category_name (Literal[&#39;SELF_POST&#39;], optional): 搜索的帖子类型 `SELF_POST`
        category_id (Literal[&#39;chart&#39;, &#39;text&#39;], optional): 搜索的画廊种类 `chart`
        tags (List[PostTag], optional): 搜索的标签，默认为空
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
        me (Optional[Me], optional): 用户验证对象

    返回:
        PostList: 搜索结果
            ```python
            result: bool # 是否有响应
            count: int # 搜索到的谱面总数
            posts: List[PostListPost] # 列举出的谱面
            ```
    '''
    ...
# 异步搜索用户帖子
@overload
async def get_list_async(
    *,
    username: str,
    limit: int=20,
    offset: int=0,
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC',
    me: Optional['Me']=None,
) -> 'PostList':
    '''搜索用户帖子

    参数:        
        username (str): 用户名
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序
        me (Optional[Me], optional): 用户验证对象

    返回:
        PostList: 搜索结果
            ```python
            result: bool # 是否有响应
            count: int # 搜索到的帖子总数
            posts: List[PostListPost] # 列举出的帖子
            ```
    '''
    ...
# 异步搜索帖子
@overload
async def get_list_async(
    *,
    search: Optional[str]=None,
    following: Optional[bool]=None,
    category_name: Optional[str]=None,
    category_id: Optional[str]=None,
    tags: Optional[List['PostTag']]=None,
    username: Optional[str]=None,
    order: Literal['TIME_DESC', 'TIME_ASC'],
    limit: int=20,
    offset: int=0,
    me: Optional['Me']=None,
) -> 'PostList':
    '''搜索帖子

    参数:        
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;]): 帖子排序
        search (Optional[str], optional): 搜索关键词
        following (Optional[bool], optional): 是否关注
        category_name (Optional[str], optional): 画廊名称
        category_id (Optional[str], optional): 画廊 ID
        tags (Optional[List[PostTag]], optional): 帖子标签
        username (Optional[str], optional): 用户名
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
        me (Optional[Me], optional): 用户验证对象

    返回:
        PostList: 搜索结果
    '''
    ...

# 异步搜索帖子
async def get_list_async(**kwargs: Any) -> 'PostList':
    me: 'Me' = kwargs.pop('me', None)
    # 去除 None 值字段
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    # 将下划线字段名转换为小驼峰字段名
    kwargs = {
        (
            "".join(x.capitalize() if i > 0 else x for i, x in enumerate(key.split("_")))
        ): value for key, value in kwargs.items() if value is not None
    }
    response = await Api(API['post']['list']).apost(
        cookies=(await me.__get_cookies_async__()) if me else None,
        data=kwargs,
    )
    return response.json()

# 搜索标签
def search_tags(
    type: str,
    data: str='',
    fuzzy: bool=True,
    *,
    me: Optional['Me']=None,
) -> List['PostTagGetResultTag']:
    '''搜索已有标签

    参数:
        type (str): 标签类型
        data (str, optional): 搜索标签数据关键词
        fuzzy (bool, optional): 是否使用模糊搜索
        me (Optional[Me], optional): 用户验证对象

    返回:
        List[PostTagGetResultTag]: 标签类 `Tag` 列表搜索结果
            ```python
            {
                "type": ..., # 标签类型 (str)
                "data": ..., # 标签数据 (str)
                "count": ..., # 标签数量 (int)
            }
    '''
    response = Api(API['post']['tag']).get(
        cookies=me.__get_cookies__() if me else None,
        params={
            'type': type,
            'data': data,
            'fuzzy': fuzzy
        },
    )
    result: 'PostTagGetResult' = response.json()
    return result['tags']

# 异步搜索标签
async def search_tags_async(
    type: str,
    data: str='',
    fuzzy: bool=True,
    *,
    me: Optional['Me']=None,
) -> List['PostTagGetResultTag']:
    '''搜索已有标签

    参数:
        type (str): 标签类型
        data (str, optional): 搜索标签数据关键词
        fuzzy (bool, optional): 是否使用模糊搜索

    返回:
        List[PostTagGetResultTag]: 标签类 `Tag` 列表搜索结果
            ```python
            {
                "type": ..., # 标签类型 (str)
                "data": ..., # 标签数据 (str)
                "count": ..., # 标签数量 (int)
            }
    '''
    response = await Api(API['post']['tag']).aget(
        cookies=(await me.__get_cookies_async__()) if me else None,
        params={
            'type': type,
            'data': data,
            'fuzzy': fuzzy
        },
    )
    result: 'PostTagGetResult' = response.json()
    return result['tags']

# 发表谱面
@overload
def post(
    *,
    me: 'Me',
    artists: str,
    category_id: Literal['chart']='chart',
    category_name: Literal['SELF_POST']='SELF_POST',
    chart: Chart,
    content: List[Content],
    diff: Literal[0, 1, 2, 3, 4],
    level: int,
    song: Union['PostSongCustom', 'PostSongProvided'],
    tags: List['PostTag']=[],
    title: str
) -> int:
    '''发表谱面

    参数:
        me (Me): 自身用户对象
        artists (str): 歌手
        category_id (Literal[&#39;chart&#39;], optional): 谱面画廊 ID `chart`
        category_name (Literal[&#39;SELF_POST&#39;], optional): 谱面画廊名称 `SELF_POST`
        chart (Chart): 谱面
        content (List[Content]): 帖子内容
        diff (Literal[0, 1, 2, 3, 4]): 难度
        level (int): 等级
        song (Union[PostSongCustom, PostSongProvided]): 歌曲
        tags (List[PostTag], optional): 谱面标签
        title (str): 谱面标题

    返回:
        int: 谱面 ID
    '''
    ...
# 发表文本帖子
@overload
def post(
    *,
    me: 'Me',
    category_id: Literal['text']='text',
    category_name: Literal['SELF_POST']='SELF_POST',
    content: List[Content],
    tags: List['PostTag']=[],
    title: str
) -> int:
    '''发表文本帖子

    参数:
        me (Me): 自身用户对象
        category_id (Literal[&#39;text&#39;], optional): 帖子画廊 ID `text`
        category_name (Literal[&#39;SELF_POST&#39;], optional): 帖子画廊名称 `SELF_POST`
        content (List[Content]): 帖子内容
        tags (List[PostTag], optional): 帖子标签
        title (str): 帖子标题

    返回:
        int: 帖子 ID
    '''
    ...
# 发表帖子
@overload
def post(
    *,
    me: 'Me',
    artists: Optional[str]=None,
    category_id: str,
    category_name: str,
    chart: Optional[Chart]=None,
    content: List[Content],
    diff: Optional[Literal[0, 1, 2, 3, 4]]=None,
    level: Optional[int]=None,
    song: Optional[Union['PostSongCustom', 'PostSongProvided']]=None,
    tags: Optional[List['PostTag']]=None,
    title: Optional[str]=None
) -> int:
    '''发表帖子

    参数:
        me (Me): 自身用户对象
        artists (Optional[str], optional): 歌手
        category_id (str): 帖子画廊 ID
        category_name (str): 帖子画廊名称
        chart (Optional[Chart], optional): 谱面
        content (List[Content]): 帖子内容
        diff (Optional[Literal[0, 1, 2, 3, 4]], optional): 难度
        level (Optional[int], optional): 等级
        song (Optional[Union[PostSongCustom, PostSongProvided]], optional): 歌曲
        tags (Optional[List[PostTag]], optional): 帖子标签
        title (Optional[str], optional): 帖子标题

    返回:
        int: 帖子 ID
    '''
    ...

# 发表帖子
def post(
    *,
    me: 'Me',
    **kwargs: Any,
) -> int:
    # 转换特定字段
    if 'chart' in kwargs:
        kwargs['chart'] = kwargs['chart'].to_list()
    if 'content' in kwargs:
        content = kwargs['content']
        kwargs['content'] = [seg.__dict__ for seg in content]
    
    # 去除 None 值字段
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    # 将下划线字段名转换为小驼峰字段名
    kwargs = {
        (
            "".join(x.capitalize() if i > 0 else x for i, x in enumerate(key.split("_")))
        ): value for key, value in kwargs.items() if value is not None
    }
    response = Api(API['post']['post']).post(
        cookies=me.__get_cookies__(),
        data=kwargs
    )
    return response.json().get('id')

# 异步发表谱面
@overload
async def post_async(
    *,
    me: 'Me',
    artists: str,
    category_id: Literal['chart']='chart',
    category_name: Literal['SELF_POST']='SELF_POST',
    chart: Chart,
    content: List[Content],
    diff: Literal[0, 1, 2, 3, 4],
    level: int,
    song: Union['PostSongCustom', 'PostSongProvided'],
    tags: List['PostTag']=[],
    title: str
) -> int:
    '''发表谱面

    参数:
        me (Me): 自身用户对象
        artists (str): 歌手
        category_id (Literal[&#39;chart&#39;], optional): 谱面画廊 ID `chart`
        category_name (Literal[&#39;SELF_POST&#39;], optional): 谱面画廊名称 `SELF_POST`
        chart (Chart): 谱面
        content (List[Content]): 帖子内容
        diff (Literal[0, 1, 2, 3, 4]): 难度
        level (int): 等级
        song (Union[PostSongCustom, PostSongProvided]): 歌曲
        tags (List[PostTag], optional): 谱面标签
        title (str): 谱面标题

    返回:
        int: 谱面 ID
    '''
    ...
# 异步发表文本帖子
@overload
async def post_async(
    *,
    me: 'Me',
    category_id: Literal['text']='text',
    category_name: Literal['SELF_POST']='SELF_POST',
    content: List[Content],
    tags: List['PostTag']=[],
    title: str
) -> int:
    '''发表文本帖子

    参数:
        me (Me): 自身用户对象
        category_id (Literal[&#39;text&#39;], optional): 帖子画廊 ID `text`
        category_name (Literal[&#39;SELF_POST&#39;], optional): 帖子画廊名称 `SELF_POST`
        content (List[Content]): 帖子内容
        tags (List[PostTag], optional): 帖子标签
        title (str): 帖子标题

    返回:
        int: 帖子 ID
    '''
    ...
# 异步发表帖子
@overload
async def post_async(
    *,
    me: 'Me',
    artists: Optional[str]=None,
    category_id: str,
    category_name: str,
    chart: Optional[Chart]=None,
    content: List[Content],
    diff: Optional[Literal[0, 1, 2, 3, 4]]=None,
    level: Optional[int]=None,
    song: Optional[Union['PostSongCustom', 'PostSongProvided']]=None,
    tags: Optional[List['PostTag']]=None,
    title: Optional[str]=None
) -> int:
    '''发表帖子

    参数:
        me (Me): 自身用户对象
        artists (Optional[str], optional): 歌手
        category_id (str): 帖子画廊 ID
        category_name (str): 帖子画廊名称
        chart (Optional[Chart], optional): 谱面
        content (List[Content]): 帖子内容
        diff (Optional[Literal[0, 1, 2, 3, 4]], optional): 难度
        level (Optional[int], optional): 等级
        song (Optional[Union[PostSongCustom, PostSongProvided]], optional): 歌曲
        tags (Optional[List[PostTag]], optional): 帖子标签
        title (Optional[str], optional): 帖子标题

    返回:
        int: 帖子 ID
    '''
    ...

# 异步发表帖子
async def post_async(
    *,
    me: 'Me',
    **kwargs: Any,
) -> int:
    # 转换特定字段
    if 'chart' in kwargs:
        kwargs['chart'] = kwargs['chart'].to_list()
    if 'content' in kwargs:
        content = kwargs['content']
        kwargs['content'] = [seg.__dict__ for seg in content]
    
    # 去除 None 值字段
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    # 将下划线字段名转换为小驼峰字段名
    kwargs = {
        (
            "".join(x.capitalize() if i > 0 else x for i, x in enumerate(key.split("_")))
        ): value for key, value in kwargs.items() if value is not None
    }
    response = await Api(API['post']['post']).apost(
        cookies=await me.__get_cookies_async__(),
        data=kwargs
    )
    return response.json().get('id')

# 查询帖子顺序
def find_post(category_name: str, category_id: str, id: int, *, me: Optional['Me'] = None) -> int:
    '''查询帖子顺序

    参数:
        category_name (str): 画廊名称
        category_id (str): 画廊 ID
        id (int): 查询的帖子 ID
        me (Optional[Me], optional): 用户验证对象

    返回:
        int: 帖子在该画廊的时间顺序
    '''
    params = {
        'categoryName': category_name,
        'categoryId': category_id,
        'id': id
    }
    response = Api(API['post']['find']).get(
        cookies=me.__get_cookies__() if me else None,
        params=params,
    )
    if (position := response.json().get('position', None)) is None:
        raise ValueError('Unknown error occurred while finding post.')
    return position

# 异步查询帖子顺序
async def find_post_async(category_name: str, category_id: str, id: int, *, me: Optional['Me'] = None) -> int:
    '''查询帖子顺序

    参数:
        category_name (str): 画廊名称
        category_id (str): 画廊 ID
        id (int): 查询的帖子 ID
        me (Optional[Me], optional): 用户验证对象

    返回:
        int: 帖子在该画廊的时间顺序
    '''
    params = {
        'categoryName': category_name,
        'categoryId': category_id,
        'id': id
    }
    response = await Api(API['post']['find']).aget(
        cookies=(await me.__get_cookies_async__()) if me else None,
        params=params,
    )
    if (position := response.json().get('position', None)) is None:
        raise ValueError('Unknown error occurred while finding post.')
    return position

# 社区帖子类
class Post:
    '''社区帖子类

    参数:
        id (str): 社区帖子 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional['Me'] = None) -> None:
        '''社区帖子类

        参数:
            id (int): 社区帖子 ID
        '''
        self.id: int = id
        '''社区帖子 ID'''
        self.__post: Optional['PostInfo'] = None
        '''社区帖子详细内容'''
        self.__basic: Optional['PostBasic'] = None
        '''社区帖子基础信息'''
        
        self.__me: Optional['Me'] = me
        return
    
    @property
    def post(self) -> 'PostInfo':
        '''社区帖子详细内容'''
        if not self.__post:
            raise RuntimeError('Post detail were not retrieved.')
        return self.__post
    
    @property
    def basic(self) -> 'PostBasic':
        '''社区帖子基础信息'''
        if not self.__basic:
            raise RuntimeError('Post basic were not retrieved.')
        return self.__basic
    
    # 获取帖子基础信息
    def get_basic(self) -> 'PostBasic':
        '''获取帖子，只会获取基础信息。

        返回:
            PostBasic: 帖子基础信息
        '''
        response = Api(API['post']['basic']).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
            params={'id': self.id},
        )
        self.__basic = response.json()
        return response.json()
    
    # 异步获取帖子基础信息
    async def get_basic_async(self) -> 'PostBasic':
        '''获取帖子，只会获取基础信息。

        返回:
            PostBasic: 帖子基础信息
        '''
        response = await Api(API['post']['basic']).aget(
            cookies=(await self.__me.__get_cookies_async__()) if self.__me else None,
            params={'id': self.id},
        )
        self.__basic = response.json()
        return response.json()
    
    # 获取帖子信息
    def get_details(self) -> 'PostInfo':
        '''获取帖子信息

        返回:
            PostInfo: 帖子详细信息
        '''
        response = Api(API['post']['details']).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
            params={'id': self.id},
        )
        _detail: 'PostDetail' = response.json()
        self.__post = _detail['post']
        return self.__post
    
    def __get_details__(self) -> 'PostInfo':
        if not self.__post:
            return self.get_details()
        return self.__post
    
    # 异步获取帖子信息
    async def get_details_async(self) -> 'PostInfo':
        '''获取帖子信息

        返回:
            PostInfo: 帖子详细信息
        '''
        response = await Api(API['post']['details']).aget(
            cookies=(await self.__me.__get_cookies_async__()) if self.__me else None,
            params={'id': self.id},
        )
        _detail: 'PostDetail' = response.json()
        self.__post = _detail['post']
        return self.__post
    
    async def __get_details_async__(self) -> 'PostInfo':
        if not self.__post:
            return await self.get_details_async()
        return self.__post
    
    # 获取谱面对象
    def get_chart(self) -> Chart:
        '''获取谱面对象'''
        detail = self.__get_details__()
        if (chart := detail.get('chart', None)) is not None:
            return Chart.from_python(chart)
        else:
            raise PostHasNoChartError(detail)
    
    # 异步获取谱面对象
    async def get_chart_async(self) -> Chart:
        '''获取谱面对象'''
        detail = await self.__get_details_async__()
        if (chart := detail.get('chart', None)) is not None:
            return Chart.from_python(chart)
        else:
            raise PostHasNoChartError(detail)
    
    # 获取帖子标签
    def get_tags(self) -> List['PostTag']:
        '''提取帖子标签'''
        return self.__get_details__()['tags']
    
    # 异步获取帖子标签
    async def get_tags_async(self) -> List['PostTag']:
        '''提取帖子标签'''
        return (await self.__get_details_async__())['tags']
    
    # 获取帖子内容
    def get_content(self) -> str:
        '''获取帖子内容'''
        result: str = ''
        if (content := self.__get_details__().get('content')) is not None:
            for seg in content:
                if seg.get('type', None) in ['text', 'link']:
                    result += seg.get('data', '') + '\n'
                elif seg.get('type', None) == 'emoji':
                    result += f':{seg.get("data", "")}:'
                elif seg.get('type', None) == 'br':
                    result += '\n'
        return result
    
    # 异步获取帖子内容
    async def get_content_async(self) -> str:
        '''获取帖子内容'''
        result: str = ''
        if (content := (await self.__get_details_async__()).get('content')) is not None:
            for seg in content:
                if seg.get('type', None) in ['text', 'link']:
                    result += seg.get('data', '') + '\n'
                elif seg.get('type', None) == 'emoji':
                    result += f':{seg.get("data", "")}:'
                elif seg.get('type', None) == 'br':
                    result += '\n'
        return result
    
    # 获取歌曲信息对象
    def get_song(self) -> SongResource:
        '''获取歌曲信息对象

        返回:
            SongResource: 歌曲音频与封面字节
        '''
        post = self.__get_details__()
        if (song := post.get('song', None)) is None:
            raise PostHasNoSongError(post)
        
        _type = song['type']
        result: Dict[str, Optional[bytes]] = {}
        if _type == 'custom': # 自定义歌曲
            # 获取歌曲音频
            if (audio := song.get('audio', None)) is None:
                result['audio'] = None
            else:
                response = Api(audio).get(
                    cookies=self.__me.__get_cookies__() if self.__me else None,
                )
                result['audio'] = response.content
            # 获取歌曲封面
            if (cover := song.get('cover', None)) is None:
                result['cover'] = None
            else:
                response = Api(cover).get(
                    cookies=self.__me.__get_cookies__() if self.__me else None,
                )
                result['cover'] = response.content
        
        elif _type == 'bandori': # BanG Dream! 歌曲
            # 获取歌曲 ID
            if (id := song.get('id', None)) is None:
                raise ValueError('Unable to get song Id.')
            # 获取歌曲信息
            info: 'SongInfo' = Api(API['songs']['info'].format(id=id)).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
            ).json()
            # 获取歌曲所在服务器
            published_at = info['publishedAt']
            # 根据 publishedAt 数据判断服务器
            if published_at[0] is not None: server = 'jp'
            elif published_at[1] is not None: server = 'en'
            elif published_at[2] is not None: server = 'tw'
            elif published_at[3] is not None: server = 'cn'
            elif published_at[4] is not None: server = 'kr'
            else:
                raise NoDataException('server')
            
            # 获取歌曲音频
            result['audio'] = Api(
                ASSETS['songs']['sound'].format(server=server, id=id)
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
            ).content
            
            # 获取歌曲封面
            # 获取数据包序列号
            quotient, remainder = divmod(id, 10)
            if remainder == 0:
                index = id
            else:
                index = (quotient + 1) * 10
            
            jacket_image = info['jacketImage']
            result['cover'] = Api(
                ASSETS['songs']['musicjacket'].format(
                    server=server, index=index, jacket_image=jacket_image[-1]
                )
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
            ).content
        
        elif _type == 'llsif': # LoveLive! 歌曲
            # 获取歌曲 ID
            if (id := song.get('id', None)) is None:
                raise ValueError('Unable to get song Id.')
            # 获取歌曲信息
            misc: 'LLSifMisc' = Api(API['misc']['llsif'].format(index=10)).get().json()
            _info = misc[str(id)]
            # 获取歌曲资源库
            live_icon_asset = _info.get('live_icon_asset')
            sound_asset = _info.get('sound_asset')
            # 获取歌曲音频
            result['audio'] = Api(ASSETS['llsif']['assets'].format(assets=sound_asset)).get().content
            # 获取歌曲封面
            result['cover'] = Api(ASSETS['llsif']['assets'].format(assets=live_icon_asset)).get().content
        
        else:
            raise AssetsNotExistError(f'Song type \'{_type}\'')
        
        return SongResource(**result)
    
    # 异步获取歌曲信息对象
    async def get_song_async(self) -> SongResource:
        '''获取歌曲信息对象

        返回:
            SongResource: 歌曲音频与封面字节
        '''
        post = await self.__get_details_async__()
        if (song := post.get('song', None)) is None:
            raise PostHasNoSongError(post)
        
        _type = song['type']
        result: Dict[str, Optional[bytes]] = {}
        if _type == 'custom':
            # 获取歌曲音频
            if (audio := song.get('audio', None)) is None:
                result['audio'] = None
            else:
                response = await Api(audio).aget(
                    cookies=(await self.__me.__get_cookies_async__()) if self.__me else None,
                )
                result['audio'] = response.content
            # 获取歌曲封面
            if (cover := song.get('cover', None)) is None:
                result['cover'] = None
            else:
                response = await Api(cover).aget(
                    cookies=(await self.__me.__get_cookies_async__()) if self.__me else None,
                )
                result['cover'] = response.content
        
        elif _type == 'bandori':
            # 获取歌曲 ID
            if (id := song.get('id', None)) is None:
                raise ValueError('Unable to get song Id.')
            # 获取歌曲信息
            info: 'SongInfo' = (await Api(API['songs']['info'].format(id=id)).aget(
                cookies=(await self.__me.__get_cookies_async__()) if self.__me else None,
            )).json()
            # 获取歌曲所在服务器
            published_at = info['publishedAt']
            # 根据 publishedAt 数据判断服务器
            if published_at[0] is not None: server = 'jp'
            elif published_at[1] is not None: server = 'en'
            elif published_at[2] is not None: server = 'tw'
            elif published_at[3] is not None: server = 'cn'
            elif published_at[4] is not None: server = 'kr'
            else:
                raise NoDataException('server')
            
            # 获取歌曲音频
            result['audio'] = (await Api(
                ASSETS['songs']['sound'].format(server=server, id=id)
            ).aget(
                cookies=(await self.__me.__get_cookies_async__()) if self.__me else None,
            )).content
            
            # 获取歌曲封面
            # 获取数据包序列号
            quotient, remainder = divmod(id, 10)
            if remainder == 0:
                index = id
            else:
                index = (quotient + 1) * 10
            
            jacket_image = info['jacketImage']
            result['cover'] = (await Api(
                ASSETS['songs']['musicjacket'].format(
                    server=server, index=index, jacket_image=jacket_image[-1]
                )
            ).aget(
                cookies=(await self.__me.__get_cookies_async__()) if self.__me else None,
            )).content
        
        elif _type == 'llsif':
            # 获取歌曲 ID
            if (id := song.get('id', None)) is None:
                raise ValueError('Unable to get song Id.')
            # 获取歌曲信息
            misc: 'LLSifMisc' = (await Api(API['misc']['llsif'].format(index=10)).aget()).json()
            _info = misc[str(id)]
            # 获取歌曲资源库
            live_icon_asset = _info.get('live_icon_asset')
            sound_asset = _info.get('sound_asset')
            # 获取歌曲音频
            result['audio'] = (await Api(ASSETS['llsif']['assets'].format(assets=sound_asset)).aget()).content
            # 获取歌曲封面
            result['cover'] = (await Api(ASSETS['llsif']['assets'].format(assets=live_icon_asset)).aget()).content
        
        else:
            raise AssetsNotExistError(f'Song type \'{_type}\'')
        
        return SongResource(**result)
    
    # 获取帖子评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取帖子评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            PostList: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[PostListPost] 列举出的评论
                }
                ```
        '''
        return get_list(
            category_name='POST_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 异步获取帖子评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> 'PostList':
        '''获取帖子评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            PostList: 搜索结果
                ```python
                {
                    "result": ... # bool 是否有响应
                    "count": ... # int 搜索到的评论总数
                    "posts": ... # List[PostListPost] 列举出的评论
                }
                ```
        '''
        return await get_list_async(
            category_name='POST_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 评论帖子
    def comment(self, content: List[Content], *, me: Optional['Me'] = None) -> int:
        '''评论帖子

        参数:
            me (Optional[Me], None): 自身用户对象
            content (List[Content]): 评论内容

        返回:
            int: 评论 ID
        '''
        if me is None:
            me = self.__me
        if me is None:
            raise ValueError('Please provide \'me\'.')
        
        return post(
            me=me,
            category_id=str(self.id),
            category_name='POST_COMMENT',
            content=content
        )
    
    # 异步评论帖子
    async def comment_async(self, content: List[Content], *, me: Optional['Me'] = None) -> int:
        '''评论帖子

        参数:
            me (Optional[Me], None): 自身用户对象
            content (List[Content]): 评论内容

        返回:
            int: 评论 ID
        '''
        if me is None:
            me = self.__me
        if me is None:
            raise ValueError('Please provide \'me\'.')
        return await post_async(
            me=me,
            category_id=str(self.id),
            category_name='POST_COMMENT',
            content=content
        )
    
    # 喜欢 / 取消喜欢帖子
    def like(self, value: bool=True, *, me: Optional['Me'] = None) -> None:
        '''喜欢 / 取消喜欢帖子

        参数:
            me (Optional[Me], None): 自身用户对象
            value (bool, optional): 值 `True`: 喜欢帖子 `False`: 取消喜欢帖子
        '''
        if me is None:
            me = self.__me
        if me is None:
            raise ValueError('Please provide \'me\'.')
        Api(API['post']['like']).post(
            data={'id': self.id, 'value': value},
            cookies=me.__get_cookies__()
        )
    
    # 异步喜欢 / 取消喜欢帖子
    async def like_async(self, value: bool=True, *, me: Optional['Me'] = None) -> None:
        '''喜欢 / 取消喜欢帖子

        参数:
            me (Optional[Me], None): 自身用户对象
            value (bool, optional): 值 `True`: 喜欢帖子 `False`: 取消喜欢帖子
        '''
        if me is None:
            me = self.__me
        if me is None:
            raise ValueError('Please provide \'me\'.')
        await Api(API['post']['like']).apost(
            data={'id': self.id, 'value': value},
            cookies=await me.__get_cookies_async__()
        )
