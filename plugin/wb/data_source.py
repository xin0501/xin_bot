'''
Author: xin
Date: 2022-04-27 21:44:42
LastEditors: xinxin
LastEditTime: 2022-04-27 22:31:32
Description: 微博热搜、网易云热搜、摸鱼
FilePath: /xin_bot/plugin/wb/data_source.py
'''
import json

import requests


# 网易云热评
async def get_163() -> dict:
    url = 'https://api.vvhan.com/api/reping'
    re = requests.get(url).text
    comment = json.loads(re)
    return comment


# 微博热搜
async def get_wbhot() -> str:
    url = 'https://api.vvhan.com/api/wbhot'
    wb_hot = requests.get(url).text
    wb_hot = json.loads(wb_hot)
    time = wb_hot['time']
    # 热搜数据
    data = wb_hot['data']
    hot_list = []
    for i in range(0, 15):
        hot_list.append(f"【{i+1}】{data[i]['title']}  热度{data[i]['hot']}")
    hot = '\n'.join(hot_list)
    hot = '微博热搜' + "\n" + time + '\n' + hot
    return hot
