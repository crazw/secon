#!/usr/bin/env python
#encoding=utf-8

import time
import handler_host as host
import lib.secon_snmp2 as snmpv2

if __name__ == '__main__' :

	_data = {
		'host_port'		:	161, 
		'community'		:	'public', 
		'domain' 		:	'69.85.87.235'
	}

	sysinfo = snmpv2.get_system_info(_data['domain'], _data['host_port'], _data['community'])
	# print 'sysinfo       ', sysinfo

	# print 'uptime        ', snmpv2.get_sys_uptime(_data['domain'], _data['host_port'], _data['community'])

	if 'Windows' == sysinfo.get('ostype', ''):
		import lib.secon_snmp2_winlib as snmpv2lib
	else:
		import lib.secon_snmp2_unixlib as snmpv2lib

	# print 'cpu_used      ', snmpv2lib.get_cpu_load(_data['domain'], _data['host_port'], _data['community'])

	# disk_label = snmpv2lib.get_disk_label(_data['domain'], _data['host_port'], _data['community'])
	# print 'disk_label    ', disk_label

	# disk_unit = snmpv2lib.get_disk_unit(_data['domain'], _data['host_port'], _data['community'])
	# print 'disk_unit     ', disk_unit

	# print 'disk_used     ', snmpv2lib.get_disk_used(_data['domain'], _data['host_port'], _data['community'], disk_unit, disk_label)

	# print 'memory        ', snmpv2lib.get_memory_used(_data['domain'], _data['host_port'], _data['community'], disk_unit, disk_label)

	network_label = snmpv2lib.get_network_label(_data['domain'], _data['host_port'], _data['community'])
	print 'network_label ', network_label

	# network_lastdata = snmpv2lib.get_network_last(_data['domain'], _data['host_port'], _data['community'], sysinfo.get('osbit', False), network_label)
	# time.sleep(60)
	# print 'network_used  ', snmpv2lib.get_network_used(_data['domain'], _data['host_port'], _data['community'], 
	# 	sysinfo.get('osbit', False), network_label, network_lastdata)

	# print 'process_count ', snmpv2.get_process_count(_data['domain'], _data['host_port'], _data['community'])