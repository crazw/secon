#!/bin/bash

#set -x
count=1
port_dir=`dirname $0`
port_fp="${port_dir%/*}/main_port.py"
port_lp="${port_dir%/*}/logs/worker_port.log"

if [ "`ps axu | grep "${port_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "Port Started PID:" `ps axu | grep "${port_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${port_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${port_fp} ${i} > ${port_lp} 2>&1 &
done;
echo "Port Started PID:" `ps axu | grep "${port_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
