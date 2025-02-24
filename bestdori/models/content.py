'''`bestdori.utils.content`

Bestdori 帖子内容模块'''
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Literal, TypeAlias

LinkTarget: TypeAlias = Literal[
    'url',
    'character-single',
    'card-single',
    'costume-single',
    'event-single',
    'gacha-single',
    'song-single',
    'logincampaign-single',
    'comic-single',
    'mission-single',
]
ListTarget: TypeAlias = Literal[
    'character-info',
    'card-info',
    'card-icon',
    'costume-info',
    'event-info',
    'gacha-info',
    'song-info',
    'logincampaign-info',
    'comic-info',
    'mission-info',
]

@dataclass
class Content:
    '''内容类'''
    type: str
    '''内容类型'''
    
    @property
    def __dict__(self) -> Dict[str, Any]:
        '''字典化'''
        return asdict(self)
    
    @staticmethod
    def text(data: str) -> 'Text':
        '''文本

        参数:
            data (str): 文本内容

        返回:
            Text: 文本对象
        '''
        return Text('text', data)
    
    @staticmethod
    def br() -> 'Br':
        '''换行

        返回:
            Br: 换行对象
        '''
        return Br('br')
    
    @staticmethod
    def emoji(data: str) -> 'Emoji':
        '''表情

        参数:
            data (str): 表情 ID

        返回:
            Emoji: 表情对象
        '''
        return Emoji('emoji', data)
    
    @staticmethod
    def mention(data: str) -> 'Mention':
        '''提及

        参数:
            data (str): 提及用户名

        返回:
            Mention: 提及对象
        '''
        return Mention('mention', data)
    
    @staticmethod
    def heading(data: str, margin: Literal['top']) -> 'Heading':
        '''标题

        参数:
            data (str): 标题内容
            margin (Literal['top']): 页边空白位置

        返回:
            Heading: 标题对象
        '''
        return Heading('heading', data, margin)
    
    @staticmethod
    def image(display: Literal[0, 1, 2], object: List[str]) -> 'Image':
        '''图片

        参数:
            display (Literal[0, 1, 2]): 显示类型
                `0`: 大图
                `1`: 缩略图
                `2`: 图标
            object (List[str]): 图片对象网址列表

        返回:
            Image: 图片对象
        '''
        return Image('image', display, object)
    
    @staticmethod
    def link(target: LinkTarget, data: str) -> 'Link':
        '''链接

        参数:
            target (LinkTarget): 链接对象
            data (str): 链接信息

        返回:
            Link: 链接对象
        '''
        return Link('link', target, data)
    
    @staticmethod
    def list(target: ListTarget, display: Literal[0, 1, 2], object: List[str]) -> 'ListContent':
        '''列表

        参数:
            target (ListTarget): 列表对象
            display (Literal[0, 1, 2]): 显示类型
            object (List[str]): 列表对象 ID 列表

        返回:
            ListContent: 列表对象
        '''
        return ListContent('list', target, display, object)

@dataclass
class Text(Content):
    '''文本类'''
    type: Literal['text']
    '''内容类型'''
    data: str
    '''文本内容'''

@dataclass
class Br(Content):
    '''换行类'''
    type: Literal['br']
    '''内容类型'''

@dataclass
class Emoji(Content):
    '''表情类'''
    type: Literal['emoji']
    '''内容类型'''
    data: str
    '''表情 ID'''

@dataclass
class Mention(Content):
    '''提及类'''
    type: Literal['mention']
    '''内容类型'''
    data: str
    '''提及用户名'''

@dataclass
class Heading(Content):
    '''标题类'''
    type: Literal['heading']
    '''内容类型'''
    data: str
    '''标题内容'''
    margin: Literal['top']
    '''页边空白位置'''

@dataclass
class Image(Content):
    '''图片类'''
    type: Literal['image']
    '''内容类型'''
    display: Literal[0, 1, 2]
    '''显示类型
    
    `0`: 大图
    
    `1`: 缩略图
    
    `2`: 图标
    '''
    object: List[str]
    '''图片对象网址列表'''

@dataclass
class Link(Content):
    '''链接类'''
    type: Literal['link']
    '''内容类型'''
    target: LinkTarget
    '''链接对象'''
    data: str
    '''链接信息'''

@dataclass
class ListContent(Content):
    '''列表内容类'''
    type: Literal['list']
    '''内容类型'''
    target: ListTarget
    '''列表对象'''
    display: Literal[0, 1, 2]
    '''显示类型'''
    object: List[str]
    '''列表对象 ID 列表'''