#!/bin/bash

#set -x
count=1
cpu_dir=`dirname $0`
cpu_fp="${cpu_dir%/*}/main_cpu.py"
cpu_lp="${cpu_dir%/*}/logs/worker_cpu.log"

if [ "`ps axu | grep "${cpu_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "CPU Started PID:" `ps axu | grep "${cpu_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${cpu_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${cpu_fp} ${i} > ${cpu_lp} 2>&1 &
done;
echo "CPU Started PID:" `ps axu | grep "${cpu_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
