#!/bin/bash

#set -x
count=1
ping_dir=`dirname $0`
ping_fp="${ping_dir%/*}/main_ping.py"
ping_lp="${ping_dir%/*}/logs/worker_ping.log"

if [ "`ps axu | grep "${ping_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "Ping Started PID:" `ps axu | grep "${ping_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${ping_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${ping_fp} ${i} > ${ping_lp} 2>&1 &
done;
echo "Ping Started PID:" `ps axu | grep "${ping_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
