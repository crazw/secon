#!/bin/bash

mntrdir=`dirname $0`
file_fp=${mntrdir%/*}/main
if [ "`ps axu | grep "${file_fp}" | grep -v 'grep' | awk '{print $2}'`" ]; then
kill -9 `ps axu | grep "${file_fp}" | grep -v 'grep' | awk '{print $2}'`
fi
echo "Stoped."