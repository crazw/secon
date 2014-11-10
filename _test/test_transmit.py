#!/usr/bin/env python
#encoding=utf-8

import os
import lib.secon_util_lib as util
import lib.secon_socket_lib as pipelib

#curl -XDELETE 'http://localhost:9200/logstash-2014.10.11/'

if __name__ == '__main__' :

	_dict = {
		'user_id'		: 	'10001',
		'domain_id'		: 	'10001',
		'sub_id'		: 	'10001',
		
		'category'		:	'sys', 
		'node_name'		:	'NODE_ALI',
		'label'			: 	'测试网站',
		'domain' 		:	'www.zcoson.com'
	}
	
	pipelib.send_msg_object(_dict)
