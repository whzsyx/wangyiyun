#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/27 下午 2:58
# @Author  : 殇夜殇雪
# @File    : 歌单.py
import cloudmusic
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
歌单 = cloudmusic.getPlaylist(5002003275)
print(type(歌单))
print(歌单)
for i in range(len(歌单)):
    print(f"第{i + 1}首:{歌单[i].name}")



