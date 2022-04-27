'''
Author: xinxin
Date: 2022-04-27 21:45:07
LastEditors: xinxin
LastEditTime: 2022-04-27 23:02:12
Description: 微博热搜、网易云热评、摸鱼插件
FilePath: /xin_bot/plugin/wb/__init__.py
'''
from typing import Union

import requests
from wechaty import Contact, FileBox, Message, Room
from wechaty.plugin import WechatyPlugin

from .data_source import get_163, get_wbhot


class WBHotPlugin(WechatyPlugin):
    @property
    def name(self):
        return 'wbhot'

    async def on_message(self, msg: Message) -> None:
        if msg.is_self():
            return
        text = msg.text()
        chat_room = msg.room()
        from_contact: Union[Room, Contact] = msg.talker() if chat_room is None else chat_room

        if text in ['到点了', '网易云', '网抑云', '我好难过', '难过']:
            comment = await get_163()
            name = comment['data']['name']
            content = comment['data']['content']
            await from_contact.ready()
            await from_contact.say(f"《{name}》\n{content}")

        if text in ['微博', '热搜', '微博热搜']:
            hot = await get_wbhot()
            await from_contact.ready()
            await from_contact.say(hot)

        if text == '摸鱼':
            re = requests.get('https://api.vvhan.com/api/moyu').url
            file = FileBox.from_url(re, name='moyu.png')
            await from_contact.ready()
            await from_contact.say(file)
