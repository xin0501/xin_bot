'''
Author: xin
Date: 2022-04-27 21:45:04
LastEditors: xinxin
LastEditTime: 2022-04-27 22:34:25
Description: 抖音分享链接解析插件
FilePath: /xin_bot/plugin/douyin/__init__.py
'''
from typing import Union

from wechaty import Contact, Message, Room
from wechaty.plugin import WechatyPlugin
from wechaty_puppet.file_box.file_box import FileBox
from .data_source import get_video_url, get_video_id, get_video_info, headers


class DouYinPlugin(WechatyPlugin):
    @property
    def name(self):
        return 'douyin'

    async def on_message(self, msg: Message) -> None:
        if msg.is_self():
            return
        text = msg.text()
        if 'https://v.douyin.com' in text:
            chat_room = msg.room()
            from_contact: Union[Room, Contact] = msg.talker() if chat_room is None else chat_room
            await from_contact.ready()
            douyin_result = get_video_info(get_video_id(get_video_url(text)))
            await from_contact.say(douyin_result[2])
            cover_file = FileBox.from_url(douyin_result[0], headers=headers, name='cover.jpeg')
            await from_contact.say(cover_file)
            video_file = FileBox.from_url(douyin_result[1], headers=headers, name='douyin.mp4')
            await from_contact.say(video_file)
