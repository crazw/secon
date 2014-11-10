#!/bin/bash

#set -x
count=1
http_dir=`dirname $0`
http_fp="${http_dir%/*}/main_http.py"
http_lp="${http_dir%/*}/logs/worker_http.log"

if [ "`ps axu | grep "${http_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "HTTP Started PID:" `ps axu | grep "${http_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf "${http_lp}"
for((i=1;i<=$count;i++)); do
nohup python -u ${http_fp} ${i} > ${http_lp} 2>&1 &
done;
echo "HTTP Started PID:" `ps axu | grep "${http_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
