# python3
import urllib.request
import lxml.html
import re

url = 'http://em.scnu.edu.cn/article/xueyuantongzhi/zonghe/'
html = urllib.request.urlopen(url)
scode=html.read().decode('utf-8')

doc = lxml.html.document_fromstring(scode)
ss = doc.xpath("""//div[@class="c_news"]/ul/li/a/font/text()|//div[@class="c_news"]/ul/li/a/text()""")
bb = doc.xpath("""//div[@class="c_news"]/ul/li/span/text()""")

aa= list(zip(ss,bb))

print(aa)