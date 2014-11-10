#!/bin/bash

#set -x
count=1
network_dir=`dirname $0`
network_fp="${network_dir%/*}/main_network.py"
network_lp="${network_dir%/*}/logs/worker_network.log"

if [ "`ps axu | grep "${network_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "Network Started PID:" `ps axu | grep "${network_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${network_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${network_fp} ${i} > ${network_lp} 2>&1 &
done;
echo "Network Started PID:" `ps axu | grep "${network_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
