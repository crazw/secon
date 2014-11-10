#!/usr/bin/env python
#encoding=utf-8

import sys, time, requests
import simplejson as json
import lib.secon_log_lib as log
import lib.secon_util_lib as util

def get(url):
	try :
		resp = requests.get(url)
		return resp.text
	except EOFError, err:
		log.error('httpclient.get', str(err))
		return False

def get_as_json(url):
	content = get(url)
	if False == content :
		return {}
	else:
		return util.strtojson(content)

def post(url, _data):
	try :
		resp = requests.post(url, data=_data)
		return resp.text
	except EOFError, err:
		log.error('httpclient.post', str(err))
		return False

def post_as_json(url, _data):
	content = post(url, _data)
	if False == content :
		return {}
	else:
		return util.strtojson(content)

def request (url, pdata) :
	try :
		resp = requests.post(url, data=pdata)
		obj = json.loads(resp.text)
		if 0 == obj.get('status'):
			log.error('httpclient.request', obj.get('message'))
			return False
		log.info('httpclient', '%s %s' % (url, obj.get('status')))
		return obj.get('data')
	except EOFError, err:
		log.error('httpclient.request', str(err))
		return False
