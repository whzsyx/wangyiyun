#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/26 下午 7:34
# @Author  : 殇夜殇雪
# @File    : 音乐属性.py
import cloudmusic
i = input("请输入歌曲ID：_______")
音乐 = cloudmusic.getMusic(i)
print(type(音乐))
print(f"歌名:{音乐.name}")
print(f"ID:{音乐.id}")
print(f"歌手：{音乐.artist[0]}")
print(f"歌手ID:{音乐.artistId[0]}")
print(f"专辑名称：{音乐.album}")
print(f"专辑ID：{音乐.albumId}")
print(f"音频文件大小：{音乐.size}kb")
print(f"专辑图片url：{音乐.picUrl}")
print(f"音乐URL：{音乐.url}")
print(f"音乐文件类型：{音乐.type}")

