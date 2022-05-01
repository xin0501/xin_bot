'''
Author: xinxin
Date: 2022-04-04 14:44:33
LastEditors: xinxin
LastEditTime: 2022-05-01 10:11:22
Description: B站链接解析
'''
import ujson as json
from loguru import logger
import requests


def is_number(s: str) -> bool:
    """
    说明：
        检测 s 是否为数字
    参数：
        :param s: 文本
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata

        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


async def b_parse(msg):
    v_id = ''
    if "BV" in msg:
        index = msg.find("BV")
        if len(msg[index + 2:]) >= 10:
            msg = msg[index: index + 12]
            url = f"https://www.bilibili.com/video/{msg}"
            v_id = msg
    elif "av" in msg:
        index = msg.find("av")
        if len(msg[index + 2:]) >= 8:
            msg = msg[index + 2: index + 11]
            if is_number(msg):
                url = f"https://www.bilibili.com/video/av{msg}"
                v_id = msg
    elif "https://b23.tv" in msg:
        url = "https://" + msg[msg.find("b23.tv"): msg.find("b23.tv") + 14]
        re = requests.get(url)
        url = str(re.url).split("?")[0]
        bvid = url.split("/")[-1]
        v_id = bvid
    if v_id[0] == 'B':
        re = requests.get(f'https://api.bilibili.com/x/web-interface/view?bvid={v_id}').text
    else:
        re = requests.get(f'https://api.bilibili.com/x/web-interface/view?aid={v_id}').text
    vd_info = json.loads(re)['data']
    title = vd_info["title"]  # 视频标题
    author = vd_info["owner"]["name"]  # 视频作者
    favorite = vd_info["stat"]["favorite"]  # 收藏
    coin = vd_info["stat"]["coin"]  # 投币
    like = vd_info['stat']['like']      # 点赞
    view = vd_info['stat']['view']  # 播放量
    pic = vd_info["pic"]
    # logger.info(vd_info)
    info = f"标题：{title}\nUP：{author}\n播放量：{view}，点赞：{like}，收藏：{favorite}，投币：{coin}\n{url}"
    print(info)
    return (info, pic)

