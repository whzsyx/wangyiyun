#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/27 下午 3:18
# @Author  : 殇夜殇雪
# @File    : 搜索.py
import cloudmusic
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
专辑 = cloudmusic.getAlbum(81127107)
歌名 = input("请输入你想搜索的歌名：")
search_list = cloudmusic.search(歌名, 20)
print(search_list)
for i in range(len(search_list)):
    print(f"第{i + 1}首：{search_list[i].name}")
