#!/bin/bash

mntrbindir=`dirname $0`

${mntrbindir}/restart_dns.sh
${mntrbindir}/restart_ping.sh
${mntrbindir}/restart_http.sh
${mntrbindir}/restart_port.sh
${mntrbindir}/restart_sys.sh
${mntrbindir}/restart_cpu.sh
${mntrbindir}/restart_disk.sh
${mntrbindir}/restart_memory.sh
${mntrbindir}/restart_network.sh
${mntrbindir}/restart_process.sh
