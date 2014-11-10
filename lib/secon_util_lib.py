#!/usr/bin/env python
#encoding=utf-8

import time, datetime
from config import DATE

try:
	import simplejson as json
except:
	import json

try:
	from hashlib import md5 as md5lib
except:
	from md5 import md5 as md5lib

def md5(key):
	_md = md5lib()
	_md.update(key)
	return _md.hexdigest()


def longtime(_time = ''):
	if _time:
		return long(time.mktime(time.strptime(_time, DATE['PATTERN'])))
	else:
		return long(time.time())


def strdatetime(_time = 0):
	if 0 == _time:
		return datetime.datetime.now().strftime(DATE['PATTERN'])
	else:
		return datetime.datetime.fromtimestamp(_time).strftime(DATE['PATTERN'])


def strdate(_time = 0):
	if 0 == _time:
		return datetime.datetime.now().strftime(DATE['DATEPAT'])
	else:
		return datetime.datetime.fromtimestamp(_time).strftime(DATE['DATEPAT'])


def addtime_second(second = 10):
	if 0 < second:
		cur_date = datetime.datetime.now() + datetime.timedelta(seconds=abs(second))
	elif 0 > second:
		cur_date = datetime.datetime.now() - datetime.timedelta(seconds=abs(second))
	else:
		cur_date = datetime.datetime.now()

	return cur_date.strftime(DATE['PATTERN'])


def addtime_day(day = 10):
	if 0 < day:
		cur_date = datetime.datetime.now() + datetime.timedelta(days=abs(day))
	elif 0 > day:
		cur_date = datetime.datetime.now() - datetime.timedelta(days=abs(day))
	else:
		cur_date = datetime.datetime.now()

	return cur_date.strftime(DATE['PATTERN'])



# ================ json begin ================

def objtostr(_obj):
	return json.dumps(_obj)

def strtojson(_str):
	return json.loads(_str)

# ================ json end ==================



# ================ dns begin ================

def qid_by_qname(qname):
	_dict = { 'A':1, 'MX':15, 'NS':2, 'TXT':16, 'CNAME':5 }
	return _dict[qname]


def qname_by_qid(qid):
	_dict = { '1':'A', '15':'MX', '2':'NS', '16':'TXT', '5':'CNAME' }
	return _dict[qid]

# ================ dns end ==================

def file_read(file_path):
	try:
		_input = open(file_path)
		if not _input:
			return '{}'
		_string = _input.read()
		_input.close()
		return _string
	except Exception, e:
		return '{}'

def file_write(file_path, content):
	try:
		_output = open(file_path, 'w')
		_output.write(content)
		_output.close() 
	except Exception, e:
		pass
