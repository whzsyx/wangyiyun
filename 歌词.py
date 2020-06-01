#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/27 下午 2:46
# @Author  : 殇夜殇雪
# @File    : 歌词.py
import re
import cloudmusic
音乐 = cloudmusic.getMusic(1372060183)
歌词 = 音乐.getLyrics()[0]
歌词_list = 音乐.getLyrics()
print(歌词_list)
print(歌词)
x = re.findall(r"](.*)\n", 歌词)
for i in x:
    print(i)
    """
    with open("歌词空.txt", "a", encoding='utf-8')as f:
        f.write(i)
        f.close()
        """