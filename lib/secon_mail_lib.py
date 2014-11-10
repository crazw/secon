#!/usr/bin/env python
#encoding=utf-8

from config import MAIL
import mimetypes, threading
import lib.secon_log_lib as log

class ThreadMail(threading.Thread):
	def __init__(self, _to, subject, content):
		threading.Thread.__init__(self)
		self._to = _to
		self.subject = subject
		self.content = content

	def run(self):
		sendmail(self._to, self.subject, self.content)


def sendmail(_to, subject, content):
	try:
		from smtplib import SMTP_SSL as SMTP
		from email.mime.text import MIMEText
		from email.mime.image import MIMEImage
		from email.mime.multipart import MIMEMultipart
	except Exception, error:
		log.error("mail_lib.sendmail", "Send mail failed to [%s]: Python not support sendmail" % _to)
		return False

	if not _to:
		raise Exception('[mail.sendmail.to] is None')

	if not subject.strip():
		raise Exception('[mail.sendmail.subject] is None')

	if not content.strip():
		raise Exception('[mail.sendmail.content] is None')

	# if isinstance(_to, str):
	# 	_tos = [_to]
	# else:
	# 	_tos = _to

	try:

		msg = MIMEMultipart()
		msg.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
		msg["Subject"] = subject
		msg["From"] = MAIL['FROM']

		# msg = MIMEText(content, 'plain')
		# msg['Subject']= subject
		# msg['From'] = MAIL['FROM'] # some SMTP servers will do this automatically, not all

		# if filename != None and os.path.exists(filename):
		# 	ctype, encoding = mimetypes.guess_type(filename)
		# 	if ctype is None or encoding is not None:
		# 		ctype = "application/octet-stream"
		# 	maintype, subtype = ctype.split("/", 1)
		# 	attachment = MIMEImage((lambda f: (f.read(), f.close()))(open(filename, "rb"))[0], _subtype = subtype)
		# 	attachment.add_header("Content-Disposition", "attachment", filename=os.path.basename(filename))
		# 	message.attach(attachment)

		conn = SMTP(MAIL['HOST'])
		conn.set_debuglevel(False)
		conn.login(MAIL['USER'], MAIL['PASS'])
		try:
			conn.sendmail(MAIL['FROM'], _to, msg.as_string())
		finally:
			conn.close()

		log.info('mail.sendmail', 'Send mail [%s] success' % _to)

		return True

	except Exception, error:
		raise Exception("Send mail failed to [%s]: %s" % (_to, error))


def sendmail_thread(_to, subject, content):
	
	ThreadMail(_to, subject, content).start()
