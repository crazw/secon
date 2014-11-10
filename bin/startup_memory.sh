#!/bin/bash

#set -x
count=1
memory_dir=`dirname $0`
memory_fp="${memory_dir%/*}/main_memory.py"
memory_lp="${memory_dir%/*}/logs/worker_memory.log"

if [ "`ps axu | grep "${memory_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "Memory Started PID:" `ps axu | grep "${memory_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${memory_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${memory_fp} ${i} > ${memory_lp} 2>&1 &
done;
echo "Memory Started PID:" `ps axu | grep "${memory_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
