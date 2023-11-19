'''`bestdori.utils.content`

Bestdori 帖子内容模块'''
from typing import Literal, Any

# 内容类
class Content:
    '''内容类'''
    type: str
    '''内容类型'''
    # 初始化
    def __init__(self, values: dict[str, Any]) -> None:
        '''初始化'''
        for key, value in values.items():
            setattr(self, key, value)
        return
    
    # 纯文本
    @staticmethod
    def text(data: str) -> 'Text':
        '''纯文本

        参数:
            data (str): 文本内容

        返回:
            Text: 文本对象 `bestdori.utils.Text`
        '''
        return Text({'type': 'text', 'data': data})
    
    # 换行
    @staticmethod
    def br() -> 'Br':
        '''换行

        返回:
            Br: 换行对象 `bestdori.utils.Br`
        '''
        return Br({'type': 'br'})
    
    # 表情
    @staticmethod
    def emoji(data: str) -> 'Emoji':
        '''表情

        参数:
            data (str): 表情名称

        返回:
            Emoji: 表情对象 `bestdori.utils.Emoji`
        '''
        return Emoji({'type': 'emoji', 'data': data})
    
    # 提及
    @staticmethod
    def mention(data: str) -> 'Mention':
        '''提及

        参数:
            data (str): 提及的用户名

        返回:
            Mention: 提及对象 `bestdori.utils.Mention`
        '''
        return Mention({'type': 'mention', 'data': data})
    
    # 标题
    @staticmethod
    def heading(data: str, margin: Literal['top']='top') -> 'Heading':
        '''标题

        参数:
            data (str): 标题内容
            
            margin (Literal[&#39;top&#39;], optional): 页边空白位置

        返回:
            Heading: 标题对象 `bestdori.utils.Heading`
        '''
        return Heading({'type': 'heading', 'data': data, 'margin': margin})
    
    # 图片
    @staticmethod
    def image(objects: list[str], display: Literal[0, 1, 2]=0) -> 'Image':
        '''图片

        参数:
            objects (list[str]): 图片对象网址列表
            
            display (Literal[&#39;0&#39;, &#39;1&#39;, &#39;2&#39;], optional): 显示类型 `0`: 大图 `1`: 缩略图 `2`: 图标

        返回:
            Image: 图片对象 `bestdori.utils.Image`
        '''
        return Image({'type': 'image', 'objects': objects, 'display': display})
    
    # 链接
    @staticmethod
    def link(
        target: Literal[
            'url',
            'character-single',
            'card-single',
            'costume-single',
            'event-single',
            'gacha-single',
            'song-single',
            'logincampaign-single',
            'comic-single',
            'mission-single'
        ],
        data: str
    ) -> 'Link':
        '''链接

        参数:
            target (str): 链接对象
            
            data (str): 链接信息

        返回:
            Link: 链接对象 `bestdori.utils.Link`
        '''
        if target != 'url':
            if not data.isdigit():
                raise ValueError('非 url 链接对象的 data 必须为数字。')
        return Link({'type': 'link', 'target': target, 'data': data})
    
    # 列表
    @staticmethod
    def list(
        target: Literal[
            'character-info',
            'card-info',
            'card-icon',
            'costume-info',
            'event-info',
            'gacha-info',
            'song-info',
            'logincampaign-info',
            'comic-info',
            'mission-info'
        ],
        display: Literal[0, 1, 2],
        objects: list[str]
    ) -> 'List':
        '''列表

        参数:
            target (str): 列表对象
            
            display (Literal[&#39;0&#39;, &#39;1&#39;, &#39;2&#39;]): 显示类型
            
            objects (list[str]): 列表对象 ID 列表

        返回:
            List: 列表对象 `bestdori.utils.List`
        '''
        return List({'type': 'list', 'target': target, 'display': display, 'objects': objects})

# 文本类
class Text(Content):
    '''文本类'''
    type: str = 'text'
    '''内容类型'''
    data: str
    '''文本内容'''

# 换行类
class Br(Content):
    type: str = 'br'
    '''内容类型'''

# 表情类
class Emoji(Content):
    '''表情类'''
    type: str = 'emoji'
    '''内容类型'''
    data: str
    '''表情名称'''

# 提及类
class Mention(Content):
    '''提及类'''
    type: str = 'mention'
    '''内容类型'''
    data: str
    '''提及的用户名'''

# 标题类
class Heading(Content):
    '''标题类'''
    type: str = 'heading'
    '''内容类型'''
    data: str
    '''标题内容'''
    margin: str
    '''页边空白位置'''

# 图片类
class Image(Content):
    '''图片类'''
    type: str = 'image'
    '''内容类型'''
    display: Literal[0, 1, 2]
    '''显示类型 `0`: 大图 `1`: 缩略图 `2`: 图标'''
    objects: list[str]
    '''图片对象网址列表'''

# 链接类
class Link(Content):
    '''链接类'''
    type: str = 'link'
    '''内容类型'''
    target: str
    '''链接对象'''
    data: str
    '''链接信息'''

# 列表类
class List(Content):
    '''列表类'''
    type: str = 'list'
    '''内容类型'''
    target: str
    '''列表对象'''
    display: Literal[0, 1, 2]
    '''显示类型'''
    objects: list[str]
    '''列表对象 ID 列表'''
