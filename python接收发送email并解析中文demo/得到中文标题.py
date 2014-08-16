import imaplib
import base64
import re
# a = '=?gb18030?B?y+21wLeiyfq1xA==?='
# print(base64.b64decode(a).decode('gb18030'))
M = imaplib.IMAP4('imap.163.com')
M.login('pythonld', 'ldldld')
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    aa = data[0][1].decode()
    aa = re.search('Subject: (.*?)\n', aa).group(1)
    if aa.startswith('=?gb'):
        aa = aa.split('?')[-2]
        print(base64.b64decode(aa).decode('gb18030'), '\n')
    else:
        print(aa)


M.close()
M.logout()
