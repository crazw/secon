#!/bin/bash

#set -x
count=1
sys_dir=`dirname $0`
sys_fp="${sys_dir%/*}/main_sys.py"
sys_lp="${sys_dir%/*}/logs/worker_sys.log"

if [ "`ps axu | grep "${sys_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "SYS Started PID:" `ps axu | grep "${sys_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${sys_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${sys_fp} ${i} > ${sys_lp} 2>&1 &
done;
echo "SYS Started PID:" `ps axu | grep "${sys_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
