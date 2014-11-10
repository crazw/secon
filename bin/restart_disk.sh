#!/bin/bash

#set -x
disk_dir=`dirname $0`
disk_fp="${disk_dir%/*}/main_disk.py"
if [ "`ps axu | grep "${disk_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${disk_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${disk_dir}/startup_disk.sh