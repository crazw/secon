#!/bin/bash

#set -x
count=1
dns_dir=`dirname $0`
dns_fp="${dns_dir%/*}/main_dns.py"
dns_lp="${dns_dir%/*}/logs/worker_dns.log"

if [ "`ps axu | grep "${dns_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
echo "DNS Started PID:" `ps axu | grep "${dns_fp}" | grep -v 'grep' | awk '{print $2}'`
else
rm -rf ${dns_lp}
for((i=1;i<=$count;i++)); do
nohup python -u ${dns_fp} ${i} > ${dns_lp} 2>&1 &
done;
echo "DNS Started PID:" `ps axu | grep "${dns_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
