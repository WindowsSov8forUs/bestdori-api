import os
import sys
# 添加父目录的父目录至系统目录中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bestdori.post import Post
proxy = 'http://127.0.0.1:2802'
print(Post('112340', proxy).get_song())