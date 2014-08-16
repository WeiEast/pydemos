import imaplib

M = imaplib.IMAP4('imap.163.com')
M.login('pythonld', 'ldldld')
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():  # 保存所有邮件
    typ, data = M.fetch(num, '(RFC822)')
    with open(str(num) + '.eml', 'wb') as f:
        f.write(data[0][1])
    # print('Message %s\n%s\n' % (num, data[0][1]))
M.close()
M.logout()
