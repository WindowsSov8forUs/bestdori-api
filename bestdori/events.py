'''`bestdori.events`

BanG Dream! 活动相关操作'''
from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional

from . import post
from .user import Me
from .stamps import Stamp
from .utils.network import Api
from .utils import name, get_api
from .eventtracker import EventTracker
from .eventarchives import EventArchive
from .festival import (
    get_stages,
    get_stages_async,
    get_rotation_musics,
    get_rotation_musics_async
)
from .exceptions import (
    HTTPStatusError,
    NoDataException,
    NotExistException,
    ServerNotAvailableError,
)

if TYPE_CHECKING:
    from .typing import (
        Server,
        NoneDict,
        PostList,
        EventInfo,
        EventsAll1,
        EventsAll3,
        EventsAll4,
        EventsAll5,
        EventsAll6,
        ServerName,
        EventTopData,
        FestivalStage,
        FestivalRotationMusic,
    )

API = get_api('bestdori.api')
ASSETS = get_api('bestdori.assets')

# 获取总活动信息
@overload
def get_all(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总活动信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`
        

    返回:
        Dict[str, NoneDict]: 所有已有活动 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[1], *, me: Optional[Me] = None) -> 'EventsAll1':
    '''获取总活动信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll1: 所有已有活动的简洁信息 `all.1.json`
    '''
    ...
@overload
def get_all(index: Literal[3], *, me: Optional[Me] = None) -> 'EventsAll3':
    '''获取总活动信息

    参数:
        index (Literal[3]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll3: 所有已有活动的简洁信息 `all.3.json`
    '''
    ...
@overload
def get_all(index: Literal[4], *, me: Optional[Me] = None) -> 'EventsAll4':
    '''获取总活动信息

    参数:
        index (Literal[4]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll4: 所有已有活动的简洁信息 `all.4.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'EventsAll5':
    '''获取总活动信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll5: 所有已有活动的简洁信息 `all.5.json`
    '''
    ...
@overload
def get_all(index: Literal[6], *, me: Optional[Me] = None) -> 'EventsAll6':
    '''获取总活动信息

    参数:
        index (Literal[6]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll6: 所有已有活动的简洁信息 `all.6.json`
    '''
    ...

def get_all(
    index: Literal[0, 1, 3, 4, 5, 6]=5, *, me: Optional[Me] = None,
) -> Union[Dict[str, 'NoneDict'], 'EventsAll1', 'EventsAll3', 'EventsAll4', 'EventsAll5', 'EventsAll6']:
    return Api(API['events']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None
    ).json()

# 异步获取总活动信息
@overload
async def get_all_async(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总活动信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`
        

    返回:
        Dict[str, NoneDict]: 所有已有活动 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[1], *, me: Optional[Me] = None) -> 'EventsAll1':
    '''获取总活动信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll1: 所有已有活动的简洁信息 `all.1.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[3], *, me: Optional[Me] = None) -> 'EventsAll3':
    '''获取总活动信息

    参数:
        index (Literal[3]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll3: 所有已有活动的简洁信息 `all.3.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[4], *, me: Optional[Me] = None) -> 'EventsAll4':
    '''获取总活动信息

    参数:
        index (Literal[4]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll4: 所有已有活动的简洁信息 `all.4.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'EventsAll5':
    '''获取总活动信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll5: 所有已有活动的简洁信息 `all.5.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[6], *, me: Optional[Me] = None) -> 'EventsAll6':
    '''获取总活动信息

    参数:
        index (Literal[6]): 指定获取哪种 `all.json`
        

    返回:
        EventsAll6: 所有已有活动的简洁信息 `all.6.json`
    '''
    ...

async def get_all_async(
    index: Literal[0, 1, 3, 4, 5, 6]=5, *, me: Optional[Me] = None,
) -> Union[Dict[str, 'NoneDict'], 'EventsAll1', 'EventsAll3', 'EventsAll4', 'EventsAll5', 'EventsAll6']:
    return (await Api(API['events']['all'].format(index=index)).aget(
        cookies=me.__get_cookies__() if me else None
    )).json()

# 活动类
class Event:
    '''活动类

    参数:
        id (int): 活动 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''活动类

        参数:
            id (int): 活动 ID
        '''
        self.id: int = id
        '''活动 ID'''
        self.archive: EventArchive = EventArchive(self.id)
        '''活动档案'''
        self.__info: Optional['EventInfo'] = None
        '''活动信息'''

        self.__me = me
        return
    
    @property
    def info(self) -> 'EventInfo':
        '''活动信息'''
        if not self.__info:
            raise RuntimeError(f'Event \'{self.id}\' info were not retrieved.')
        return self.__info

    # 活动标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''活动标题'''
        return self.info['eventName']
    
    # 活动默认服务器
    @property
    def __server__(self) -> 'ServerName':
        '''活动默认服务器'''
        # 获取 startAt 数据
        start_at = self.info['startAt']
        # 根据 startAt 数据判断服务器
        if start_at[0] is not None: return 'jp'
        elif start_at[1] is not None: return 'en'
        elif start_at[2] is not None: return 'tw'
        elif start_at[3] is not None: return 'cn'
        elif start_at[4] is not None: return 'kr'
        else:
            raise NoDataException('event server')
    
    # 获取对应服务器活动PT&排名追踪器
    def tracker(self, server: 'Server') -> EventTracker:
        '''获取对应服务器活动PT&排名追踪器

        参数:
            server (Server): 指定服务器

        返回:
            EventTracker: 活动追踪器
        '''
        return EventTracker(server, self.id, me=self.__me)

    # 获取活动信息
    def get_info(self) -> 'EventInfo':
        '''获取活动信息

        返回:
            EventInfo: 活动详细信息
        '''
        try:
            response = Api(
                API['events']['info'].format(id=self.id)
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Event {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return self.info
    
    def __get_info__(self) -> 'EventInfo':
        if not self.__info:
            return self.get_info()
        return self.__info
    
    # 异步获取活动信息
    async def get_info_async(self) -> 'EventInfo':
        '''获取活动信息

        返回:
            EventInfo: 活动详细信息
        '''
        try:
            response = await Api(
                API['events']['info'].format(id=self.id)
            ).aget(
                cookies=await self.__me.__get_cookies_async__() if self.__me else None
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'Event {self.id}')
            else:
                raise exception
        
        self.__info = response.json()
        return self.info
    
    async def __get_info_async__(self) -> 'EventInfo':
        if not self.__info:
            return await self.get_info_async()
        return self.__info
    
    # 获取活动评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取活动评论

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
            category_name='EVENT_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 异步获取活动评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取活动评论

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
            category_name='EVENT_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 获取活动缩略图图像
    def get_banner(self, server: 'ServerName') -> bytes:
        '''获取活动缩略图图像

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 活动缩略图图像字节数据 `bytes`
        '''
        info = self.__get_info__()
        # 获取活动数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        start_at = info['startAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'Event \'{name(self)}\'', server)
        return Api(
            ASSETS['event']['banner'].format(
                server=server, asset_bundle_name=asset_bundle_name
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me else None
        ).content
    
    # 异步获取活动缩略图图像
    async def get_banner_async(self, server: 'ServerName') -> bytes:
        '''获取活动缩略图图像

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 活动缩略图图像字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取活动数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        start_at = info['startAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'Event \'{name(self)}\'', server)
        return (await Api(
            ASSETS['event']['banner'].format(
                server=server, asset_bundle_name=asset_bundle_name
            )
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None
        )).content
    
    # 获取活动 logo 图像
    def get_logo(self, server: 'ServerName') -> bytes:
        '''获取活动 logo 图像

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 活动 logo 图像字节数据 `bytes`
        '''
        info = self.__get_info__()
        # 获取活动数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        start_at = info['startAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'Event \'{name(self)}\'', server)
        return Api(
            ASSETS['event']['logo'].format(
                server=server, asset_bundle_name=asset_bundle_name
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
        ).content
    
    # 异步获取活动 logo 图像
    async def get_logo_async(self, server: 'ServerName') -> bytes:
        '''获取活动 logo 图像

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 活动 logo 图像字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取活动数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        start_at = info['startAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'Event \'{name(self)}\'', server)
        return (await Api(
            ASSETS['event']['logo'].format(
                server=server, asset_bundle_name=asset_bundle_name
            )
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None,
        )).content

    # 获取活动主界面图像
    def get_topscreen(self, server: 'ServerName', type: Literal['bg', 'trim']) -> bytes:
        '''获取活动主界面图像

        参数:
            server (ServerName): 指定服务器
            type (Literal[&#39;bg&#39;, &#39;trim&#39;]): 图像类型
                `bg`: 背景图像
                `trim`: 角色图像

        返回:
            bytes: 活动主界面图像字节数据 `bytes`
        '''
        info = self.__get_info__()
        # 获取活动数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        start_at = info['startAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'Event \'{name(self)}\'', server)
        return Api(
            ASSETS['event']['topscreen'].format(
                server=server, asset_bundle_name=asset_bundle_name, type=type
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
        ).content
    
    # 异步获取活动主界面图像
    async def get_topscreen_async(self, server: 'ServerName', type: Literal['bg', 'trim']) -> bytes:
        '''获取活动主界面图像

        参数:
            server (ServerName): 指定服务器
            type (Literal[&#39;bg&#39;, &#39;trim&#39;]): 图像类型
                `bg`: 背景图像
                `trim`: 角色图像

        返回:
            bytes: 活动主界面图像字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取活动数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        start_at = info['startAt']
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if start_at[index] is None:
            raise ServerNotAvailableError(f'Event \'{name(self)}\'', server)
        return (await Api(
            ASSETS['event']['topscreen'].format(
                server=server, asset_bundle_name=asset_bundle_name, type=type
            )
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None,
        )).content
    
    # 获取活动奖励稀有表情
    def get_stamp(self) -> bytes:
        '''获取活动奖励稀有表情

        返回:
            bytes: 活动奖励稀有表情字节数据 `bytes`
        '''
        info = self.__get_info__()
        # 获取活动点数奖励列表
        point_rewards = info['pointRewards']
        # 获取第一个非 None 奖励列表
        try:
            point_reward = next(x for x in point_rewards if x is not None)
        except StopIteration:
            raise NoDataException('event point reward')
        # 获取 rewardType 为 stamp 的活动奖励
        try:
            reward = next(filter(lambda x: x['rewardType'] == 'stamp', point_reward))
        except StopIteration:
            raise ValueError(f'Event {self.id} has no stamp reward.')
        stamp_id = reward.get('rewardId')
        if stamp_id is None:
            raise ValueError(f'Event {self.id} has no stamp reward.')
        # 获取贴纸资源
        stamp = Stamp(stamp_id)
        return stamp.get_stamp(self.__server__)
    
    # 异步获取活动奖励稀有表情
    async def get_stamp_async(self) -> bytes:
        '''获取活动奖励稀有表情

        返回:
            bytes: 活动奖励稀有表情字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取活动点数奖励列表
        point_rewards = info['pointRewards']
        # 获取第一个非 None 奖励列表
        try:
            point_reward = next(x for x in point_rewards if x is not None)
        except StopIteration:
            raise NoDataException('event point reward')
        # 获取 rewardType 为 stamp 的活动奖励
        try:
            reward = next(filter(lambda x: x['rewardType'] == 'stamp', point_reward))
        except StopIteration:
            raise ValueError(f'Event {self.id} has no stamp reward.')
        stamp_id = reward.get('rewardId')
        if stamp_id is None:
            raise ValueError(f'Event {self.id} has no stamp reward.')
        # 获取贴纸资源
        stamp = Stamp(stamp_id)
        return await stamp.get_stamp_async(self.__server__)

    # 获取最新 T10 排名分数线
    @overload
    def get_top(
        self,
        server: 'Server',
        mid: int = 0,
        *,
        interval: int,
    ) -> 'EventTopData':
        '''获取最新 T10 排名分数线

        参数:
            server (Server): 指定服务器
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
            interval (int): 间隔

        返回:
            EventTopData: T10 排名数据
        '''
        ...
    # 获取最终 T10 排名分数线
    @overload
    def get_top(
        self,
        server: 'Server',
        mid: int = 0,
        *,
        latest: Literal[1],
    ) -> 'EventTopData':
        '''获取最终 T10 排名分数线

        参数:
            server (Server): 指定服务器
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
            latest (Literal[1]): 获取最终排名分数线

        返回:
            EventTopData: T10 排名数据
        '''
        ...

    # 获取 T10 排名分数线
    def get_top(
        self,
        server: 'Server',
        mid: int = 0,
        *,
        interval: Optional[int] = None,
        latest: Optional[Literal[1]] = None,
    ) -> 'EventTopData':
        if interval is None:
            if latest is None:
                raise ValueError('Either `interval` or `latest` must be specified.')
            return self.archive.get_top(server, mid)
        if latest is None:
            return self.tracker(server).get_top(mid, interval=interval)
        raise ValueError('Both `interval` and `latest` cannot be specified at the same time.')
    
    # 异步获取最新 T10 排名分数线
    @overload
    async def get_top_async(
        self,
        server: 'Server',
        mid: int = 0,
        *,
        interval: int,
    ) -> 'EventTopData':
        '''异步获取最新 T10 排名分数线

        参数:
            server (Server): 指定服务器
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
            interval (int): 间隔

        返回:
            EventTopData: T10 排名数据
        '''
        ...
    # 异步获取最终 T10 排名分数线
    @overload
    async def get_top_async(
        self,
        server: 'Server',
        mid: int = 0,
        *,
        latest: Literal[1],
    ) -> 'EventTopData':
        '''异步获取最终 T10 排名分数线

        参数:
            server (Server): 指定服务器
            mid (int, optional): 歌曲 ID ，仅在查询歌曲分数排名时为非 `0` 值
            latest (Literal[1]): 获取最终排名分数线

        返回:
            EventTopData: T10 排名数据
        '''
        ...
    
    # 异步获取 T10 排名分数线
    async def get_top_async(
        self,
        server: 'Server',
        mid: int = 0,
        *,
        interval: Optional[int] = None,
        latest: Optional[Literal[1]] = None,
    ) -> 'EventTopData':
        if interval is None:
            if latest is None:
                raise ValueError('Either `interval` or `latest` must be specified.')
            return await self.archive.get_top_async(server, mid)
        if latest is None:
            return await self.tracker(server).get_top_async(mid, interval=interval)
        raise ValueError('Both `interval` and `latest` cannot be specified at the same time.')

    # 获取团队 LIVE 佳节活动歌曲循环数据
    def get_rotation_musics(self) -> List['FestivalRotationMusic']:
        '''获取团队 LIVE 佳节活动歌曲循环数据

        返回:
            List[FestivalRotationMusic]: 团队 LIVE 佳节活动歌曲循环数据
        '''
        info = self.__get_info__()
        if (event_type := info['eventType']) != 'festival':
            raise ValueError(f'Rotation musics are only available for festival events, not \'{event_type}\'.')
        return get_rotation_musics(self.id)
    
    # 异步获取团队 LIVE 佳节活动歌曲循环数据
    async def get_rotation_musics_async(self) -> List['FestivalRotationMusic']:
        '''获取团队 LIVE 佳节活动歌曲循环数据

        返回:
            List[FestivalRotationMusic]: 团队 LIVE 佳节活动歌曲循环数据
        '''
        info = await self.__get_info_async__()
        if (event_type := info['eventType']) != 'festival':
            raise ValueError(f'Rotation musics are only available for festival events, not \'{event_type}\'.')
        return await get_rotation_musics_async(self.id)
    
    # 获取团队 LIVE 佳节活动舞台数据
    def get_stages(self) -> List['FestivalStage']:
        '''获取团队 LIVE 佳节活动舞台数据

        返回:
            List[FestivalStage]: 团队 LIVE 佳节活动舞台数据
        '''
        info = self.__get_info__()
        if (event_type := info['eventType']) != 'festival':
            raise ValueError(f'Stages are only available for festival events, not \'{event_type}\'.')
        return get_stages(self.id)
    
    # 异步获取团队 LIVE 佳节活动舞台数据
    async def get_stages_async(self) -> List['FestivalStage']:
        '''获取团队 LIVE 佳节活动舞台数据

        返回:
            List[FestivalStage]: 团队 LIVE 佳节活动舞台数据
        '''
        info = await self.__get_info_async__()
        if (event_type := info['eventType']) != 'festival':
            raise ValueError(f'Stages are only available for festival events, not \'{event_type}\'.')
        return await get_stages_async(self.id)
