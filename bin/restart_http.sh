#!/bin/bash

#set -x
http_dir=`dirname $0`
http_fp="${http_dir%/*}/main_http.py"
if [ "`ps axu | grep "${http_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${http_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${http_dir}/startup_http.sh