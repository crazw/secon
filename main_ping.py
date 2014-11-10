#!/usr/bin/env python
#encoding=utf-8

import sys, time, gevent
import handler_cache as mcache

import lib.secon_log_lib as log
import lib.secon_ping_lib as pinglib
import lib.secon_socket_lib as msglib

def worker(_id):

	_data = mcache.get_ping(_id)

	domain = _data.get('domain', False)
	if not domain:
		return False
	domain = domain.encode("utf-8")
	# log.info('worker', domain);

	time_total, message = pinglib.check(domain)
	data_ping = {
		'status' : 0,
		'time_total' : 0,
		'errmsg': message
	}
	if 0 < time_total:
		data_ping['status'] = 1
		data_ping['time_total'] = float('%.3f' % time_total)

	_data.update(data_ping)
	
	msglib.send_msg_object(_data)

	gevent.sleep(int(_data.get('timeout', '1')))

def add_job_ping(ids):
	if not ids:
		log.error('main.execute_job', '[Ping] not task')

	threads = []
	for _id in ids:
		threads.append(gevent.spawn(worker, _id))
	try:
		gevent.joinall(threads)
	except Exception as e:
		log.error('main.add_job_ping', '[Ping] add task')

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
			mcache.list_ping(int(sys.argv[1]), True)
			add_job_ping(mcache.get_ping_keys())
			time.sleep(60)
