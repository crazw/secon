#!/usr/bin/env python
#encoding=utf-8

'''
Author: SecOn 团队
Description: 
Create Date: 2013-10-24
'''

import os,pipes
import lib.secon_log_lib as log
import lib.secon_util_lib as util

from config import LASTDATA
import secon_httpclient as httpclient

pfile_path = os.path.abspath(os.path.join(\
	os.path.dirname(__file__), os.path.pardir))

fpipe = open('%s/%s' % (pfile_path, 'client.pipe'), 'w')

def send_msg_object(_data):
	_data['time_add'] = util.strdatetime()
	_data['time_add_unix'] = util.longtime()
	content = util.objtostr(_data).replace('\n','')

	# log.info('send_msg_object', content);
	# httpclient.post(LASTDATA['URI'], content)

	fpipe.write('%s\n' % content)

	# fpipe.close()
