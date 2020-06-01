#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/27 下午 3:39
# @Author  : 殇夜殇雪
# @File    : 下载.py
import cloudmusic
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
歌名 = input("请输入歌曲：")
搜索 = cloudmusic.search(歌名, 20)
for i in range(len(搜索)):
    print(f"第：{i+1}首{搜索[i].name}")
    zz = f"作者：{搜索[i].artist[0]}"
    s = f"歌曲ID：{搜索[i].id}"
    print(s)
    print(zz)
ID = input("对应歌的ID：")
下载 = cloudmusic.getMusic(ID)
下载.download("D:\Pycharm\普通程序\爬虫\音乐", level=" lossess ")


