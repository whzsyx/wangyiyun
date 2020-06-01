#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/30 下午 9:54
# @Author  : 殇夜殇雪
# @File    : 对象方法.py
import cloudmusic
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
对象 = cloudmusic.getPlaylist(5002003275)  # 对应歌单ID
排行 = cloudmusic.getUser(1804446467)

# print(type(对象))

for i in range(len(对象)):
    print(f"创建者ID:{对象[i].artistId}")
    print(f"歌曲ID:{对象[i].id}")
    print(f"第{i+1}首:{对象[i].name}")
    print(f"格式:{对象[i].type}")


