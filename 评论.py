#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/26 下午 9:44
# @Author  : 殇夜殇雪
# @File    : 评论.py
import cloudmusic
import time
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
音乐 = cloudmusic.getMusic(1372060183)
评论数量 = 音乐.getCommentsCount()
print(f"一共有{评论数量}条评论")
cons = 音乐.getHotComments()
print(type(cons))
for con in cons:
    print(f"用户：{con['nickName']}")
    print(f"用户ID：{con['userId']}")
    print(f"用户头像Url：{con['avatarUrl']}")
    print(f"内容：{con['content']}")
    print(f"获赞数：{con['likeCount']}")
    timestamp = int((con['time']))/1000
    timeArray = time.localtime(timestamp)
    Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(f"发布时间：{Time}")
    print(f"是否开通VIP：{con['vipType']}")
    with open("评论.txt", "a", encoding="utf-8")as f:
        f.write(str(con))
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')

