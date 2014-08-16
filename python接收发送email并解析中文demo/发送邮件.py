
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mailfrom = 'pythonld@163.com'
mailto = 'lidongone@qq.com'
title = '你好，我是python机器人，正在发送邮件测试'
cc = 'check english'


msg = MIMEText(cc)
msg['Subject'] = Header(title, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login('pythonld', 'ldldld')
smtp.sendmail(mailfrom, mailto, msg.as_string())
smtp.quit()
