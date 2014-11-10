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
	unit_data = snmp2.snmp_next(host, port, community, unit_oid)
	if isinstance(unit_data, bool):
		return False
	return snmp2.change_dict(unit_data)

#获取正在使用的逻辑分区
def get_disk_label(host, port, community):
	disk_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.3')
	disk_data = snmp2.snmp_next(host, port, community, disk_oid)
	if isinstance(disk_data, bool):
		return False
	return snmp2.change_dict(disk_data)

#获取正在使用的网卡   
def get_network_label(host, port, community):
	status_oid = ObjectName('.1.3.6.1.2.1.2.2.1.8')
	status_data = snmp2.snmp_next(host, port, community,status_oid)
	if isinstance(status_data, bool):
		return False
	status_data = snmp2.change_dict(status_data)

	label_oid = ObjectName('.1.3.6.1.2.1.2.2.1.2')
	label_data = snmp2.snmp_next(host, port, community, label_oid)
	if isinstance(label_data, bool):
		return False
	label_data = snmp2.change_dict(label_data)

	active_eth={}
	for key in status_data:
		if status_data[key]!='2':
			_lable = label_data[key].lower()
			if 'ms' in _lable or 'loopback' in _lable\
				or 'wan' in _lable or 'microsoft' in _lable:
				pass
			else:
				result_eth={key:label_data[key]}
				active_eth.update(result_eth)
	return active_eth

#==============================================

def get_cpu_load(host, port, community):
	
	cpu_oid = ObjectName('1.3.6.1.2.1.25.3.3.1.2')
	cpu_data = snmp2.snmp_get(host, port, community,cpu_oid)
	if isinstance(cpu_data, bool):
		return False

	j=k=0
	for i in cpu_data:
		j=float(i[0][1])+j
		k=k+1
	
	load = 0

	if k>0:
		avg_load=float(j/k)
		if avg_load > 0:
			load=float(avg_load/100)
	
	if 1 > load:
		load = 1

	return str(load)

def get_disk_used(host, port, community, units=False, labels=False):

	if not units:
		units = get_disk_unit(host, port, community)

	if not labels:
		labels = get_disk_label(host, port, community)

	used_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.6')
	total_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.5')
	
	used_data = snmp2.snmp_next(host, port, community, used_oid)
	total_data = snmp2.snmp_next(host, port, community, total_oid)
	
	used_data = snmp2.change_dict(used_data)
	total_data = snmp2.change_dict(total_data)
	
	disk_list = []
	for idx in labels.keys():
		if labels[idx] != "Virtual Memory" and labels[idx] != "Physical Memory":
			par_name = str(labels[idx])[0:2]
			_used = int(units[idx]) * int(used_data[idx])
			_total = int(units[idx]) * int(total_data[idx])

			disk_list.append({
				'disk_id': idx,
				'label': par_name,
				'used': str(int(_used) / 1024),
				'total': str(int(_total) / 1024)
			})
		
	return disk_list

def get_memory_used(host, port, community, units=False, labels=False):

	if not units:
		units = get_disk_unit(host, port, community)

	if not labels:
		labels = get_disk_label(host, port, community)

	used_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.6')
	total_oid = ObjectName('.1.3.6.1.2.1.25.2.3.1.5')
	
	used_data = snmp2.snmp_next(host, port, community, used_oid)
	total_data = snmp2.snmp_next(host, port, community, total_oid)
	
	used_data = snmp2.change_dict(used_data)
	total_data = snmp2.change_dict(total_data)

	virtalmem_used = 0
	virtalmem_total = 0
	physicalmem_used = 0
	physicalmem_total = 0

	for idx in labels.keys():
		if 'Virtual Memory' == labels[idx]:
			virtalmem_used = int(units[idx]) * long(used_data[idx])
			virtalmem_total = int(units[idx]) * long(total_data[idx])
		elif 'Physical Memory' == labels[idx]:
			physicalmem_used = int(units[idx]) * long(used_data[idx]) 
			physicalmem_total = int(units[idx]) * long(total_data[idx]) 
			
	result = {'buffer': '0', 'cached': '0'}
	result['real_total'] = str(physicalmem_total)
	result['real_used'] = str(physicalmem_used)
	result['swap_total'] = str(virtalmem_total)
	result['swap_used'] = str(virtalmem_used)
	return result

# =============================================================

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

		if 0 < in_last or 0 < in_last:
			if in_data > in_last and out_data:
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
