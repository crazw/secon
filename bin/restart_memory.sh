#!/bin/bash

#set -x
memory_dir=`dirname $0`
memory_fp="${memory_dir%/*}/main_memory.py"
if [ "`ps axu | grep "${memory_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${memory_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${memory_dir}/startup_memory.sh