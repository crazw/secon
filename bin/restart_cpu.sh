#!/bin/bash

#set -x
cpu_dir=`dirname $0`
cpu_fp="${cpu_dir%/*}/main_cpu.py"
if [ "`ps axu | grep "${cpu_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${cpu_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${cpu_dir}/startup_cpu.sh