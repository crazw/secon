#!/usr/bin/env python
#encoding=utf-8

import sys, MySQLdb
import secon_log_lib as log

MYSQL = {
	'CHARSET'	: 'utf8',
	'HOST' 		: '_mysql_host_',
	'PORT' 		: '_mysql_port_',
	'USER' 		: '_mysql_user_',
	'PASS' 		: '_mysql_pass_',
	'DBNAME' 	: '_mysql_dbname_'
}

# get mysql connect
def mysql__connect():
	try:
		return MySQLdb.connect(host=MYSQL['HOST'], user=MYSQL['USER'], passwd=MYSQL['PASS'], db=MYSQL['DBNAME'], charset=MYSQL['CHARSET'])
	except Exception as err:
		raise Exception("Mysql Connect: [%d: %s]" % (err.args[0], err.args[1]))

# query mysql table
def mysql__query(sql, args, res='list'):
	if not sql.strip():
		raise Exception("Input(sql) must no be empty")

	# log.sql(sql, args)

	connect = mysql__connect()
	cursor = connect.cursor()

	try:
		
		affect = cursor.execute(sql, args)
		
		if 0 == affect:
			if 'dict' == res:
				mysql__close(cursor, connect)
				return {}
			elif 'list' == res:
				mysql__close(cursor, connect)
				return []
			else :
				mysql__close(cursor, connect)
				return 0

		label = cursor.description

		if 'dict' == res:
			_dict = {}
			_row = cursor.fetchone()
			for i in range(len(label)):
				_dict[label[i][0]] = _row[i]

			mysql__close(cursor, connect)
			return _dict
		elif 'list' == res:
			_list = []
			_rows = cursor.fetchall()
			for _row in _rows:
				_dict = {}
				for i in range(len(label)):
					_dict[label[i][0]] = _row[i]
				_list.append(_dict)
			
			mysql__close(cursor, connect)
			return _list
		else :
			mysql__close(cursor, connect)
			return affect
	except Exception as error:
		mysql__close(cursor, connect)
		raise Exception("Mysql Query: [%d: %s]" % (error.args[0], error.args[1]))

# update mysql table
def mysql__update(sql, args):
	if not sql.strip():
		raise Exception("input[sql] must no be empty.")

	connect = mysql__connect()
	cursor = connect.cursor()
	
	try:
		
		affect = cursor.execute(sql, args)
		connect.commit()
		mysql__close(cursor, connect)
		return affect
	except Exception as error:
		mysql__close(cursor, connect)
		raise Exception("Mysql Update: [%d: %s]" % (error.args[0], error.args[1]))

# close mysql connect
def mysql__close(cursor, connect) :
	cursor.close()
	connect.close()
