#!/usr/bin/env python
#encoding=utf-8

from config import CONFIG
import lib.secon_log_lib as log
import lib.secon_mysql_lib as mysql

def job_ping_list(limit, size):
	try:
		sql = "SELECT 'ping' as category, c.label as glabel,e.node_name,e.node_label,"
		sql += "a.user_id, a.group_id, a.domain_id, a.domain, a.label as dlabel, a.enabled,"
		sql += "b.ping_id as sub_id, b.memo, b.timeout"

		sql += " FROM domain_basic AS a"
		sql += " INNER JOIN ping_basic AS b ON a.domain_id = b.domain_id"
		sql += " INNER JOIN domain_group AS c ON a.group_id = c.group_id"
		sql += " INNER JOIN user_node AS d ON a.user_id = d.user_id"
		sql += " INNER JOIN node_basic AS e ON d.node_id = e.node_id"

		sql += " WHERE a.`enabled`=%s AND b.`enabled`=%s AND e.node_name=%s"
		sql += " ORDER BY b.ping_id ASC limit %s,%s"
		
		args = ['Y','Y', CONFIG['NAME'], ((limit - 1) * size), size]
		_ping_list = mysql.mysql__query(sql, args)
		
		# log.info('model_job.job_ping_list', '[%s] %s' % (len(_ping_list), (sql % tuple(args))))
		# log.debug('model_job.job_ping_list', '[%s] %s' % (len(_ping_list), (sql % tuple(args))))

		return _ping_list
	except Exception, e:
		raise Exception("[model_job.job_ping_list] except: [%s]" % str(e))

def job_dns_list(limit, size):
	try:
		sql = "SELECT 'dns' as category, c.label as glabel,e.node_name,e.node_label,"
		sql += "a.user_id, a.group_id, a.domain_id, a.domain, a.label as dlabel, a.enabled,"
		sql += "b.dns_id as sub_id, b.qtype, b.qvalue, b.timeout"

		sql += " FROM domain_basic AS a"
		sql += " INNER JOIN dns_basic AS b ON a.domain_id = b.domain_id"
		sql += " INNER JOIN domain_group AS c ON a.group_id = c.group_id"
		sql += " INNER JOIN user_node AS d ON a.user_id = d.user_id"
		sql += " INNER JOIN node_basic AS e ON d.node_id = e.node_id"

		sql += " WHERE a.`enabled`=%s AND b.`enabled`=%s AND e.node_name=%s"
		sql += " ORDER BY b.dns_id ASC limit %s,%s"

		args = ['Y','Y', CONFIG['NAME'], ((limit - 1) * size), size]
		_dns_list = mysql.mysql__query(sql, args)

		log.debug('model_job.job_dns_list', '[%s] %s' % (len(_dns_list), (sql % tuple(args))))

		return _dns_list
	except Exception, e:
		raise Exception("[model_job.job_dns_list] except: [%s]" % str(e))

def job_http_list(limit, size):
	try:
		sql = "SELECT 'http' as category, c.label as glabel,e.node_name,e.node_label,"
		sql += "a.user_id, a.group_id, a.domain_id, a.domain, a.label as dlabel, a.enabled,"
		sql += "b.http_id as sub_id, b.protocol, b.`port`, b.path, b.avail_hc, b.memo, b.timeout"

		sql += " FROM domain_basic AS a"
		sql += " INNER JOIN http_basic AS b ON a.domain_id = b.domain_id"
		sql += " INNER JOIN domain_group AS c ON a.group_id = c.group_id"
		sql += " INNER JOIN user_node AS d ON a.user_id = d.user_id"
		sql += " INNER JOIN node_basic AS e ON d.node_id = e.node_id"

		sql += " WHERE a.`enabled`=%s AND b.`enabled`=%s AND e.node_name=%s"
		sql += " ORDER BY b.http_id ASC limit %s,%s"

		args = ['Y','Y', CONFIG['NAME'], ((limit - 1) * size), size]
		_http_list = mysql.mysql__query(sql, args)

		log.debug('model_job.job_http_list', '[%s] %s' % (len(_http_list), (sql % tuple(args))))

		return _http_list
	except Exception, e:
		raise Exception("[model_job.job_http_list] except: [%s]" % str(e))

def job_port_list(limit, size):
	try:
		sql = "SELECT 'port' as category, c.label as glabel,e.node_name,e.node_label,"
		sql += "a.user_id, a.group_id, a.domain_id, a.domain, a.label as dlabel, a.enabled,"
		sql += "b.port_id as sub_id, b.`port`, b.memo, b.timeout"

		sql += " FROM host_basic AS a"
		sql += " INNER JOIN port_basic AS b ON a.domain_id = b.domain_id"
		sql += " INNER JOIN host_group AS c ON a.group_id = c.group_id"
		sql += " INNER JOIN user_node AS d ON a.user_id = d.user_id"
		sql += " INNER JOIN node_basic AS e ON d.node_id = e.node_id"

		sql += " WHERE a.`enabled`=%s AND b.`enabled`=%s AND e.node_name=%s"
		sql += " ORDER BY b.port_id ASC limit %s,%s"

		args = ['Y','Y', CONFIG['NAME'], ((limit - 1) * size), size]
		_port_list = mysql.mysql__query(sql, args)

		log.debug('model_job.job_port_list', '[%s] %s' % (len(_port_list), (sql % tuple(args))))

		return _port_list
	except Exception, e:
		raise Exception("[model_job.job_port_list] except: [%s]" % str(e))

def job_host_list(category, limit, size):
	try:
		sql = "SELECT b.category, c.label as glabel,e.node_name,e.node_label,"
		sql += "a.user_id, a.group_id, a.domain_id, a.domain, a.snmp_port, a.community, a.ostype , a.label as dlabel, a.enabled,"
		sql += "a.purge,b.item_id as sub_id, b.timeout"

		sql += " FROM host_basic AS a"
		sql += " INNER JOIN host_item AS b ON a.domain_id = b.domain_id"
		sql += " INNER JOIN host_group AS c ON a.group_id = c.group_id"
		sql += " INNER JOIN user_node AS d ON a.user_id = d.user_id"
		sql += " INNER JOIN node_basic AS e ON d.node_id = e.node_id"

		sql += " WHERE a.`enabled`=%s AND b.`enabled`=%s AND b.category=%s AND e.node_name=%s"
		sql += " ORDER BY b.item_id ASC limit %s,%s"

		args = ['Y','Y', category, CONFIG['NAME'], ((limit - 1) * size), size]
		_host_list = mysql.mysql__query(sql, args)

		log.debug('model_job.job_host_list', '[%s:%s] %s' % (category, len(_host_list), (sql % tuple(args))))

		return _host_list
	except Exception, e:
		raise Exception("[model_job.job_host_list] except: [%s]" % str(e))