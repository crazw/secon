#!/usr/bin/env python
#encoding=utf-8

import sys, time, gevent
import handler_cache as mcache

import lib.secon_log_lib as log
import lib.secon_dns_lib as dnslib
import lib.secon_socket_lib as msglib

def worker(_id):

	_data = mcache.get_dns(_id)

	domain = _data.get('domain', False)
	if not domain:
		return False

	qtype = _data.get('qtype', False)
	if not qtype:
		return False

	domain = domain.encode("utf-8")
	qtype = qtype.encode("utf-8")

	resp_data, resp_time = dnslib.check(domain, qtype)

	data_dns = {
		'status': 0,
		'time_total': 0,
		'data': resp_data
	}

	if 0 < resp_time:
		data_dns['time_total'] = float('%.3f' % resp_time)
		qvalue = _data.get('qvalue', '')
		if '' == qvalue:
			data_dns['status'] = 1
		else:
			if qvalue == resp_data:
				data_dns['status'] = 1

	_data.update(data_dns)

	msglib.send_msg_object(_data)

	gevent.sleep(int(_data.get('timeout', '1')))

def add_job_dns(ids):
	if not ids:
		log.error('main.execute_job', '[DNS] not task')
	
	threads = []
	for _id in ids:
		threads.append(gevent.spawn(worker, _id))

	try:
		gevent.joinall(threads)
	except Exception as e:
		print('This will never be reached')

if __name__ == '__main__' :
	if 1 == len(sys.argv):
		log.error('main.execute_job', 'argv[1] is None')
		sys.exit(0)
	else:
		try:
			int(sys.argv[1])
		except Exception, e:
			log.error('main.execute_job', 'argv[1] is not number')
			sys.exit(0)
		while True:
			mcache.list_dns(int(sys.argv[1]), True)
			add_job_dns(mcache.get_dns_keys())
			time.sleep(60)
