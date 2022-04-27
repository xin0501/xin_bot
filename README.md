# xin_bot
[![Powered by Wechaty](https://img.shields.io/badge/Powered%20By-Wechaty-green.svg)](https://wechaty.js.org)
[![Wechaty Contributor Program](https://img.shields.io/badge/Wechaty-Contributor%20Program-green.svg)](https://wechaty.js.org/docs/contributor-program)   
基于wechaty社区的python-wechaty开发的一款娱乐性质的机器人。
# 主要功能
* B站视频分享链接自动解析功能 
* 抖音视频分享链接自动解析功能
* 网易云热评功能
* 微博热搜功能
* 摸鱼图
# 功能演示
### B站视频分享链接自动解析  
被动技能，无命令。
当用户发送的聊天信息中，包含B站视频链接时，机器人将自动解析视频各种信息，并发送视频消息。支持BV，av，b23.tv的链接。方便微信群内分享视频，可以快速了解到分享的内容
![B站链接解析](https://user-images.githubusercontent.com/104504661/165520309-86cbb08b-c748-4300-ae0d-41de720a58ad.png)

### 抖音分享链接自动解析  
被动技能，无命令。
由于微信屏蔽抖音链接，每次分享的时候，都需要自己下载再上传视频，比较麻烦，所以做了这个功能，方便微信群内大家分享视频。此功能自动检测含有 “https://v.douyin.com” 的聊天信息，然后解析视频信息，并自动下载上传视无水印视频。下次再分享抖音视频的时候，直接选择【复制链接】，发送链接即可。
![image](https://user-images.githubusercontent.com/104504661/165521073-866aa668-c421-40c8-b97b-73b18978c625.png)
### 网易云热评
命令：到点了  |  网易云  |  我好难过  
收到用户命令时，将随机发送网易云音乐的歌曲热评一条。  
![网抑云](https://user-images.githubusercontent.com/104504661/165522957-b5c8bd64-52f7-4597-8981-7f3b943397a2.png)

### 微博热搜
命令：微博  |  微博  |  微博热搜  
收到用户命令时，将发送此刻微博热搜榜前15。  
![微博热搜](https://user-images.githubusercontent.com/104504661/165522790-f6a4ec29-82e0-470e-a252-42bb928c7d7f.png)
### 摸鱼图
命令：摸鱼
收到用户命令时，将发送一张摸鱼图。  
![image](https://user-images.githubusercontent.com/104504661/165523603-b12e7f2e-4390-44c3-835a-caeb351ce8f6.png)
# linux部署方法
本机器人基于python-wechaty的pad-local协议，采用插件的方式组织。
### 1、python-wechaty的安装
详见python-wechaty官网文档。传送门[python-wechaty文档](https://wechaty.readthedocs.io/zh_CN/latest/introduction/use-padlocal-protocol/)
### 2、安装xin_bot
```bash
git clone https://github.com/xin0501/xin_bot.git
```
### 3、配置pad-local协议
编辑xin_bot.py文件中，相关部分。  
```python
os.environ['TOKEN'] = "uuid"   # wechaty-puppet-padlocal中使用的uuid
os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = "ip:port"  # wechaty-puppet-padlocal中设置的ip和端口
```
# 启动方法
运行shell目录下的pad_env.sh，启动启动Padlocal网关服务  
```bash
./shell/pad_env.sh
```
* 启动xin_bot机器人  
```
python xin_bot.py
```
首次启动时，使用手机微信，扫描二维码登录，后续即可自动登录。
