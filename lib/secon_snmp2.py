#!/usr/bin/env python
#encoding=utf-8

import re,sys,time,types
import lib.secon_log_lib as log
import lib.secon_util_lib as util

from pysnmp.proto.rfc1902 import ObjectName
from pysnmp.entity.rfc3413.oneliner import cmdgen

reload(sys)
sys.setdefaultencoding('utf8')

SNMP = {'AGENT' : 'myagent'}

def snmp_get(host, port, community, objectid, agent=SNMP['AGENT']):
	if not objectid:
		raise Exception("Input(objectid) must no be empty")

	command = cmdgen.CommandGenerator()
	errorIndication, errorStatus, errorIndex, varBindTable = command.getCmd(
		cmdgen.CommunityData(agent, community,1),
		cmdgen.UdpTransportTarget((host, port),retries=3),
		# cmdgen.UdpTransportTarget((host, port),timeout=15,retries=3),
		objectid
	)
	if varBindTable:
		return varBindTable
	else:
		log.error('secon_snmp_lib.snmp_get', '[%s] (%s:%s:%s)' % (str(errorIndication), host, port, community))
		return False

def snmp_next(host, port, community, objectid, agent=SNMP['AGENT']):

	if not objectid:
		raise Exception("Input(objectid) must no be empty")

	command = cmdgen.CommandGenerator()
	errorIndication, errorStatus, errorIndex, varBindTable = command.nextCmd(
		cmdgen.CommunityData(agent, community,1),
		cmdgen.UdpTransportTarget((host, port),retries=3),
		# cmdgen.UdpTransportTarget((host, port),timeout=15,retries=3),
		objectid
	)

	if varBindTable and 0 < len(varBindTable):
		return varBindTable
	else:
		log.error('secon_snmp_lib.snmp_next', '[%s] (%s:%s:%s)' % (str(errorIndication), host, port, community))
		return False

def snmp_info(host, port, community, objectid):
	snmpinfo = snmp_next(host, port, community, objectid)
	i=0
	while True:
		if snmpinfo == False and i<3:
			i = i+1
			snmpinfo = snmp_next(host, port, community, objectid)
		else:
			return snmpinfo

#===========================================================================

def change_dict(snmp_get):
	'''
	把snmp获取来的数据转为字典
	'''
	snmp_dict={}
	for key in snmp_get:		#print f
		snmp_index=key[0][0][-1]
		snmp_values=str(key[0][1])
		idx = snmp_values.find('Label:')
		if idx > 1:
			snmp_values = snmp_values[0:idx]
		snmp_change={str(snmp_index):snmp_values}
		snmp_dict.update(snmp_change)
	return snmp_dict

#===========================================================================

#获取系统的位数，看是64位还是32位
def get_system_info(host, port, community):
	system_oid = ObjectName('1.3.6.1.2.1.1.1')
	system_data = snmp_next(host, port, community, system_oid)
	if isinstance(system_data, bool):
		return False
	else:
		system_name = str(system_data[0][0][1])

		sys_info = {'osdesc':system_name}

		if 'Windows' in system_name:
			sys_info['ostype'] = 'Windows'
		elif 'Linux' in system_name:
			sys_info['ostype'] = 'Linux'
		else:
			sys_info['ostype'] = 'Unknown'

		if 'x86_64' == str(system_name).split()[11]:
			sys_info['osbit'] = '64'
		else:
			sys_info['osbit'] = '32'

		return sys_info

#login 登录用户数量
def get_user_login(host, port, community):
	login_oid = ObjectName('.1.3.6.1.2.1.25.1.5.0')
	login_data = snmp_get(host, port, community, login_oid)
	
	if isinstance(login_data, bool):
		return False
	else:
		return str(login_data[0][1])

# get system os type
def get_sys_uptime(host, port, community):
	uptime_oid = ObjectName('1.3.6.1.2.1.1.3.0')
	uptime_data = snmp_get(host, port, community, uptime_oid)
	if isinstance(uptime_data, bool):
		return False
	else:
		return str(uptime_data[0][1])

#process_num : 进程数量
#return {"process_num":"process_num"}
def get_process_count(host, port, community):
	process_oid = ObjectName('.1.3.6.1.2.1.25.1.6.0')
	process_data = snmp_get(host, port, community, process_oid)
	if isinstance(process_data, bool):
		return False
	return str(process_data[0][1])
