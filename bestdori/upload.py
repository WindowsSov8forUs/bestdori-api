'''`bestdori.upload`

Bestdori 文件相关操作'''
from pathlib import Path
from hashlib import sha1
from io import BufferedReader
from typing import Optional, Union, TYPE_CHECKING

from .utils.utils import API
from .utils.network import Api
from .exceptions import AlreadyUploadedError

if TYPE_CHECKING:
    from .user import Me

# 从 Bestdori 获取指定哈希文件字节
def download(hash_: str, proxy: Optional[str]=None) -> bytes:
    '''从 Bestdori 获取指定哈希文件字节

    参数:
        hash_ (str): 文件哈希值
        
        proxy (Optional[str]): 代理服务器

    返回:
        bytes: 文件字节 `bytes`
    '''
    return Api(API['upload']['file'].format(hash=hash_), proxy).request('get').content

# 通过哈希值构建 Bestdori 文件 URL
def hash_to_url(hash_: str) -> str:
    '''通过哈希值构建 Bestdori 文件 URL

    参数:
        hash_ (str): 文件哈希值

    返回:
        str: 文件 URL
    '''
    return f'https://bestdori.com/api/upload/file/{hash_}'

# 上传文件类
class Upload:
    ''''''
    # 初始化
    def __init__(self, file_bytes: bytes, name: str, reader: BufferedReader) -> None:
        # 处理文件字节
        hash_ = sha1(file_bytes).hexdigest() # 计算 SHA-1 哈希
        size = len(file_bytes) # 计算文件大小
        # 赋值对象属性
        self._ver: int = 3
        '''文件版本'''
        self._hash: str = hash_
        '''文件哈希'''
        self._size: int = size
        '''文件大小'''
        self._name: str = name
        '''文件名'''
        self._reader: BufferedReader = reader
        '''文件字节流'''
        return
    
    # 从路径中获取文件
    @classmethod
    def from_path(cls, path: Union[str, Path]) -> 'Upload':
        '''从路径中获取文件

        参数:
            path (Union[str, Path]): 文件路径

        返回:
            Upload: 上传文件对象
        '''
        # 从路径中获取文件名
        path = Path(path)
        file_name = path.name
        # 读取文件字节
        file = open(path, 'rb')
        file_bytes = file.read()
        # 返回上传文件对象
        return cls(file_bytes, file_name, file)
    
    # 上传文件
    def upload(self, me: 'Me', proxy: Optional[str]=None) -> str:
        '''上传文件

        参数:
            me (Me): 自身用户对象
            
            proxy (Optional[str]): 代理服务器

        返回:
            str: 上传文件的哈希值
        '''
        if self._reader.closed:
            raise ValueError('文件流已关闭。')
        
        # 构建上传负载
        payload = {
            'ver': self._ver,
            'hash': self._hash,
            'size': self._size
        }
        # 发送预上传请求
        try:
            Api(API['upload']['prepare'], proxy).request('post', cookies=me.cookies, data=payload)
        except AlreadyUploadedError:
            self._reader.close()
            return self._hash
        # 发送上传请求
        with self._reader:
            response = Api(API['upload']['upload'], proxy).request(
                'post',
                files={
                    'file': (self._name, self._reader)
                },
                cookies=me.cookies
            )
        # 获取文件的哈希值
        hash_get = response.json()['hash']
        #重复查询至多 5 次上传状态
        for _ in range(5):
            # 发送上传状态查询请求
            response = Api(API['upload']['status'].format(hash=hash_get), proxy).request('get')
            # 获取上传状态
            status = response.json()['status']
            # 若上传成功则返回
            if status == 'available':
                return hash_get
        
        raise TimeoutError(f'上传文件 {self._name} 超时。')
