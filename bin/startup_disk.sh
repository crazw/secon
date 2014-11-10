#!/bin/bash

#set -x
count=1
disk_dir=`dirname $0`
disk_fp="${disk_dir%/*}/main_disk.py"
disk_lp="${disk_dir%/*}/logs/worker_disk.log"

if [ "`ps axu | grep "${disk_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "Disk Started PID:" `ps axu | grep "${disk_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${disk_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${disk_fp} ${i} > ${disk_lp} 2>&1 &
done;
echo "Disk Started PID:" `ps axu | grep "${disk_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
