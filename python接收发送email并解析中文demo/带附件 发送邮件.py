from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

mailfrom = 'pythonld@163.com'
mailto = 'lidongone@qq.com'
title = '你好，我是python机器人，正在发送邮件测试'
cc = 'check english'


msg = MIMEMultipart()
att1 = MIMEText(open('1.txt', 'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
#这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="1.txt"'
msg.attach(att1)

msg['to'] = mailto
msg['from'] = mailfrom
msg['subject'] = 'fujian'

smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login('pythonld', 'ldldld')
smtp.sendmail(msg['from'], msg['to'], msg.as_string())
smtp.quit()
