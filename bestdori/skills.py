'''`bestdori.skills`

技能信息获取模块'''

from typing_extensions import overload
from typing import TYPE_CHECKING, Union, Literal, Optional

from .user import Me
from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import (
        SkillsAll2,
        SkillsAll5,
        SkillsAll10,
    )

API = get_api('bestdori.api')

# 获取总技能信息
@overload
def get_all(index: Literal[2], *, me: Optional[Me] = None) -> 'SkillsAll2':
    '''获取总技能信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`
    
    返回:
        SkillsAll2: 获取到的总技能简易描述信息 `all.2.json`
    '''
    ...
@overload
def get_all(index: Literal[5], *, me: Optional[Me] = None) -> 'SkillsAll5':
    '''获取总技能信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`
    
    返回:
        SkillsAll5: 获取到的总技能简洁信息 `all.5.json`
    '''
    ...
@overload
def get_all(index: Literal[10], *, me: Optional[Me] = None) -> 'SkillsAll10':
    '''获取总技能信息

    参数:
        index (Literal[10]): 指定获取哪种 `all.json`
    
    返回:
        SkillsAll10: 获取到的总技能详细信息 `all.10.json`
    '''
    ...

def get_all(index: Literal[2, 5, 10]=10, *, me: Optional[Me] = None) -> Union['SkillsAll2', 'SkillsAll5', 'SkillsAll10']:
    return Api(API['all']['skills'].format(index=index)).get(
        cookies=me.__get_cookies__() if me else None,
    ).json()

# 异步获取总技能信息
@overload
async def get_all_async(index: Literal[2], *, me: Optional[Me] = None) -> 'SkillsAll2':
    '''获取总技能信息

    参数:
        index (Literal[2]): 指定获取哪种 `all.json`
    
    返回:
        SkillsAll2: 获取到的总技能简易描述信息 `all.2.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[5], *, me: Optional[Me] = None) -> 'SkillsAll5':
    '''获取总技能信息

    参数:
        index (Literal[5]): 指定获取哪种 `all.json`
    
    返回:
        SkillsAll5: 获取到的总技能简洁信息 `all.5.json`
    '''
    ...
@overload
async def get_all_async(index: Literal[10], *, me: Optional[Me] = None) -> 'SkillsAll10':
    '''获取总技能信息

    参数:
        index (Literal[10]): 指定获取哪种 `all.json`
    
    返回:
        SkillsAll10: 获取到的总技能详细信息 `all.10.json`
    '''
    ...

async def get_all_async(index: Literal[2, 5, 10]=10, *, me: Optional[Me] = None) -> Union['SkillsAll2', 'SkillsAll5', 'SkillsAll10']:
    return (await Api(API['all']['skills'].format(index=index)).aget(
        cookies=await me.__get_cookies_async__() if me else None,
    )).json()
