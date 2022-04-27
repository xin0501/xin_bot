'''
Author: xin
Date: 2022-04-27 21:45:02
LastEditors: xinxin
LastEditTime: 2022-04-27 22:34:15
Description: ding-dong插件
FilePath: /xin_bot/plugin/ding/__init__.py
'''
from typing import Union

from wechaty import Contact, Message, Room
from wechaty.plugin import WechatyPlugin


class DingPlugin(WechatyPlugin):
    @property
    def name(self):
        return 'ding'

    async def on_message(self, msg: Message) -> None:
        if msg.is_self():
            return
        text = msg.text()
        chat_room = msg.room()
        from_contact: Union[Room, Contact] = msg.talker() if chat_room is None else chat_room
        if text == 'ding':
            await from_contact.ready()
            await from_contact.say('dong')
