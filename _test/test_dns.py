#!/usr/bin/env python
#encoding=utf-8

import lib.secon_dns_lib as dnslib

def check_a(domain):
	resp_data, resp_time = dnslib.check(domain, 'A')
	if 0 == resp_time:
		print resp_data, resp_time
	else:
		print resp_data, float('%.3f' % resp_time)

def check_ns(domain):
	resp_data, resp_time = dnslib.check(domain, 'NS')
	if 0 == resp_time:
		print resp_data, resp_time
	else:
		print resp_data, float('%.3f' % resp_time)

def check_mx(domain):
	resp_data, resp_time = dnslib.check(domain, 'MX')
	if 0 == resp_time:
		print resp_data, resp_time
	else:
		print resp_data, float('%.3f' % resp_time)

def check_txt(domain):
	resp_data, resp_time = dnslib.check(domain, 'TXT')
	if 0 == resp_time:
		print resp_data, resp_time
	else:
		print resp_data, float('%.3f' % resp_time)

def check_cname(domain):
	resp_data, resp_time = dnslib.check(domain, 'CNAME')
	if 0 == resp_time:
		print resp_data, resp_time
	else:
		print resp_data, float('%.3f' % resp_time)

if __name__ == '__main__' :
	
	check_a('www.zcoson.com')

	check_ns('zcoson.com')

	check_mx('xxssw.com')

	check_txt('txt.xxssw.com')

	check_cname('cname.xxssw.com')
