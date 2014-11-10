#!/bin/bash

#set -x
network_dir=`dirname $0`
network_fp="${network_dir%/*}/main_network.py"
if [ "`ps axu | grep "${network_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${network_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${network_dir}/startup_network.sh