#!/usr/bin/env python
#encoding=utf-8

'''
Author: SecOn 团队
Description: tcp检测
Create Date: 2013-10-25
'''

import sys, time, socket
from datetime import datetime
import lib.secon_log_lib as log
import lib.secon_util_lib as util


def check(host, port, count = 2):

	artt = None
	plist = []
	message = ''

	for i in xrange(count):
		try:

			client = socket.socket()
			client.settimeout(1)

			start = datetime.now()
			client.connect((host, int(port)))
			client.send('PORT_IS_ALIVE')
			client.close()
			end = datetime.now()

			resp_time = (end - start).microseconds / float(1000)
			if 0 < resp_time:
				plist.append(resp_time)

		except Exception, e:
			message = 'TCP连接失败:%s' % str(e)
			time.sleep(0.1)
			continue

	if plist:
		artt = sum(plist) / len(plist)
		message = ''
	else:
		artt = 0

	if 0 == artt:
		log.error('secon_port_lib.check', '[%s:%s] %s' % (host, port, message))

	return artt, message
