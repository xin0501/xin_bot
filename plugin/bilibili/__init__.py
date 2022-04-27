'''
Author: xin
Date: 2022-04-27 21:44:05
LastEditors: xinxin
LastEditTime: 2022-04-27 23:04:10
Description: B站分享链接解析插件
FilePath: /xin_bot/plugin/bilibili/__init__.py
'''
from typing import Union

from wechaty import Contact, Message, Room
from wechaty.plugin import WechatyPlugin
from wechaty_puppet.file_box.file_box import FileBox

from .data_source import b_parse


class BilibiliPlugin(WechatyPlugin):
    @property
    def name(self):
        return 'bilibili'

    async def on_message(self, msg: Message) -> None:
        if msg.is_self():
            return
        text = msg.text()
        if "BV" in text or "av" in text or "https://b23.tv" in text:
            chat_room = msg.room()
            from_contact: Union[Room, Contact] = msg.talker() if chat_room is None else chat_room
            info = await b_parse(text)
            file_box = FileBox.from_url(info[1], name='fengmian.jpg')
            await from_contact.say(file_box)
            await from_contact.say(info[0])
