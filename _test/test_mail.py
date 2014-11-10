#!/usr/bin/env python
#encoding=utf-8

import lib.secon_mail_lib as mail

if __name__ == '__main__' :
	
	mail.sendmail('zcoson@qq.com', 'python mail test', 'Python邮件测试.')
	