'''`bestdori.post`

社区帖子相关操作'''
from typing_extensions import overload, NotRequired
from typing import TypedDict, Optional, Literal, Union, Any

from .charts import Chart
from .utils.utils import API, ASSETS
from .utils.network import Api, Assets
from .exceptions import (
    AssetsNotExistError,
    PostHasNoChartError,
    PostHasNoSongError
)

# 基础作者信息
class BasicAuthor(TypedDict):
    '''基础作者信息'''
    username: str
    '''用户名'''

# 基础信息类
class Basic(TypedDict):
    '''基础信息类'''
    result: bool
    '''是否有结果'''
    title: NotRequired[Optional[str]]
    '''帖子标题'''
    author: NotRequired[BasicAuthor]
    '''作者信息'''
    code: NotRequired[str]
    '''错误信息'''

# 标签类
class Tag(TypedDict):
    '''标签类'''
    type: str
    '''标签类型'''
    data: str
    '''标签数据'''

# 歌曲信息类
class SongInfo(TypedDict):
    '''歌曲信息类'''
    audio: Union[bytes, None]
    '''音频字节'''
    cover: Union[bytes, None]
    '''封面字节'''

# 搜索社区谱面
@overload
def get_list(
    proxy: Optional[str]=None,
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
        proxy (Optional[str], optional): 代理服务器

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
    proxy: Optional[str]=None,
    *,
    username: str,
    limit: int=20,
    offset: int=0,
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_DESC'
) -> dict[str, Any]:
    '''搜索用户帖子

    参数:
        proxy (Optional[str], optional): 代理服务器
        
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

# 搜索评论
@overload
def get_list(
    proxy: Optional[str]=None,
    *,
    category_id: str,
    category_name: Literal[
        'POST_COMMENT',
        'CHARACTER_COMMENT', 
        'CARD_COMMENT',
        'COSTUME_COMMENT',
        'EVENT_COMMENT',
        'EVENTARCHIVE_COMMENT',
        'GACHA_COMMENT',
        'SONG_COMMENT',
        'LOGINCAMPAIGN_COMMENT',
        'COMIC_COMMENT',
        'MISSION_COMMENT'
    ],
    limit: int=10,
    offset: int=0,
    order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
) -> dict[str, Any]:
    '''搜索评论

    参数:
        proxy (Optional[str], optional): 代理服务器
        
        category_id (str): 对象 ID
        
        category_name (str): 搜索的评论类型
        
        limit (int, optional): 展示出的评论数，默认 10
        
        offset (int, optional): 忽略前面的 `offset` 个评论，默认 0
        
        order (Literal[&#39;TIME_DESC&#39;, &#39;TIME_ASC&#39;], optional): 评论排序，默认时间顺序

    返回:
        dict[str, Any]: 搜索结果
        ```python
        result: bool # 是否有响应
        count: int # 搜索到的评论总数
        posts: list[dict[str, Any]] # 列举出的评论
        ```
    '''
    ...

# 搜索帖子
@overload
def get_list(
    proxy: Optional[str]=None,
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
        proxy (Optional[str], optional): 代理服务器
        
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
def get_list(proxy: Optional[str]=None, **kwargs: Any) -> dict[str, Any]:
    # 去除 None 值字段
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    # 将下划线字段名转换为小驼峰字段名
    kwargs = {
        (
            "".join(x.capitalize() if i > 0 else x for i, x in enumerate(key.split("_")))
        ): value for key, value in kwargs.items() if value is not None
    }
    response = Api(API['post']['list'], proxy).request('post', data=kwargs)
    return response.json()

# 社区帖子类
class Post:
    '''社区帖子类

    参数:
        id_ (str): 社区帖子 ID
        
        proxy (Optional[str], optional): 代理服务器
    '''
    # 初始化
    def __init__(self, id_: str, proxy: Optional[str]=None) -> None:
        '''社区帖子类

        参数:
            id_ (str): 社区帖子 ID
            
            proxy (Optional[str], optional): 代理服务器
        '''
        if not id_.isdigit():
            raise ValueError('帖子 ID 必须为纯数字。')
        self.id: str = id_
        '''社区帖子 ID'''
        self._post: dict[str, Any] = {}
        '''社区帖子内容'''
        self.proxy: Optional[str] = proxy
        '''代理服务器'''
        return
    
    # 获取帖子基础信息
    def get_basic(self) -> Basic:
        '''获取帖子基础信息

        返回:
            Basic: 基础信息
        '''
        response = Api(API['post']['basic'], self.proxy).request('get', params={'id': self.id,})
        return Basic(response.json())
    
    # 获取帖子信息
    def get_details(self) -> dict[str, Any]:
        '''获取帖子信息

        返回:
            dict[str, Any]: 帖子详细信息
        '''
        if len(self._post) <= 0:
            # 如果没有帖子内容存储
            response = Api(API['post']['details'], self.proxy).request('get', params={'id': self.id,})
            if (post := response.json().get('post', None)) is not None:
                self._post = dict(post)
            else:
                raise Exception('无帖子信息获取。')
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
    def get_song(self) -> SongInfo:
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
                try:
                    response = Api(audio, self.proxy).request('get')
                    response.raise_for_status()
                    result['audio'] = response.content
                except Exception as exception:
                    print(f'获取自定义歌曲音频时失败：{type(exception).__name__}: {exception}')
                    result['audio'] = None
            # 获取歌曲封面
            if (cover := song.get('cover', None)) is None:
                result['cover'] = None
            else:
                try:
                    response = Api(cover, self.proxy).request('get')
                    response.raise_for_status()
                    result['cover'] = response.content
                except Exception as exception:
                    print(f'获取自定义歌曲封面时失败：{type(exception).__name__}: {exception}')
                    result['cover'] = None
        elif type_ == 'bandori': # BanG Dream! 歌曲
            # 获取歌曲 ID
            if (id_ := song.get('id', None)) is None:
                raise ValueError('未能获取歌曲 ID。')
            # 获取歌曲信息
            info = Api(API['songs']['info'].format(id=id_), self.proxy).request('get').json()
            # 获取歌曲所在服务器
            if (published_at := info.get('publishedAt', None)) is None:
                raise Exception('无法获取歌曲发布时间。')
            # 根据 publishedAt 数据判断服务器
            if published_at[0] is not None: server = 'jp'
            elif published_at[1] is not None: server = 'en'
            elif published_at[2] is not None: server = 'tw'
            elif published_at[3] is not None: server = 'cn'
            elif published_at[4] is not None: server = 'kr'
            else:
                raise Exception('无法获取歌曲服务器。')
            # 获取歌曲音频
            try:
                result['audio'] = Assets(
                    ASSETS['songs']['sound'].format(id=id_), server, self.proxy
                ).get()
            except Exception as exception:
                print(f'获取 BanG Dream! 歌曲音频时失败：{type(exception).__name__}: {exception}')
                result['audio'] = None
            # 获取歌曲封面
            try:
                # 获取数据包序列号
                quotient, remainder = divmod(int(self.id), 10)
                if remainder == 0:
                    index = self.id
                else:
                    index = str((quotient + 1) * 10)
                
                if (jacket_image := info.get('jacketImage', None)) is None:
                    raise Exception('歌曲封面资源未找到。')
                result['cover'] = Assets(
                    ASSETS['songs']['musicjacket'].format(
                        index=index, jacket_image=jacket_image[-1]
                    ), server, self.proxy
                ).get()
            except Exception as exception:
                print(f'获取 BanG Dream! 歌曲封面时失败：{type(exception).__name__}: {exception}')
                result['cover'] = None
        else:
            raise AssetsNotExistError(f'{type_} 歌曲')
        
        return SongInfo(**result)
    
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
            proxy=self.proxy,
            category_name='POST_COMMENT',
            category_id=self.id,
            order=order,
            limit=limit,
            offset=offset
        )
