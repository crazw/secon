#!/usr/bin/env python
#encoding=utf-8

'''
Author: SecOn 团队
Description: 网站存活性检测
Create Date: 2013-10-24
'''

import os,pycurl, StringIO
import lib.secon_log_lib as log
import lib.secon_util_lib as util

def check(protocol,domain,port,path) :

	http_url = '%s://%s:%s%s' % (protocol, domain, port, path)

	_dict = {'http_code':0, 'time_total':0, 'time_connect':0, 'time_lookup':0, 'time_transfer':0}

	try :

		request = pycurl.Curl()
		request.setopt(pycurl.URL, http_url)
		request.setopt(pycurl.HTTPHEADER, ['Accept: text/html', 'Accept-Charset: UTF-8'])
		request.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36")
		request.setopt(pycurl.CONNECTTIMEOUT, 50)
		request.setopt(pycurl.TIMEOUT, 30)
		request.setopt(pycurl.COOKIEFILE, '')
		# request.setopt(pycurl.FAILONERROR, 1)

		request.setopt(pycurl.SSL_VERIFYPEER, 0)
		request.setopt(pycurl.SSL_VERIFYHOST, 0)
		request.setopt(pycurl.IPRESOLVE, pycurl.IPRESOLVE_V4)

		# request.buf = StringIO.StringIO()
		headers = StringIO.StringIO()
		request.setopt(pycurl.NOBODY, 1)
		request.setopt(pycurl.WRITEFUNCTION, headers.write)
		request.perform()

		#响应代码
		_dict['http_code'] = int('%s' % (request.getinfo(pycurl.HTTP_CODE)))
		#远程服务器连接时间
		_dict['time_connect'] = float('%.3f' % (1000 * request.getinfo(pycurl.CONNECT_TIME)))
		#域名解析时间
		_dict['time_lookup'] = float('%.3f' % (1000 * request.getinfo(pycurl.NAMELOOKUP_TIME)))
		
		#如果存在转向的话，花费的时间
		#_dict['http_redirect'] = '%.3f' % (1000 * request.getinfo(pycurl.REDIRECT_TIME))
		#连接上后到开始传输时的时间
		#_dict['http_pre_tran'] = '%.3f' % (1000 * request.getinfo(pycurl.PRETRANSFER_TIME))
		
		#接收到第一个字节的时间
		_dict['time_transfer'] = float('%.3f' % (1000 * request.getinfo(pycurl.STARTTRANSFER_TIME)))
		#请求总的时间
		_dict['time_total'] = float('%.3f' % (1000 * request.getinfo(pycurl.TOTAL_TIME)))
		
		request.close()
		
		return _dict
	except Exception, e:

		log.error('secon_http_lib.check', '[%s] %s' % (http_url, str(e)))
		# raise Exception, "[secon_http_lib.check] runtime error: [%s]" % e

		_dict['http_code'] = 0
		return _dict
