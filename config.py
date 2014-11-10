#!/usr/bin/env python
#encoding=utf-8

#from ctrlpy.etc.config import SOCKET

CONFIG = {
	'NAME'			: '_node_name_',
	'LABEL'			: '_node_label_',
	'TITLE'			: '网站安全监控平台'
}

DATE = {
	'TIMEPAT'		: '%H:%M:%S',
	'DATEPAT'		: '%Y-%m-%d',
	'PATTERN'		: '%Y-%m-%d %H:%M:%S'
}

LOG = {
	'ENABLED'		: False,
	'LEVEL'			: 'info'
}

THREAD = {
	'DNS_JOB_SIZE'		: 60,
	'PING_JOB_SIZE'		: 60,
	'HTTP_JOB_SIZE'		: 60,
	'PORT_JOB_SIZE'		: 60,
	'SYS_JOB_SIZE'		: 60,
	'CPU_JOB_SIZE'		: 60,
	'DISK_JOB_SIZE'		: 60,
	'MEMORY_JOB_SIZE'	: 60,
	'NETWORK_JOB_SIZE'	: 60,
	'PROCESS_JOB_SIZE'	: 60
}

SOCKET = {
	'PORT'			: '_es_port_',
	'HOST'			: '_es_host_'
}

LASTDATA = {
	'URI'			: '_es_uri_',
}

MAIL = {
	'ENABLE'		: False,
	# 'HOST'			: 'smtp.gmail.com:587',
	'HOST'			: 'smtp.exmail.qq.com:465',
	'USER'			: 'support@secon.me',
	'PASS'			: 'secontech110',
	'FROM'			: '%s<support@secon.me>' % CONFIG['TITLE'],
	'TO'			: 'bug@secon.me'
}
