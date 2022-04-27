'''
Author: xin
Date: 2022-04-27 21:44:42
LastEditors: xinxin
LastEditTime: 2022-04-27 22:31:50
Description: B站分享链接解析
FilePath: /xin_bot/plugin/bilibili/data_source.py
'''
import requests
from bilibili_api import video


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


# 链接解析
async def b_parse(msg):
    if "BV" in msg:
        index = msg.find("BV")
        if len(msg[index + 2:]) >= 10:
            msg = msg[index: index + 12]
            url = f"https://www.bilibili.com/video/{msg}"
            vd_info = await (video.Video(bvid=msg).get_info())
            # print(vd_info)
    elif "av" in msg:
        index = msg.find("av")
        if len(msg[index + 2:]) >= 8:
            msg = msg[index + 2: index + 11]
            if is_number(msg):
                url = f"https://www.bilibili.com/video/av{msg}"
                vd_info = await video.Video(aid=int(msg)).get_info()
    elif "https://b23.tv" in msg:
        url = "https://" + msg[msg.find("b23.tv"): msg.find("b23.tv") + 14]
        re = requests.get(url)
        print(re.url)
        url = str(re.url).split("?")[0]
        print(url)
        bvid = url.split("/")[-1]
        print(bvid)
        vd_info = await (video.Video(bvid=bvid).get_info())

    # aid = vd_info["aid"]  # 视频aid
    title = vd_info["title"]  # 视频标题
    author = vd_info["owner"]["name"]  # 视频作者
    # reply = vd_info["stat"]["reply"]  # 回复
    favorite = vd_info["stat"]["favorite"]  # 收藏
    coin = vd_info["stat"]["coin"]  # 投币
    like = vd_info['stat']['like']      # 点赞
    view = vd_info['stat']['view']  # 播放量
    # danmu = vd_info['stat']['danmaku']  # 弹幕
    pic = vd_info["pic"]
    # logger.info(vd_info)
    info = f"标题：{title}\nUP：{author}\n播放量：{view}，点赞：{like}，收藏：{favorite}，投币：{coin}\n{url}"
    print(info)
    return (info, pic)
