#!/usr/bin/env python
#encoding=utf-8

from config import THREAD
import handler_model as modelJob

#===============================

global _list_ping
_list_ping = {}

def list_ping(limit, force=False):
	global _list_ping
	if force or not _list_ping:
		_data_ping = modelJob.job_ping_list(limit, THREAD['PING_JOB_SIZE'])
		if _data_ping:
			for data in _data_ping:
				_list_ping[data.get('sub_id', '')] = data

def get_ping(id):
	global _list_ping
	return _list_ping.get(id)

def get_ping_keys():
	global _list_ping
	return _list_ping.keys()


#===============================
global _list_dns
_list_dns = {}

def list_dns(limit, force=False):
	global _list_dns
	if force or not _list_dns:
		_data_dns = modelJob.job_dns_list(limit, THREAD['DNS_JOB_SIZE'])
		if _data_dns:
			for data in _data_dns:
				_list_dns[data.get('sub_id', '')] = data

def get_dns(id):
	global _list_dns
	return _list_dns.get(id)

def get_dns_keys():
	global _list_dns
	return _list_dns.keys()

#===============================
global _list_http
_list_http = {}

def list_http(limit, force=False):
	global _list_http
	if force or not _list_http:
		_data_http = modelJob.job_http_list(limit, THREAD['HTTP_JOB_SIZE'])
		if _data_http:
			for data in _data_http:
				_list_http[data.get('sub_id', '')] = data

def get_http(id):
	global _list_http
	return _list_http.get(id)

def get_http_keys():
	global _list_http
	return _list_http.keys()

#===============================
global _list_port
_list_port = {}

def list_port(limit, force=False):
	global _list_port
	if force or not _list_port:
		_data_port = modelJob.job_port_list(limit, THREAD['PORT_JOB_SIZE'])
		if _data_port:
			for data in _data_port:
				_list_port[data.get('sub_id', '')] = data

def get_port(id):
	global _list_port
	return _list_port.get(id)

def get_port_keys():
	global _list_port
	return _list_port.keys()

#=================================

global _list_sys
_list_sys = {}

def list_sys(limit, force=False):
	global _list_sys
	if force or not _list_sys:
		_data_sys = modelJob.job_host_list('sys',limit, THREAD['SYS_JOB_SIZE'])
		if _data_sys:
			for data in _data_sys:
				_list_sys[data.get('sub_id', '')] = data

def get_sys(id):
	global _list_sys
	return _list_sys.get(id)

def get_sys_keys():
	global _list_sys
	return _list_sys.keys()

#===============================

global _list_cpu
_list_cpu = {}

def list_cpu(limit, force=False):
	global _list_cpu
	if force or not _list_cpu:
		_data_cpu = modelJob.job_host_list('cpu', limit, THREAD['CPU_JOB_SIZE'])
		if _data_cpu:
			for data in _data_cpu:
				_list_cpu[data.get('sub_id', '')] = data

def get_cpu(id):
	global _list_cpu
	return _list_cpu.get(id)

def get_cpu_keys():
	global _list_cpu
	return _list_cpu.keys()

#===============================

global _list_disk
_list_disk = {}

def list_disk(limit, force=False):
	global _list_disk
	if force or not _list_disk:
		_data_disk = modelJob.job_host_list('disk', limit, THREAD['DISK_JOB_SIZE'])
		if _data_disk:
			for data in _data_disk:
				_list_disk[data.get('sub_id', '')] = data

def get_disk(id):
	global _list_disk
	return _list_disk.get(id)

def get_disk_keys():
	global _list_disk
	return _list_disk.keys()

#===============================

global _list_memory
_list_memory = {}

def list_memory(limit, force=False):
	global _list_memory
	if force or not _list_memory:
		_data_memory = modelJob.job_host_list('memory', limit, THREAD['MEMORY_JOB_SIZE'])
		if _data_memory:
			for data in _data_memory:
				_list_memory[data.get('sub_id', '')] = data

def get_memory(id):
	global _list_memory
	return _list_memory.get(id)

def get_memory_keys():
	global _list_memory
	return _list_memory.keys()

#===============================

global _list_network
_list_network = {}

def list_network(limit, force=False):
	global _list_network
	if force or not _list_network:
		_data_network = modelJob.job_host_list('network', limit, THREAD['NETWORK_JOB_SIZE'])
		if _data_network:
			for data in _data_network:
				_list_network[data.get('sub_id', '')] = data

def get_network(id):
	global _list_network
	return _list_network.get(id)

def get_network_keys():
	global _list_network
	return _list_network.keys()

#===============================

global _list_process
_list_process = {}

def list_process(limit, force=False):
	global _list_process
	if force or not _list_process:
		_data_process = modelJob.job_host_list('process', limit, THREAD['PROCESS_JOB_SIZE'])
		if _data_process:
			for data in _data_process:
				_list_process[data.get('sub_id', '')] = data

def get_process(id):
	global _list_process
	return _list_process.get(id)

def get_process_keys():
	global _list_process
	return _list_process.keys()
