'''
Author: xin
Date: 2022-04-27 21:40:19
LastEditors: xinxin
LastEditTime: 2022-04-27 23:05:00
Description: 机器人启动入口
FilePath: /xin_bot/xin_bot.py
'''
from __future__ import annotations, print_function

import asyncio
import os

from wechaty import Wechaty

from plugin.bilibili import BilibiliPlugin
from plugin.ding import DingPlugin
from plugin.douyin import DouYinPlugin
from plugin.wb import WBHotPlugin

# Padlocal协议的TOKEN，基于ipad
# 将此处替换为自己的uuid和IP地址端口
os.environ['TOKEN'] = "UUID"
os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = "IP:port"


async def main():
    bot = Wechaty().use([
        WBHotPlugin(),
        DingPlugin(),
        DouYinPlugin(),
        BilibiliPlugin(),
    ])
    await bot.start()
    print("机器人正在启动")


asyncio.run(main())
