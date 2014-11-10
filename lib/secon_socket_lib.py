#!/usr/bin/env python
#encoding=utf-8

'''
Author: SecOn 团队
Description: 
Create Date: 2013-10-24
'''

#import socket, gevent
from gevent import socket
from config import SOCKET
from config import LASTDATA
import lib.secon_log_lib as log
import lib.secon_util_lib as util
import secon_httpclient as httpclient


def send_msg_object(_data):

	_data['time_add'] = util.strdatetime()
	_data['time_add_unix'] = util.longtime()

	content = util.objtostr(_data)

	# print _data['domain'], _data['http_code']

	# httpclient.post(LASTDATA['URI'], content)

	send_message_content(SOCKET['HOST'], SOCKET['PORT'], content)

def send_message_content(_host, _port, _message):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(20)
		s.connect((_host, int(_port)))
		s.setblocking(0)
		s.sendall(_message)
		s.close()
		log.info('soket.send_message ', '[Succed] %s' % _message)
	except Exception, e:
		log.error('soket.send_message ', '[Except] {%s} %s' % (str(e), _message))
		# raise Exception("[soket.send_message] Except:{%s} %s" % (str(e), _message))
