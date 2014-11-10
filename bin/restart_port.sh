#!/bin/bash

#set -x
port_dir=`dirname $0`
port_fp="${port_dir%/*}/main_port.py"
if [ "`ps axu | grep "${port_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${port_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${port_dir}/startup_port.sh