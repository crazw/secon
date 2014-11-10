#!/usr/bin/env python
#encoding=utf-8

'''
Author:	SecOn 团队
Description: 主程序
Create Date: 2013-10-24
'''

import sys

def check_json():
	try:
		import simplejson
		print 'simplejson Already installed'
	except Exception, e:
		print 'simplejson not install'


def check_pycurl():
	try:
		import pycurl
		print 'pycurl Already installed'
	except Exception, e:
		print 'pycurl not install'


def check_httplib2():
	try:
		import httplib2
		print 'httplib2 Already installed'
	except Exception, e:
		print 'httplib2 not install'


def check_DNS():
	try:
		import dns.resolver
		print 'dns.resolver Already installed'
	except Exception, e:
		print 'dns.resolver not install'


def check_gearman():
	try:
		import gearman
		print 'gearman Already installed'
	except Exception, e:
		print 'gearman not install'


def check_snmp():
	try:
		from pysnmp.proto.rfc1902 import ObjectName
		print 'pysnmp Already installed'
	except Exception, e:
		print 'pysnmp not install'


def check_gevent():
	try:
		import gevent
		print 'gevent Already installed'
	except Exception, e:
		print 'gevent not install'

if __name__ == '__main__' :

	check_json()
	check_DNS()
	check_pycurl()
	# check_httplib2()
	# check_gearman()
	check_snmp()
	check_gevent()

	sys.exit(0)

