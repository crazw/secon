#!/usr/bin/env python
#encoding=utf-8

import os
import lib.secon_util_lib as util
import lib.secon_http_lib as httplib

#curl -XDELETE 'http://localhost:9200/logstash-2014.10.11/'

if __name__ == '__main__' :

	# print httplib.check('http', 'www.7651.com', '80', '/')
	# print httplib.check('https', 'cns.lillydr.cn', '443', '/')
	print httplib.check('https', 'svn.logbt.net', '443', '/')

