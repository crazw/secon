#!/usr/bin/env python
#encoding=utf-8

import httplib2, urllib
import simplejson as json
import lib.secon_log_lib as log
import lib.secon_util_lib as util

def get(url):
	try :
		http = httplib2.Http()
		resp, content = http.request(url, "GET")
		return content
	except EOFError, err:
		log.error('httpclient.get', str(err))
		return False

def get_as_json(url):
	content = get(url)
	if False == content :
		return {}
	else:
		return util.strtojson(content)

def post(url, data):
	try :
		http = httplib2.Http()
		resp, content = http.request(url, "POST", body=data)
		return content
	except EOFError, err:
		log.error('httpclient.post', str(err))
		return False

def post_as_json(url, _data):
	content = post(url, _data)
	if False == content :
		return {}
	else:
		return util.strtojson(content)
