'''`bestdori.logincampaigns`

BanG Dream! 登录奖励相关操作'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional

from . import post
from .user import Me
from .utils.network import Api
from .utils import name, get_api
from .exceptions import (
    HTTPStatusError,
    NoDataException,
    NotExistException,
    ServerNotAvailableError,
)

if TYPE_CHECKING:
    from .typing import (
        NoneDict,
        PostList,
        ServerName,
        LoginCampaignInfo,
        LoginCampaignsAll1,
        LoginCampaignsAll5,
    )

API = get_api('bestdori.api')

# 获取总登录奖励信息
@overload
def get_all(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总登录奖励信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`
        me (Optional[Me], optional): 登录用户信息
    
    返回:
        Dict[str, NoneDict]: 所有已有登录奖励 ID `all.0.json`
    '''
    ...
@overload
def get_all(index: Literal[1], *, me: Optional[Me] = None) -> 'LoginCampaignsAll1':
    '''获取总登录奖励信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`
        me (Optional[Me], optional): 登录用户信息
    
    返回:
        LoginCampaignsAll1: 所有已有登录奖励简洁信息 `all.1.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'LoginCampaignsAll5':
    '''获取总登录奖励信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`
        me (Optional[Me], optional): 登录用户信息
    
    返回:
        LoginCampaignsAll5: 所有已有登录奖励的较详细信息 `all.5.json`
    '''
    ...

def get_all(index: Literal[0, 1, 5], *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'LoginCampaignsAll1', 'LoginCampaignsAll5']:
    return Api(API['loginCampaigns']['all'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取总登录奖励信息
@overload
async def get_all_async(index: Literal[0], *, me: Optional[Me] = None) -> Dict[str, 'NoneDict']:
    '''获取总登录奖励信息

    参数:
        index (Literal[0]): 指定获取哪种 `all.json`
        me (Optional[Me], optional): 登录用户信息
    
    返回:
        Dict[str, NoneDict]: 所有已有登录奖励 ID `all.0.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[1], *, me: Optional[Me] = None) -> 'LoginCampaignsAll1':
    '''获取总登录奖励信息

    参数:
        index (Literal[1]): 指定获取哪种 `all.json`
        me (Optional[Me], optional): 登录用户信息
    
    返回:
        LoginCampaignsAll1: 所有已有登录奖励简洁信息 `all.1.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'LoginCampaignsAll5':
    '''获取总登录奖励信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`
        me (Optional[Me], optional): 登录用户信息
    
    返回:
        LoginCampaignsAll5: 所有已有登录奖励的较详细信息 `all.5.json`
    '''
    ...

async def get_all_async(index: Literal[0, 1, 5], *, me: Optional[Me] = None) -> Union[Dict[str, 'NoneDict'], 'LoginCampaignsAll1', 'LoginCampaignsAll5']:
    return (await Api(API['loginCampaigns']['all'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()

# 登录奖励类
class LoginCampaign:
    '''登录奖励类

    参数:
        id (int): 登录奖励 ID
    '''
    # 初始化
    def __init__(self, id: int, *, me: Optional[Me] = None) -> None:
        '''登录奖励类

        参数:
            id (int): 登录奖励 ID
        '''
        self.id: int = id
        '''登录奖励 ID'''
        self.__info: Optional['LoginCampaignInfo'] = None
        '''登录奖励信息'''

        self.__me = me
        return
    
    @property
    def info(self) -> 'LoginCampaignInfo':
        '''登录奖励信息'''
        if not self.__info:
            raise RuntimeError(f'LoginCampaign \'{self.id}\' info were not retrieved.')
        return self.__info

    # 奖励标题
    @property
    def __name__(self) -> List[Optional[str]]:
        '''登录奖励标题'''
        return self.info['caption']
    
    # 登录奖励默认服务器
    @property
    def __server__(self) -> 'ServerName':
        '''登录奖励默认服务器'''
        # 获取 publishedAt 数据
        published_at = self.info['publishedAt']
        # 根据 publishedAt 数据判断服务器
        if published_at[0] is not None: return 'jp'
        elif published_at[1] is not None: return 'en'
        elif published_at[2] is not None: return 'tw'
        elif published_at[3] is not None: return 'cn'
        elif published_at[4] is not None: return 'kr'
        else:
            raise NoDataException('logincampaign server')
    
    # 获取登录奖励信息
    def get_info(self) -> 'LoginCampaignInfo':
        '''获取登录奖励信息

        返回:
            LoginCampaignInfo: 登录奖励详细信息
        '''
        try:
            response = Api(
                API['loginCampaigns']['info'].format(id=self.id)
            ).get(
                cookies=self.__me.__get_cookies__() if self.__me else None,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'LoginCampaign {self.id}')
            raise exception
        
        self.__info = response.json()
        return self.info

    def __get_info__(self) -> 'LoginCampaignInfo':
        if not self.__info:
            return self.get_info()
        return self.__info
    
    # 异步获取登录奖励信息
    async def get_info_async(self) -> 'LoginCampaignInfo':
        '''获取登录奖励信息

        返回:
            LoginCampaignInfo: 登录奖励详细信息
        '''
        try:
            response = await Api(
                API['loginCampaigns']['info'].format(id=self.id)
            ).aget(
                cookies=await self.__me.__get_cookies_async__() if self.__me else None,
            )
        except HTTPStatusError as exception:
            if exception.response.status_code == 404:
                raise NotExistException(f'LoginCampaign {self.id}')
            raise exception
        
        self.__info = response.json()
        return self.info
    
    async def __get_info_async__(self) -> 'LoginCampaignInfo':
        if not self.__info:
            return await self.get_info_async()
        return self.__info
    
    # 获取登录奖励评论
    def get_comment(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取登录奖励评论

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
            category_name='LOGINCAMPAIGN_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 异步获取登录奖励评论
    async def get_comment_async(
        self,
        limit: int=20,
        offset: int=0,
        order: Literal['TIME_DESC', 'TIME_ASC']='TIME_ASC',
    ) -> 'PostList':
        '''获取登录奖励评论

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
            category_name='LOGINCAMPAIGN_COMMENT',
            category_id=str(self.id),
            order=order,
            limit=limit,
            offset=offset,
            me=self.__me,
        )
    
    # 获取登录奖励背景图图像
    def get_background(self, server: 'ServerName') -> bytes:
        '''获取登录奖励背景图图像

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 登录奖励背景图图像字节数据 `bytes`
        '''
        info = self.__get_info__()
        # 获取登录奖励数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if asset_bundle_name[index] is None:
            raise ServerNotAvailableError(f'LoginCampaign \'{name(self)}\'', server)
        return Api(
            API['event']['loginbouns'].format(
                server=server, asset_bundle_name=asset_bundle_name[index]
            )
        ).get(
            cookies=self.__me.__get_cookies__() if self.__me else None,
        ).content
    
    # 异步获取登录奖励背景图图像
    async def get_background_async(self, server: 'ServerName') -> bytes:
        '''获取登录奖励背景图图像

        参数:
            server (ServerName): 指定服务器

        返回:
            bytes: 登录奖励背景图图像字节数据 `bytes`
        '''
        info = await self.__get_info_async__()
        # 获取登录奖励数据包名称
        asset_bundle_name = info['assetBundleName']
        # 判断服务器
        SERVERS = ['jp', 'en', 'tw', 'cn', 'kr']
        index = SERVERS.index(server)
        if asset_bundle_name[index] is None:
            raise ServerNotAvailableError(f'LoginCampaign \'{name(self)}\'', server)
        return (await Api(
            API['event']['loginbouns'].format(
                server=server, asset_bundle_name=asset_bundle_name[index]
            )
        ).aget(
            cookies=await self.__me.__get_cookies_async__() if self.__me else None,
        )).content
