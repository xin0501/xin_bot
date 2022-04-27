# 设置环境变量
###
 # @Author: xin
 # @Date: 2022-04-27 22:06:08
 # @LastEditors: xin
 # @LastEditTime: 2022-04-27 22:06:09
 # @Description: padlocal启动环境
 # @FilePath: /xin_bot/shell/pad_env.sh
### 

export WECHATY_LOG="verbose"
export WECHATY_PUPPET="wechaty-puppet-padlocal"
export WECHATY_PUPPET_PADLOCAL_TOKEN="puppet_padlocal_token"
export WECHATY_PUPPET_SERVICE_NO_TLS_INSECURE_SERVER="true"

export WECHATY_PUPPET_SERVER_PORT="8085"
# 可使用代码随机生成UUID：import uuid;print(uuid.uuid4());
export WECHATY_TOKEN="uuid"

docker run -ti -d \
  --name wechaty_puppet_service_token_gateway \
  --rm \
  -e WECHATY_LOG \
  -e WECHATY_PUPPET \
  -e WECHATY_PUPPET_PADLOCAL_TOKEN \
  -e WECHATY_PUPPET_SERVER_PORT \
  -e WECHATY_PUPPET_SERVICE_NO_TLS_INSECURE_SERVER \
  -e WECHATY_TOKEN \
  -p "$WECHATY_PUPPET_SERVER_PORT:$WECHATY_PUPPET_SERVER_PORT" \
  wechaty/wechaty:0.65

