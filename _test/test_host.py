#!/usr/bin/env python
#encoding=utf-8

import time
import handler_host as host

if __name__ == '__main__' :

	_data = {
		'domain_id'		: 	8,
		'host_port'		:	161, 
		'community'		:	'public', 
		'category'		:   'cpu',
		'domain' 		:	'107.189.158.100',
		'purge'			: 	'Y'
	}

	host.handler_main(_data)
