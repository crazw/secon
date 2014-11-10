#!/usr/bin/env python
#encoding=utf-8

import sys, time, gevent
import handler_cache as mcache

import lib.secon_log_lib as log
import lib.secon_http_lib as httplib
import lib.secon_socket_lib as msglib

def worker(_id):

	_data = mcache.get_http(_id)

	domain = _data.get('domain', False)
	if not domain:
		return False

	protocol = _data.get('protocol', False)
	if not protocol:
		return False

	path = _data.get('path', False)
	if not path:
		return False

	port = _data.get('port', False)
	if not port:
		return False

	path = path.encode("utf-8")
	domain = domain.encode("utf-8")
	protocol = protocol.encode("utf-8")

	data_http = httplib.check(protocol, domain, port, path)

	data_http['status'] = 0

	avail_hc = _data.get('avail_hc', '200').split(',')
	if str(data_http['http_code']) in avail_hc:
		data_http['status'] = 1

	_data.update(data_http)

	msglib.send_msg_object(_data)

	gevent.sleep(int(_data.get('timeout', '1')))

def add_job_http(ids):
	if not ids:
		log.error('main.execute_job', '[HTTP] not task')

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
			mcache.list_http(int(sys.argv[1]), True)
			add_job_http(mcache.get_http_keys())
			time.sleep(60)
