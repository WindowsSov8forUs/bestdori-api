'''`bestdori.ingameskin`

游戏皮肤资源获取模块'''

from typing import TYPE_CHECKING, Literal, Optional

from .utils import get_api
from .utils.network import Api

if TYPE_CHECKING:
    from .typing import ServerName

ASSETS = get_api('bestdori.assets')

# 获取音符皮肤资源图
def get_noteskin(
    type: int,
    name: Literal["longNoteLine", "longNoteLine2", "simultaneous_line", "rhythmGameSprites", "directionalFlickSprites"],
    *,
    server: 'ServerName',
) -> bytes:
    '''获取音符皮肤资源图

    参数:
        type (int): 皮肤类型
        name (Literal["longNoteLine", "longNoteLine2", "simultaneous_line", "rhythmGameSprites", "directionalFlickSprites"]): 资源名称
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服
    
    返回:
        bytes: 音符皮肤资源图字节数据 `bytes`
    '''
    return Api(
        ASSETS['noteskin'][name].format(
            server=server,
            type=type,
        )
    ).get().content

# 异步获取音符皮肤资源图
async def get_noteskin_async(
    type: int,
    name: Literal["longNoteLine", "longNoteLine2", "simultaneous_line", "rhythmGameSprites", "directionalFlickSprites"],
    *,
    server: 'ServerName',
) -> bytes:
    '''获取音符皮肤资源图

    参数:
        type (int): 皮肤类型
        name (Literal["longNoteLine", "longNoteLine2", "simultaneous_line", "rhythmGameSprites", "directionalFlickSprites"]): 资源名称
        server (ServerName): 指定服务器
            `jp`: 日服
            `en`: 英服
            `tw`: 台服
            `cn`: 国服
            `kr`: 韩服
    
    返回:
        bytes: 音符皮肤资源图字节数据 `bytes`
    '''
    return (await Api(
        ASSETS['noteskin'][name].format(
            server=server,
            type=type,
        )
    ).aget()).content
