
import poplib
import re

# pop3服务器地址
host = "pop.163.com"
# 用户名
username = "pythonld"
# 密码
password = "ldldld"
# 创建一个pop3对象，这个时候实际上已经连接上服务器了
pp = poplib.POP3(host)
# 设置调试模式，可以看到与服务器的交互信息
pp.set_debuglevel(1)
# 向服务器发送用户名
pp.user(username)
# 向服务器发送密码
pp.pass_(password)
for ii in range(1, len(pp.list()[1]) + 1):
    rsp, msg, siz = pp.retr(ii)
    msg = [i.decode('utf-8')
           for i in msg if i.decode().startswith('Subject')]
    print(msg)
