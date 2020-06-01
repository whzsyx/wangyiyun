#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/26 下午 9:44
# @Author  : 殇夜殇雪
import cloudmusic
import time
用户 = cloudmusic.getUser(1804446467)
print(type(用户))
print(f"用户等级:{用户.level}")
print(f"累计听歌数量:{用户.listenSongs}")
print(f"所在城市行政区代码:{用户.city}")
print(f"所在省份行政区代码:{用户.province}")
print(f"用户头像:{用户.avatarUrl}")
print(f"用户昵称:{用户.nickname}")
print(f"粉丝数量:{用户.fans}")
print(f"个性签名:{用户.signature}")
print(f"关注的用户数量:{用户.follows}")
print(f"动态数量:{用户.eventCount}")
print(f"创建歌单数量:{用户.playlistCount}")
print(f"是否开通VIP(0=未开通,11=黑胶,10=开通音乐包):{用户.vipType}")
birthday_stamp = int((用户.birthday))/1000
b = abs(birthday_stamp)
timearray = time.localtime(b)
birthday_time = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
print(f"生日时间:{birthday_time}")
print(用户.birthday)
