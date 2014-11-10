#!/usr/bin/env python
#encoding=utf-8

import sys, os, socket
import lib.secon_log_lib as log
import lib.secon_util_lib as util
import lib.secon_snmp2 as snmpv2
import lib.secon_socket_lib as msglib

# import threading
# class threadHost(threading.Thread):

# 	def __init__(self, data):
# 		threading.Thread.__init__(self)
# 		self.data = data

# 	def run(self):
# 		handler_main(self.data)

# def handler_start(_dict):
# 	threadHost(_dict).start()

# ===========================================
def read_host_info(_key):
	filepath = '%s/data/host_%s.json' % (sys.path[0], _key)
	return util.strtojson(util.file_read(filepath))

def write_host_info(_key, _object):
	filepath = '%s/data/host_%s.json' % (sys.path[0], _key)
	util.file_write(filepath, util.objtostr(_object))

def remove_host_info(_key):
	os.remove('%s/data/host_%s.json' % (sys.path[0], _key))

#==================================================

def get_hostinfo(_key, host, port, community):
	
	enable_write = False
	hostinfo = read_host_info(_key)

	# log.info('handler_host.get_hostinfo', hostinfo)

	if not hostinfo.get('sys', False):
		enable_write = True
		host_sys = snmpv2.get_system_info(host, port, community)
		if False == host_sys:
			hostinfo['sys'] = False
			write_host_info(_key, hostinfo)
			return False

		hostinfo['sys'] = host_sys

	if 'Windows' == hostinfo.get('sys').get('ostype',''):
		import lib.secon_snmp2_winlib as snmpv2lib
	else:
		import lib.secon_snmp2_unixlib as snmpv2lib

	if not hostinfo.get('unit', False):
		enable_write = True
		hostinfo['unit'] = snmpv2lib.get_disk_unit(host, port, community)

	if not hostinfo.get('dlabel', False):
		enable_write = True
		hostinfo['dlabel'] = snmpv2lib.get_disk_label(host, port, community)

	if not hostinfo.get('nlabel', False):
		enable_write = True
		hostinfo['nlabel'] = snmpv2lib.get_network_label(host, port, community)

	_sysbit = hostinfo.get('sys').get('osbit', '64')
	if not hostinfo.get('ndata', False):
		enable_write = True
		hostinfo['ndata'] = snmpv2lib.get_network_last(host, port, community, _sysbit, hostinfo.get('nlabel'))

	if enable_write:
		write_host_info(_key, hostinfo)

	return hostinfo
