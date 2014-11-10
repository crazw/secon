#!/bin/bash

#set -x
sys_dir=`dirname $0`
sys_fp="${sys_dir%/*}/main_sys.py"
if [ "`ps axu | grep "${sys_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${sys_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${sys_dir}/startup_sys.sh