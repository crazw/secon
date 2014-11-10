#!/usr/bin/env python
#encoding=utf-8

import re, sys, time
import lib.secon_snmp2 as snmp2
import lib.secon_log_lib as log
import lib.secon_util_lib as util
from pysnmp.proto.rfc1902 import ObjectName

#获取每个逻辑分区的计算单位
def get_disk_unit(host, port, community):
	unit_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.4')
	unit_data = snmp2.snmp_info(host, port, community, unit_oid)
	if isinstance(unit_data, bool):
		return False
	return snmp2.change_dict(unit_data)

#获取正在使用的逻辑分区
def get_disk_label(host, port, community):
	label_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.3')
	label_data = snmp2.snmp_info(host, port, community, label_oid)
	if isinstance(label_data, bool):
		return False
	return snmp2.change_dict(label_data)

#获取正在使用的网卡   
def get_network_label(host, port, community):

	id_oid = ObjectName('.1.3.6.1.2.1.2.2.1.8')
	id_data = snmp2.snmp_info(host, port, community, id_oid)
	if isinstance(id_data, bool):
		return False
	id_data = snmp2.change_dict(id_data)

	label_oid = ObjectName('.1.3.6.1.2.1.2.2.1.2')
	label_data = snmp2.snmp_info(host, port, community, label_oid)
	if isinstance(label_data, bool):
		return False
	label_data = snmp2.change_dict(label_data)

	active_eth = {}
	for key in id_data.keys():
		if id_data[key]!='2' and not re.match('lo',label_data[key]):
			active_eth.update({str(key):label_data[key]})
	return active_eth

#==============================================

#获取cpu的使用率
def get_cpu_load(host, port, community):
	cpu_oid = ObjectName('.1.3.6.1.2.1.25.3.3.1.2')
	cpu_data = snmp2.snmp_next(host, port, community, cpu_oid)
	if isinstance(cpu_data, bool):
		return get_cpu_load_old(host, port, community)
	return cpu_data[0][0][1]

def get_cpu_load_old(host, port, community):
	cpu_oid = ObjectName('.1.3.6.1.4.1.2021.11')
	cpu_data = snmp2.snmp_next(host, port, community, cpu_oid)
	if isinstance(cpu_data, bool):
		return False
	return str(int(100) - int(cpu_data[10][0][1]))

#获取正在使用的逻辑分区的使用
#单位kb
def get_disk_used(host, port, community, units=False, labels=False):

	if not units:
		units = get_disk_unit(host, port, community)

	if not labels:
		labels = get_disk_label(host, port, community)

	if False == units or False == labels:
		return False

	use_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.6')
	use_data = snmp2.snmp_info(host, port, community, use_oid)

	if isinstance(use_data, bool):
		return False

	used = snmp2.change_dict(use_data)

	total_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.5')
	total_data = snmp2.snmp_info(host, port, community, total_oid)

	if isinstance(total_data, bool):
		return False

	total = snmp2.change_dict(total_data)

	disk_list = []
	for _id in labels.keys():
		if labels[_id].startswith('/'):
			disk_list.append({
				'disk_id' : int(_id),
				'label' : labels[_id],
				'used': str(int(int(used[_id]) * int(units[_id])) / 1024),
				'total': str(int(int(total[_id]) * int(units[_id])) / 1024)
			})

	return disk_list

# get memory for linux
#memory 内存使用信息，单位单位：Bytes
#user : 已使用内存
#total :总内存
#return {"memory":{"used":"used","total":"total"}}
def get_memory_used(host, port, community, units=False, labels=False):

	memory_oid = ObjectName('.1.3.6.1.4.1.2021.4')
	memory_data = snmp2.snmp_info(host, port, community, memory_oid)
	if isinstance(memory_data, bool):
		return get_memory_used_old(host, port, community, units, labels)
	swap_mem_total = memory_data[2][0][1]
	swap_mem_avail = memory_data[3][0][1]
	real_mem_total = memory_data[4][0][1]
	real_mem_avail = memory_data[5][0][1]
	Buffer = memory_data[8][0][1]
	Cached = memory_data[9][0][1]

	result = {'buffer': str(Buffer), 'cached': str(Cached)}
	result['real_total'] = str(real_mem_total)
	result['real_used'] = str(real_mem_total - real_mem_avail)

	result['swap_total'] = str(swap_mem_total)
	result['swap_used'] = str(swap_mem_total - swap_mem_avail)

	return result

def get_memory_used_old(host, port, community, units, labels):

	if not units:
		units = get_disk_units(host, port, community)

	if not labels:
		labels = get_disk_labels(host, port, community)

	if False == units or False == labels:
		return False

	use_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.6')
	use_data = snmp2.snmp_info(host, port, community, use_oid)

	if isinstance(use_data, bool):
		return False

	used = snmp2.change_dict(use_data)

	total_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.5')
	total_data = snmp2.snmp_info(host, port, community, total_oid)

	if isinstance(total_data, bool):
		return False

	total = snmp2.change_dict(total_data)

	dict_memory = {'swap_used': '0', 'swap_total': '0', \
		'real_total': '0', 'real_used': '0', 'buffer': '0', 'cached': '0'}

	memory_list = []
	for _id in labels.keys():

		if 'Physical memory' == labels[_id]:
			dict_memory['real_used'] = str(long(long(used[_id]) * int(units[_id])) / 1024)
			dict_memory['real_total'] = str(long(long(total[_id]) * int(units[_id])) / 1024)

		elif 'Swap space' == labels[_id]:
			dict_memory['swap_used'] = str(long(long(used[_id]) * int(units[_id])) / 1024)
			dict_memory['swap_total'] = str(long(long(total[_id]) * int(units[_id])) / 1024)

		elif 'Memory buffers' == labels[_id]:
			dict_memory['buffer'] = str(long(long(used[_id]) * int(units[_id])) / 1024)

		elif 'Cached memory' == labels[_id]:
			dict_memory['cached'] = str(long(long(used[_id]) * int(units[_id])) / 1024)

		else:
			pass

	return dict_memory

#获取正在使用的网卡
def get_network_data(host, port, community, _bit):

	if not _bit:
		system_bit = snmp2.get_system_info(host, port, community)
		if False == system_bit:
			return False
		_bit = system_bit['osbit']

	if not _bit:
		return False

	if '64' == _bit:
		in_flow_oid = ObjectName('.1.3.6.1.2.1.31.1.1.1.6')
		out_flow_oid = ObjectName('.1.3.6.1.2.1.31.1.1.1.10')
	else:
		in_flow_oid = ObjectName('.1.3.6.1.2.1.2.2.1.10')
		out_flow_oid = ObjectName('.1.3.6.1.2.1.2.2.1.16')

	in_flow_data = snmp2.snmp_info(host, port, community, in_flow_oid)
	if isinstance(in_flow_data, bool):
		return False

	out_flow_data = snmp2.snmp_info(host, port, community, out_flow_oid)
	if isinstance(out_flow_data, bool):
		return False

	in_flow = snmp2.change_dict(in_flow_data)
	out_flow = snmp2.change_dict(out_flow_data)

	return in_flow, out_flow

def get_network_last(host, port, community, _bit, labels):

	if not labels:
		labels = get_network_label(host, port, community)

	if not labels:
		return False

	in_flow, out_flow = get_network_data(host, port, community, _bit)

	_network = {}
	for _id in labels.keys():
		in_data = long(in_flow[_id]) * 8 / 1024
		out_data = long(out_flow[_id]) * 8 / 1024
		_network[str(_id)] = {'in_data':str(in_data), 'out_data':str(out_data)}
	return _network

def get_network_used(host, port, community, _bit, labels, lastdata):

	if not labels:
		labels = get_network_label(host, port, community)

	if not labels:
		return False

	if not lastdata:
		lastdata = get_network_last(host, port, community, _bit, labels)

	if not lastdata:
		return False

	in_flow, out_flow = get_network_data(host, port, community, _bit)

	networkes = []
	for _id in labels.keys():
		in_data = long(in_flow[_id]) * 8 / 1024
		out_data = long(out_flow[_id]) * 8 / 1024

		in_last = long(lastdata[_id]['in_data'])
		out_last = long(lastdata[_id]['out_data'])
			
		if in_data > in_last and out_data > out_last:
			networkes.append({
				'network_id' : int(_id),
				'label' : labels[_id],
				'in_flow': str(in_data - in_last),
				'out_flow': str(out_data - out_last),
				'in_total': str(in_data),
				'out_total': str(out_data)
			})
		else:
			networkes.append({
				'network_id' : int(_id),
				'label' : labels[_id],
				'in_flow': '0',
				'out_flow': '0',
				'in_total': str(in_data),
				'out_total': str(out_data)
			})
	return networkes
