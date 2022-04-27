#!/bin/bash
###
 # @Author: xin
 # @Date: 2022-04-27 22:07:05
 # @LastEditors: xin
 # @LastEditTime: 2022-04-27 22:08:06
 # @Description: 机器人重启基本
 # @FilePath: /xin_bot/restart.sh
### 
# shellcheck disable=SC2006
# shellcheck disable=SC2009
ID=`ps -ef|grep xin_bot.py | grep -v grep | awk '{print$2}'`
echo "$ID"
kill -9 "$ID"
echo "kill $ID"
sleep 3
nohup python3 xin_bot.py > bot.log 2>&1 &
#tail -f bot.log
