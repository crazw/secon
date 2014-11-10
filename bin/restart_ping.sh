#!/bin/bash

#set -x
ping_dir=`dirname $0`
ping_fp="${ping_dir%/*}/main_ping.py"
if [ "`ps axu | grep "${ping_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${ping_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${ping_dir}/startup_ping.sh