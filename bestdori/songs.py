'''`bestdori.songs`

BanG Dream! 歌曲相关操作'''
from typing import Any, Literal

from httpx._exceptions import HTTPStatusError

from .charts import Chart
from .post import get_list
from .utils.utils import ASSETS, API
from .utils.network import Assets, Api
from .exceptions import (
    NoDataException,
    DiffNotExistError,
    SongNotExistError
)

# 获取总歌曲信息
def get_all(index: Literal[0, 5, 7]=5) -> dict[str, dict[str, Any]]:
    '''获取总歌曲信息

    参数:
        index (Literal[0, 5], optional): 指定获取哪种 `all.json`
            `0`: 仅获取所有已有歌曲 ID `all.0.json`
            `5`: 获取所有已有歌曲的简洁信息 `all.5.json`，默认为该项
            `7`: 获取所有已有歌曲的较为详细信息 `all.7.json`

    返回:
        dict[str, dict[str, Any]]: 获取到的总歌曲信息
    '''
    return Api(API['songs']['all'].format(index=index)).request('get').json()

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
        server: Literal['jp', 'en', 'tw', 'cn', 'kr']
    ) -> None:
        '''歌曲封面类'''
        self._index: int = index
        '''数据包序列号'''
        self._jacket_image: str = jacket_image
        '''封面文件名'''
        self._server: Literal['jp', 'en', 'tw', 'cn', 'kr'] = server
        '''封面所在服务器'''
        return
    
    # 获取封面 url
    @property
    def url(self) -> str:
        '''获取封面 url'''
        return Assets(
            ASSETS['songs']['musicjacket'].format(
                index=self._index, jacket_image=self._jacket_image
            ), self._server
        ).get_url()
    
    # 获取封面字节数据
    @property
    def bytes(self) -> bytes:
        '''获取封面字节数据'''
        return Assets(
            ASSETS['songs']['musicjacket'].format(
                index=self._index, jacket_image=self._jacket_image
            ), self._server
        ).get()

# 歌曲类
class Song:
    '''歌曲类

    参数:
        id_ (int): 歌曲 ID
    '''
    # 初始化
    def __init__(self, id_: int) -> None:
        '''歌曲类

        参数:
            id_ (int): 歌曲 ID
        '''
        self.id: int = id_
        '''歌曲 ID'''
        self._info: dict[str, Any] = {}
        '''歌曲信息'''
        # 检测 ID 是否存在
        all_id = get_all(0)
        if not str(id_) in all_id.keys():
            raise SongNotExistError(id_)
        return
    
    # 获取歌曲信息
    def get_info(self) -> dict[str, Any]:
        '''获取歌曲信息

        返回:
            dict[str, Any]: 歌曲详细信息
        '''
        if len(self._info) <= 0:
            # 如果没有歌曲信息存储
            response = Api(
                API['songs']['info'].format(id=self.id)
            ).request('get')
            self._info = dict(response.json())
        return self._info
    
    # 获取歌曲所在服务器
    @property
    def server(self) -> Literal['jp', 'en', 'tw', 'cn', 'kr']:
        '''获取歌曲所在服务器

        返回:
            Literal[&#39;jp&#39;, &#39;en&#39;, &#39;tw&#39;, &#39;cn&#39;, &#39;kr&#39;]: 歌曲所在服务器
        '''
        info = self.get_info()
        # 获取 publishedAt 数据
        if (published_at := info.get('publishedAt', None)) is None:
            raise NoDataException('歌曲发布时间')
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('歌曲服务器')
    
    # 获取歌曲名称
    @property
    def name(self) -> str:
        '''获取歌曲名称

        返回:
            str: 歌曲名称
        '''
        info = self.get_info()
        # 获取 musicTitle 数据
        if (music_title := info.get('musicTitle', None)) is None:
            raise NoDataException('歌曲名称')
        # 获取第一个非 None 歌曲名称
        try:
            return next(filter(lambda x: x is not None, music_title))
        except StopIteration:
            raise NoDataException('歌曲名称')
    
    # 获取歌曲谱面
    def get_chart(
        self,
        diff: Literal['easy', 'normal', 'hard', 'expert', 'special']='expert'
    ) -> Chart:
        '''获取歌曲谱面

        参数:
            diff (Literal[&#39;easy&#39;, &#39;normal&#39;, &#39;hard&#39;, &#39;expert&#39;, &#39;special&#39;], optional): 难度名称

        返回:
            Chart: 获取到的谱面对象
        '''
        try:
            chart = Chart.get_chart(self.id, diff)
            return chart
        except HTTPStatusError as e:
            if e.response.status_code == 404:
                # 难度不存在
                raise DiffNotExistError(diff)
            else:
                raise e
    
    # 获取歌曲封面
    def get_jacket(self) -> list[Jacket]:
        '''获取歌曲封面

        返回:
            Jacket: 歌曲封面对象 `Jacket`
        '''
        # 获取数据包序列号
        quotient, remainder = divmod(self.id, 10)
        if remainder == 0:
            index = self.id
        else:
            index = (quotient + 1) * 10
        
        info = self.get_info()
        if (jacket_image := info.get('jacketImage', None)) is None:
            raise NoDataException('歌曲封面资源')
        jacket: list[Jacket] = []
        
        for image in jacket_image:
            jacket.append(Jacket(index, image, self.server))
        
        return jacket
    
    # 获取歌曲音频
    def get_bgm(self) -> bytes:
        '''获取歌曲音频

        返回:
            bytes: 歌曲音频字节数据 `bytes`
        '''
        return Assets(ASSETS['songs']['sound'].format(id=self.id), self.server).get()
    
    # 获取歌曲评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC'
    ) -> dict[str, Any]:
        '''获取歌曲评论

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
            category_name='SONG_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset
        )
