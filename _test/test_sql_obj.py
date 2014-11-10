#!/usr/bin/env python
#encoding=utf-8

from config import THREAD
import handler_cache as cache
import handler_model as modelJob

def test_ping():

	cache.list_ping(1)
	ids = cache.get_ping_keys()
	print ids
	print cache.get_ping(ids[0])

def test_dns():

	cache.list_dns(1)
	ids = cache.get_dns_keys()
	print ids
	print cache.get_dns(ids[0])

def test_http():

	cache.list_http(1)
	ids = cache.get_http_keys()
	print ids
	print cache.get_http(ids[0])

def test_port():

	cache.list_port(1)
	ids = cache.get_port_keys()
	print ids
	print cache.get_port(ids[0])

def test_host():

	cache.list_port(1)
	ids = cache.get_port_keys()
	print ids
	print cache.get_port(ids[0])


if __name__ == '__main__' :
	
	# test_ping()
	print "\n\n"

	# test_dns()
	print "\n\n"

	# test_http()
	print "\n\n"

	# test_port()
	print "\n\n"

	# print modelJob.job_host_list('cpu', 1, 10)

