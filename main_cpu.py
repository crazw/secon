#!/usr/bin/env python
#encoding=utf-8

import sys, time, gevent

import lib.secon_log_lib as log
import lib.secon_snmp2 as snmpv2
import lib.secon_socket_lib as msglib

import handler_cache as mcache
import handler_host as hostutil

def worker(_id):

	_dict = mcache.get_cpu(_id)
	
	category = _dict.get('category', False)
	if not category:
		raise Exception('[handler_host.handler_main] data.category is None')

	host = _dict.get('domain', False)
	if not host:
		raise Exception('[handler_host.handler_main] data.host_ip is None')

	port = int(_dict.get('snmp_port', '0'))
	if 0 == port:
		raise Exception('[handler_host.handler_main] data.host_port is None')

	community = _dict.get('community', False)
	if not community:
		raise Exception('[handler_host.handler_main] data.community is None')

	_key = '%s' % _dict.get('domain_id', '0')

	if 'Y'==_dict.get('purge', 'N'):
		hostutil.remove_host_info(_key)

	hostinfo = hostutil.get_hostinfo(_key, host, port, community)

	if False == hostinfo:
		_dict['used'] = 0
		_dict['status'] = 0
		msglib.send_msg_object(_dict)
		return False

	if 'Windows' == hostinfo.get('sys').get('ostype'):
		import lib.secon_snmp2_winlib as snmpv2lib
	else:
		import lib.secon_snmp2_unixlib as snmpv2lib

	_cpu_data = {}
	_cpu_data.update(_dict)

	cpu_used = snmpv2lib.get_cpu_load(host, port, community)
	if False == cpu_used:
		_cpu_data['status'] = 0
	else:
		_cpu_data['status'] = 1
		_cpu_data['used'] = int(cpu_used)

	msglib.send_msg_object(_cpu_data)

	gevent.sleep(int(_dict.get('timeout', '1')))

def add_job_cpu(ids):
	if not ids:
		log.error('main_cpu.execute_job', '[CPU] not task')
	
	threads = []
	for _id in ids:
		threads.append(gevent.spawn(worker, _id))

	try:
		gevent.joinall(threads)
	except Exception as e:
		print('This will never be reached')

if __name__ == '__main__' :
	if 1 == len(sys.argv):
		log.error('main_cpu.execute_job', 'argv[1] is None')
		sys.exit(0)
	else:
		try:
			int(sys.argv[1])
		except Exception, e:
			log.error('main_cpu.execute_job', 'argv[1] is not number')
			sys.exit(0)
		while True:
			mcache.list_cpu(int(sys.argv[1]), True)
			add_job_cpu(mcache.get_cpu_keys())
			time.sleep(60)
