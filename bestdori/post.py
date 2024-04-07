'''`bestdori.post`

社区帖子相关操作'''
from typing_extensions import overload
from typing import TYPE_CHECKING, Any, Union, Literal, Optional, TypedDict

from .charts import Chart
from .utils.content import Content
from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .exceptions import (
    NoDataException,
    RequestException,
    PostHasNoSongError,
    AssetsNotExistError,
    PostHasNoChartError
)

if TYPE_CHECKING:
    from .user import Me

# 标签类
class Tag(TypedDict):
    '''标签类'''
    type: str
    '''标签类型'''
    data: str
    '''标签数据'''

# 歌曲资源类
class SongRes(TypedDict):
    '''歌曲资源类'''
    audio: Union[bytes, None]
    '''音频字节'''
    cover: Union[bytes, None]
    '''封面字节'''

# 自定义歌曲信息类
class CustomSong(TypedDict):
    '''自定义歌曲信息类'''
    type: Literal['custom']
    '''歌曲类型'''
    audio: Optional[str]
    '''歌曲音频'''
    cover: Optional[str]
    '''歌曲封面'''

# 服务器歌曲信息类
class ProvidedSong(TypedDict):
    '''服务器歌曲信息类'''
    type: Literal['bandori', 'llsif']
    '''歌曲类型'''
    id: int
    '''歌曲 ID'''

# 搜索社区谱面
@overload
def get_list(
    *,
    search: str='',
    category_name: Literal['SELF_POST']='SELF_POST',
    category_id: Literal['chart']='chart',
    tags: list[Tag]=[],
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC',
    limit: int=20,
    offset: int=0
) -> dict[str, Any]:
    '''搜索社区谱面
        ```python
        # 以 'Arghena' 为关键词，搜索社区谱面
        Post.search(search='Arghena', caregory_name='SELF_POST', category_id='chart')
        ```

    参数:
        search (str, optional): 搜索关键词，默认为空
        category_name (Literal[&#39;SELF_POST&#39;], optional): 搜索的帖子类型 `SELF_POST`
        category_id (Literal[&#39;chart&#39;, &#39;text&#39;], optional): 搜索的画廊种类 `chart`
        tags (list[Tag], optional): 搜索的标签，默认为空
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0

    返回:
        dict[str, Any]: 搜索结果
            ```python
            result: bool # 是否有响应
            count: int # 搜索到的谱面总数
            posts: list[dict[str, Any]] # 列举出的谱面
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
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
) -> dict[str, Any]:
    '''搜索用户帖子

    参数:        
        username (str): 用户名
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 帖子排序，默认时间倒序

    返回:
        dict[str, Any]: 搜索结果
            ```python
            result: bool # 是否有响应
            count: int # 搜索到的帖子总数
            posts: list[dict[str, Any]] # 列举出的帖子
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
    tags: Optional[list[Tag]]=None,
    username: Optional[str]=None,
    order: Literal['TIME_DESC', 'TIME_ASC'],
    limit: int=20,
    offset: int=0
) -> dict[str, Any]:
    '''搜索帖子

    参数:        
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;]): 帖子排序
        search (Optional[str], optional): 搜索关键词
        following (Optional[bool], optional): 是否关注
        category_name (Optional[str], optional): 画廊名称
        category_id (Optional[str], optional): 画廊 ID
        tags (Optional[List[Tag]], optional): 帖子标签
        username (Optional[str], optional): 用户名
        limit (int, optional): 展示出的帖子数，默认 20
        offset (int, optional): 忽略前面的 `offset` 个帖子，默认 0

    返回:
        dict[str, Any]: 搜索结果
    '''
    ...

# 搜索帖子
def get_list(**kwargs: Any) -> dict[str, Any]:
    # 去除 None 值字段
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    # 将下划线字段名转换为小驼峰字段名
    kwargs = {
        (
            "".join(x.capitalize() if i > 0 else x for i, x in enumerate(key.split("_")))
        ): value for key, value in kwargs.items() if value is not None
    }
    response = Api(API['post']['list']).request('post', data=kwargs)
    return response.json()

# 搜索标签
def search_tags(
    type_: str,
    data: str='',
    fuzzy: bool=True
) -> list[Tag]:
    '''搜索已有标签

    参数:
        type (str): 标签类型
        data (str, optional): 搜索标签数据关键词
        fuzzy (bool, optional): 是否使用模糊搜索

    返回:
        list[Tag]: 标签类 `Tag` 列表
    '''
    response = Api(API['post']['tag']).request(
        'get',
        params={
            'type': type_,
            'data': data,
            'fuzzy': fuzzy
        }
    )
    if (tags := response.json().get('tags', None)) is not None:
        return [Tag(tag) for tag in tags]
    else:
        raise RequestException(API['post']['tag'], '搜索标签时出现未知错误')

# 发表谱面
@overload
def post(
    me: 'Me',
    *,
    artists: str,
    category_id: Literal['chart']='chart',
    category_name: Literal['SELF_POST']='SELF_POST',
    chart: Chart,
    content: list[Content],
    diff: Literal[0, 1, 2, 3, 4],
    level: int,
    song: Union[CustomSong, ProvidedSong],
    tags: list[Tag]=[],
    title: str
) -> int:
    '''发表谱面

    参数:
        me (Me): 自身用户对象
        artists (str): 歌手
        category_id (Literal[&#39;chart&#39;], optional): 谱面画廊 ID `chart`
        category_name (Literal[&#39;SELF_POST&#39;], optional): 谱面画廊名称 `SELF_POST`
        chart (Chart): 谱面
        content (list[Content]): 帖子内容
        diff (Literal[0, 1, 2, 3, 4]): 难度
        level (int): 等级
        song (Union[CustomSong, ProvidedSong]): 歌曲
        tags (list[Tag], optional): 谱面标签
        title (str): 谱面标题

    返回:
        int: 谱面 ID
    '''
    ...

# 发表文本帖子
@overload
def post(
    me: 'Me',
    *,
    category_id: Literal['text']='text',
    category_name: Literal['SELF_POST']='SELF_POST',
    content: list[Content],
    tags: list[Tag]=[],
    title: str
) -> int:
    '''发表文本帖子

    参数:
        me (Me): 自身用户对象
        category_id (Literal[&#39;text&#39;], optional): 帖子画廊 ID `text`
        category_name (Literal[&#39;SELF_POST&#39;], optional): 帖子画廊名称 `SELF_POST`
        content (list[Content]): 帖子内容
        tags (list[Tag], optional): 帖子标签
        title (str): 帖子标题

    返回:
        int: 帖子 ID
    '''
    ...

# 发表帖子
@overload
def post(
    me: 'Me',
    *,
    artists: Optional[str]=None,
    category_id: str,
    category_name: str,
    chart: Optional[Chart]=None,
    content: list[Content],
    diff: Optional[Literal[0, 1, 2, 3, 4]]=None,
    level: Optional[int]=None,
    song: Optional[Union[CustomSong, ProvidedSong]]=None,
    tags: Optional[list[Tag]]=None,
    title: Optional[str]=None
) -> int:
    '''发表帖子

    参数:
        me (Me): 自身用户对象
        artists (Optional[str], optional): 歌手
        category_id (str): 帖子画廊 ID
        category_name (str): 帖子画廊名称
        chart (Optional[Chart], optional): 谱面
        content (list[Content]): 帖子内容
        diff (Optional[Literal[0, 1, 2, 3, 4]], optional): 难度
        level (Optional[int], optional): 等级
        song (Optional[Union[CustomSong, ProvidedSong]], optional): 歌曲
        tags (Optional[list[Tag]], optional): 帖子标签
        title (Optional[str], optional): 帖子标题

    返回:
        int: 帖子 ID
    '''
    ...

# 发表帖子
def post(
    me: 'Me',
    **kwargs: Any
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
    response = Api(API['post']['post']).request(
        'post',
        cookies=me.cookies,
        data=kwargs
    )
    if (id_ := response.json().get('id', None)) is None:
        raise ValueError('发表帖子时出现未知错误。')
    return id_

# 查询帖子顺序
def find_post(category_name: str, category_id: str, id_: int) -> int:
    '''查询帖子顺序

    参数:
        category_name (str): 画廊名称
        category_id (str): 画廊 ID
        id (int): 查询的帖子 ID

    返回:
        int: 帖子在该画廊的时间顺序
    '''
    params = {
        'categoryName': category_name,
        'categoryId': category_id,
        'id': id_
    }
    response = Api(API['post']['find']).request('get', params=params)
    if (position := response.json().get('position', None)) is None:
        raise ValueError('查询帖子顺序时出现未知错误。')
    return position

# 社区帖子类
class Post:
    '''社区帖子类

    参数:
        id_ (str): 社区帖子 ID
    '''
    # 初始化
    def __init__(self, id_: int) -> None:
        '''社区帖子类

        参数:
            id_ (int): 社区帖子 ID
        '''
        self.id: int = id_
        '''社区帖子 ID'''
        self._post: dict[str, Any] = {}
        '''社区帖子内容'''
        return
    
    # 获取帖子基础信息
    def get_basic(self) -> dict[str, Any]:
        '''获取帖子基础信息

        返回:
            dict[str, Any]: 基础信息
        '''
        response = Api(API['post']['basic']).request('get', params={'id': self.id,})
        return response.json()
    
    # 获取帖子信息
    def get_details(self) -> dict[str, Any]:
        '''获取帖子信息

        返回:
            dict[str, Any]: 帖子详细信息
        '''
        if len(self._post) <= 0:
            # 如果没有帖子内容存储
            response = Api(API['post']['details']).request('get', params={'id': self.id,})
            if (post := response.json().get('post', None)) is not None:
                self._post = dict(post)
            else:
                raise NoDataException('帖子信息')
        return self._post
    
    # 获取谱面对象
    def get_chart(self) -> Chart:
        '''获取谱面对象

        返回:
            Chart: 谱面对象
        '''
        post = self.get_details()
        if (chart := post.get('chart', None)) is not None:
            return Chart.normalize(chart)
        else:
            raise PostHasNoChartError(post)
    
    # 获取帖子标签
    def get_tags(self) -> list[Tag]:
        '''获取帖子标签

        返回:
            list[Tag]: 标签列表
        '''
        if (tags := self.get_details().get('tags', None)) is not None:
            return [Tag(tag) for tag in tags]
        else:
            return []
    
    # 获取帖子内容
    def get_content(self) -> str:
        '''获取帖子内容

        返回:
            str: 帖子内容
        '''
        result: str = ''
        if (content := list(self.get_details().get('content', None))) is not None:
            for seg in content:
                if seg.get('type', None) in ['text', 'link']:
                    result += seg.get('data', '') + '\n'
                elif seg.get('type', None) == 'emoji':
                    result += f':{seg.get("data", "")}:'
                elif seg.get('type', None) == 'br':
                    result += '\n'
        return result
    
    # 获取歌曲信息对象
    def get_song(self) -> SongRes:
        '''获取歌曲信息对象

        返回:
            SongInfo: 歌曲音频与封面字节
        '''
        post = self.get_details()
        if (song := post.get('song', None)) is None:
            raise PostHasNoSongError(post)
        
        if (type_ := song.get('type', None)) is None:
            raise TypeError('该帖子没有歌曲类型。')
        
        result: dict[str, Union[bytes, None]] = {}
        if type_ == 'custom': # 自定义歌曲
            # 获取歌曲音频
            if (audio := song.get('audio', None)) is None:
                result['audio'] = None
            else:
                response = Api(audio).request('get')
                response.raise_for_status()
                result['audio'] = response.content
            # 获取歌曲封面
            if (cover := song.get('cover', None)) is None:
                result['cover'] = None
            else:
                response = Api(cover).request('get')
                response.raise_for_status()
                result['cover'] = response.content
        elif type_ == 'bandori': # BanG Dream! 歌曲
            # 获取歌曲 ID
            if (id_ := song.get('id', None)) is None:
                raise ValueError('未能获取歌曲 ID。')
            # 获取歌曲信息
            info = Api(API['songs']['info'].format(id=id_)).request('get').json()
            # 获取歌曲所在服务器
            if (published_at := info.get('publishedAt', None)) is None:
                raise NoDataException('歌曲发布时间')
            # 根据 publishedAt 数据判断服务器
            if published_at[0] is not None: server = 'jp'
            elif published_at[1] is not None: server = 'en'
            elif published_at[2] is not None: server = 'tw'
            elif published_at[3] is not None: server = 'cn'
            elif published_at[4] is not None: server = 'kr'
            else:
                raise NoDataException('歌曲服务器')
            # 获取歌曲音频
            result['audio'] = Assets(
                ASSETS['songs']['sound'].format(id=id_), server
            ).get()
            # 获取歌曲封面
            # 获取数据包序列号
            quotient, remainder = divmod(id_, 10)
            if remainder == 0:
                index = id_
            else:
                index = (quotient + 1) * 10
            
            if (jacket_image := info.get('jacketImage', None)) is None:
                raise NoDataException('歌曲封面资源')
            result['cover'] = Assets(
                ASSETS['songs']['musicjacket'].format(
                    index=index, jacket_image=jacket_image[-1]
                ), server
            ).get()
        elif type_ == 'llsif': # LoveLive! 歌曲
            # 获取歌曲 ID
            if (id_ := song.get('id', None)) is None:
                raise ValueError('未能获取歌曲 ID。')
            # 获取歌曲信息
            info = Api(API['misc']['llsif'].format(index=10)).request('get').json()[str(id_)]
            # 获取歌曲资源库
            live_icon_asset = info.get('live_icon_asset', None)
            sound_asset = info.get('sound_asset', None)
            # 获取歌曲音频
            result['audio'] = Assets(sound_asset, 'llsif').get()
            # 获取歌曲封面
            result['cover'] = Assets(live_icon_asset, 'llsif').get()
        else:
            raise AssetsNotExistError(f'{type_} 歌曲')
        
        return SongRes(**result)
    
    # 获取帖子评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取帖子评论

        参数:
            limit (int, optional): 展示出的评论数，默认为 20
            offset (int, optional): 忽略前面的 `offset` 条评论，默认为 0
            order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 排序顺序，默认时间顺序

        返回:
            dict[str, Any]: 搜索结果
                ```python
                result: bool # 是否有响应
                count: int # 搜索到的评论总数
                posts: list[dict[str, Any]] # 列举出的评论
                ```
        '''
        return get_list(
            category_name='POST_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
    
    # 评论帖子
    def comment(self, me: 'Me', content: list[Content]) -> int:
        '''评论帖子

        参数:
            me (Me): 自身用户对象
            content (list[Content]): 评论内容

        返回:
            int: 评论 ID
        '''
        return post(
            me,
            category_id=str(self.id),
            category_name='POST_COMMENT',
            content=content
        )
    
    # 喜欢 / 取消喜欢帖子
    def like(self, me: 'Me', value: bool=True) -> None:
        '''喜欢 / 取消喜欢帖子

        参数:
            me (Me): 自身用户对象
            value (bool, optional): 值 `True`: 喜欢帖子 `False`: 取消喜欢帖子
        '''
        Api(API['post']['like']).request(
            'post',
            data={'id': self.id, 'value': value},
            cookies=me.cookies
        )
        return
