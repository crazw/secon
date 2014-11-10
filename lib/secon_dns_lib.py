#!/usr/bin/env python
#encoding=utf-8

'''
Author: SecOn 团队
Description: DNS 检测
Create Date: 2013-10-24
Explain:
	DNS.Type.A = 1
	DNS.Type.MX = 15
	DNS.Type.TXT = 16
	DNS.Type.NS = 2
	DNS.Type.CNAME = 5
'''

import datetime, dns.resolver
import lib.secon_log_lib as log
import lib.secon_util_lib as util

def check(domain, qtype):
	if not domain.strip():
		raise Exception('[secon_dns_lib.check] domain is None')

	if not qtype.strip():
		raise Exception('[secon_dns_lib.check] type is None')

	if 'A' == qtype:
		return get_dns_a(domain)
	elif 'NS' == qtype:
		return get_dns_ns(domain)
	elif 'MX' == qtype:
		return get_dns_mx(domain)
	elif 'TXT' == qtype:
		return get_dns_txt(domain)
	elif 'CNAME' == qtype:
		return get_dns_cname(domain)
	else:
		pass

def get_dns_a(domain):
	try:

		start = datetime.datetime.now()
		answers = dns.resolver.query(domain, 'A')
		end = datetime.datetime.now()

		resp_time = (end - start).microseconds / float(1000)
		if (0 >= resp_time):
			resp_time = 0.1

		if not answers:
			return 'Unknown', 0

		resp_data = ''
		for rdata in answers:
			resp_data = rdata.address

		return resp_data, resp_time
	except Exception, error:
		errormsg = 'DNS解析失败'
		log.error('secon_dns_lib.get_dns_a', '[%s:A] %s' % (domain, errormsg))
		return errormsg, 0

def get_dns_ns(domain):
	try:

		start = datetime.datetime.now()
		answers = dns.resolver.query(domain, 'NS')
		end = datetime.datetime.now()

		#microsecond是微秒需要除以1000才能取出毫秒数
		resp_time = (end - start).microseconds / float(1000) 
		if (0 >= resp_time):
			resp_time = 0.1

		if not answers:
			return 'Unknown', 0

		resp_data = ''
		for rdata in answers:
			_ns = rdata.to_text()
			if '.' == _ns[-1]:
				resp_data += '%s,' % _ns[0:-1]
			else:
				resp_data += '%s,' % _ns

		if ',' == resp_data[-1]:
			resp_data = resp_data[0:-1]

		return resp_data, resp_time
	except Exception, error:
		errormsg = 'DNS解析失败'
		log.error('secon_dns_lib.get_dns_ns', '[%s:NS] %s' % (domain, errormsg))
		return errormsg, 0

def get_dns_mx(domain):
	try:
		start = datetime.datetime.now()
		answers = dns.resolver.query(domain, 'MX')
		end = datetime.datetime.now()

		resp_time = (end - start).microseconds / float(1000)
		if (0 >= resp_time):
			resp_time = 0.1

		if not answers:
			return 'Unknown', resp_time

		resp_data = ''
		for rdata in answers:
			_mx = str(rdata.exchange)
			if '.' == _mx[-1]:
				resp_data = _mx[0:-1]
			else:
				resp_data = _mx

		return resp_data, resp_time
	except Exception, error:
		errormsg = 'DNS解析失败'
		log.error('secon_dns_lib.get_dns_mx', '[%s:MX] %s' % (domain, errormsg))
		return errormsg, 0

def get_dns_txt(domain):
	try:

		start = datetime.datetime.now()
		answers = dns.resolver.query(domain, 'TXT')
		end = datetime.datetime.now()

		resp_time = (end - start).microseconds / float(1000)
		if (0 >= resp_time):
			resp_time = 0.1

		resp_data = ''
		if not answers:
			return 'Unknown', resp_time

		for rdata in answers:
			resp_data = str(rdata).replace('"','')

		return resp_data, resp_time
	except Exception, error:
		errormsg = 'DNS解析失败'
		log.error('secon_dns_lib.get_dns_txt', '[%s:TXT] %s' % (domain, errormsg))
		return errormsg, 0

def get_dns_cname(domain):
	try:

		start = datetime.datetime.now()
		answers = dns.resolver.query(domain, 'CNAME')
		end = datetime.datetime.now()

		resp_time = (end - start).microseconds / float(1000)
		if (0 >= resp_time):
			resp_time = 0.1

		if not answers:
			return 'Unknown', resp_time

		resp_data = ''
		for rdata in answers:
			_cname = str(rdata.target)
			if '.' == _cname[-1]:
				resp_data += '%s,' % _cname[0:-1]
			else:
				resp_data += '%s,' % _cname

		return resp_data, resp_time
	except Exception, error:
		errormsg = 'DNS解析失败'
		log.error('secon_dns_lib.get_dns_cname', '[%s:CNAME] %s' % (domain, errormsg))
		return errormsg, 0