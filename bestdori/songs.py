'''`bestdori.songs`

BanG Dream! 歌曲相关操作'''
from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional

from . import post
from .user import Me
from .charts import Chart
from .utils import get_api
from .utils.network import Api
from .exceptions import (
    HTTPStatusError,
    NoDataException,
    NotExistException,
)

if TYPE_CHECKING:
    from .typing import (
        NoneDict,
        PostList,
        SongInfo,
        SongsAll1,
        SongsAll5,
        SongsAll7,
        SongsAll8,
        ServerName,
        DifficultyName,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总歌曲信息
@overload
def get_all(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总歌曲信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 获取到的所有已有歌曲 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[1], *, me: Optional[Me] = None) -> 'SongsAll1':
    '''获取总歌曲信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`

    返回:
        SongsAll1: 获取到的所有已有歌曲的曲名信息 `all.1.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'SongsAll5':
    '''获取总歌曲信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`，默认为该项

    返回:
        SongsAll5: 获取到的所有已有歌曲的简洁信息 `all.5.json`
    '''
    ...
@overload
def get_all(index: Literal[7], *, me: Optional[Me] = None) -> 'SongsAll7':
    '''获取总歌曲信息

    参数:
        index (Literal[7]): 指定获取哪种 `all.json`

    返回:
        SongsAll7: 获取到的所有已有歌曲的较为详细信息 `all.7.json`
    '''
    ...
@overload
def get_all(index: Literal[8], *, me: Optional[Me] = None) -> 'SongsAll8':
    '''获取总歌曲信息

    参数:
        index (Literal[8]): 指定获取哪种 `all.json`

    返回:
        SongsAll8: 获取到的所有已有歌曲的详细信息 `all.8.json`
    '''
    ...

def get_all(
        index: Literal[0, 1, 5, 7, 8]=5, *, me: Optional[Me] = None
    ) -> Union[Dict[str, 'NoneDict'], 'SongsAll1', 'SongsAll5', 'SongsAll7', 'SongsAll8']:
    return Api(API['songs']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None
    ).json()

# 异步获取总歌曲信息
@overload
async def get_all_async(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''异步获取总歌曲信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`

    返回:
        Dict[str, NoneDict]: 获取到的所有已有歌曲 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[1], *, me: Optional[Me] = None) -> 'SongsAll1':
    '''异步获取总歌曲信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`

    返回:
        SongsAll1: 获取到的所有已有歌曲的曲名信息 `all.1.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'SongsAll5':
    '''异步获取总歌曲信息

    参数:
        index (Literal[5], optional): 指定获取哪种 `all.json`，默认为该项

    返回:
        SongsAll5: 获取到的所有已有歌曲的简洁信息 `all.5.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[7], *, me: Optional[Me] = None) -> 'SongsAll7':
    '''异步获取总歌曲信息

    参数:
        index (Literal[7]): 指定获取哪种 `all.json`

    返回:
        SongsAll7: 获取到的所有已有歌曲的较为详细信息 `all.7.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[8], *, me: Optional[Me] = None) -> 'SongsAll8':
    '''异步获取总歌曲信息

    参数:
        index (Literal[8]): 指定获取哪种 `all.json`

    返回:
        SongsAll8: 获取到的所有已有歌曲的详细信息 `all.8.json`
    '''
    ...

async def get_all_async(
    index: Literal[0, 1, 5, 7, 8]=5, *, me: Optional[Me] = None
) -> Union[Dict[str, 'NoneDict'], 'SongsAll1', 'SongsAll5', 'SongsAll7', 'SongsAll8']:
    return (await Api(API['songs']['all'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None
    )).json()

# 歌曲封面内部类
class Jacket:
    '''歌曲封面类

    参数:
        url (str): 封面链接
        bytes (bytes): 封面字节数据
    '''
    # 初始化
    def __init__(
        self,
        index: int,
        jacket_image: str,
        server: 'ServerName'
    ) -> None:
        '''歌曲封面类'''
        self._index: int = index
        '''数据包序列号'''
        self._jacket_image: str = jacket_image
        '''封面文件名'''
        self._server: 'ServerName' = server
        '''封面所在服务器'''

        return
    
    # 封面 url
    @property
    def url(self) -> str:
        '''封面 url'''
        return Api(
            ASSETS['songs']['musicjacket'].format(
                server=self._server, index=self._index, jacket_image=self._jacket_image
            )
        ).url
    
    # 获取封面字节数据
    def get_bytes(self) -> bytes:
        '''获取封面字节数据'''
        return Api(
            ASSETS['songs']['musicjacket'].format(
                server=self._server, index=self._index, jacket_image=self._jacket_image
            )
        ).get().content
    
    # 异步获取封面字节数据
    async def get_bytes_async(self) -> bytes:
        '''获取封面字节数据'''
        return (await Api(
            ASSETS['songs']['musicjacket'].format(
                server=self._server, index=self._index, jacket_image=self._jacket_image
            )
        ).aget()).content

# 歌曲类
class Song:
    '''歌曲类

    参数:
        id (int): 歌曲 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''歌曲类

        参数:
            id (int): 歌曲 ID
        '''
        self.id: int = id
        '''歌曲 ID'''
        self.__info: Optional['SongInfo'] = None
        '''歌曲信息'''

        self.__me = me
        return
    
    @property
    def info(self) -> 'SongInfo':
        '''歌曲信息'''
        if self.__info is None:
            raise RuntimeError(f'Song \'{self.id}\' info were not retrieved.')
        return self.__info

    # 获取歌曲信息
    def get_info(self) -> 'SongInfo':
        '''获取歌曲信息

        返回:
            SongInfo: 歌曲详细信息
        '''
        try:
            response = Api(
                API['songs']['info'].format(id=self.id)
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Song {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return self.info
    
    def __get_info__(self) -> 'SongInfo':
        if self.__info is None:
            return self.get_info()
        return self.info

    # 异步获取歌曲信息
    async def get_info_async(self) -> 'SongInfo':
        '''获取歌曲信息

        返回:
            SongInfo: 歌曲详细信息
        '''
        try:
            response = await Api(
                API['songs']['info'].format(id=self.id)
            ).aget(
                cookies=await self.__me.__get_cookies_async__() if self.__me else None
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Song {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return self.info
    
    async def __get_info_async__(self) -> 'SongInfo':
        if self.__info is None:
            return await self.get_info_async()
        return self.info

    @property
    def __server__(self) -> 'ServerName':
        # 获取 publishedAt 数据
        published_at = self.info['publishedAt']
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('song server')
    
    @property
    def __name__(self) -> List[Optional[str]]:
        return self.info['musicTitle']
    
    # 获取歌曲封面
    def get_jacket(self) -> List[Jacket]:
        '''获取歌曲封面'''
        # 获取数据包序列号
        quotient, remainder = divmod(self.id, 10)
        if remainder == 0:
            index = self.id
        else:
            index = (quotient + 1) * 10
        
        info = self.__get_info__()
        jacket_image = info['jacketImage']
        jacket: List[Jacket] = []
        
        for image in jacket_image:
            jacket.append(Jacket(index, image, self.__server__))
        
        return jacket
    
    # 异步获取歌曲封面
    async def get_jacket_async(self) -> List[Jacket]:
        '''获取歌曲封面'''
        # 获取数据包序列号
        quotient, remainder = divmod(self.id, 10)
        if remainder == 0:
            index = self.id
        else:
            index = (quotient + 1) * 10
        
        info = await self.__get_info_async__()
        jacket_image = info['jacketImage']
        jacket: List[Jacket] = []
        
        for image in jacket_image:
            jacket.append(Jacket(index, image, self.__server__))
        
        return jacket
    
    # 获取歌曲谱面
    def get_chart(
        self,
        diff: 'DifficultyName' = 'expert',
    ) -> Chart:
        '''获取歌曲谱面

        参数:
            diff (DifficultyName, optional): 难度名称

        返回:
            Chart: 获取到的谱面对象
        '''
        try:
            chart = Chart.get_chart(self.id, diff, me=self.__me)
            return chart
        except HTTPStatusError as e:
            if e.response.status_code == 404:
                # 难度不存在
                raise NotExistException(f'Difficulty \'{diff}\'')
            else:
                raise e
    
    # 异步获取歌曲谱面
    async def get_chart_async(
        self,
        diff: 'DifficultyName' = 'expert',
    ) -> Chart:
        '''获取歌曲谱面

        参数:
            diff (DifficultyName, optional): 难度名称

        返回:
            Chart: 获取到的谱面对象
        '''
        try:
            chart = await Chart.get_chart_async(self.id, diff, me=self.__me)
            return chart
        except HTTPStatusError as e:
            if e.response.status_code == 404:
                # 难度不存在
                raise NotExistException(f'Difficulty \'{diff}\'')
            else:
                raise
    
    # 获取歌曲音频
    def get_bgm(self) -> bytes:
        '''获取歌曲音频

        返回:
            bytes: 歌曲音频字节数据 `bytes`
        '''
        self.__get_info__()
        return Api(
            ASSETS['songs']['sound'].format(server=self.__server__, id=self.id)
        ).get().content
    
    # 异步获取歌曲音频
    async def get_bgm_async(self) -> bytes:
        '''获取歌曲音频

        返回:
            bytes: 歌曲音频字节数据 `bytes`
        '''
        await self.__get_info_async__()
        return (await Api(
            ASSETS['songs']['sound'].format(server=self.__server__, id=self.id)
        ).aget()).content
    
    # 获取歌曲评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取歌曲评论

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
        return post.get_list(
            category_name='SONG_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 异步获取歌曲评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取歌曲评论

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
        return await post.get_list_async(
            category_name='SONG_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
