#!/bin/bash

#set -x
dns_dir=`dirname $0`
dns_fp="${dns_dir%/*}/main_dns.py"
if [ "`ps axu | grep "${dns_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
  kill -9 `ps axu | grep "${dns_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
sleep 0.5
${dns_dir}/startup_dns.sh