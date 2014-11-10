#!/usr/bin/env python
#encoding=utf-8

import sys

from config import LOG
import lib.secon_util_lib as util

LOG_TYPE = 'WORK'

# =====================================================================
def debug(loc, message):
	if (LOG['ENABLED']) :
		pass
		# print '[DEBUG] [%s] [%s] [%s] - %s' % (util.strdatetime(), LOG_TYPE, loc, message)

# =====================================================================
def info(loc, message):
	if (LOG['ENABLED']) :
		# pass
		print '[INFO ] [%s] [%s] [%s] - %s' % (util.strdatetime(), LOG_TYPE, loc, message)

# =====================================================================
def error(loc, message):
	# pass
	print '[ERROR] [%s] [%s] [%s] - %s' % (util.strdatetime(), LOG_TYPE, loc, message)