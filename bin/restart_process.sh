#!/bin/bash

#set -x
process_dir=`dirname $0`
process_fp="${process_dir%/*}/main_process.py"
if [ "`ps axu | grep "${process_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${process_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${process_dir}/startup_process.sh