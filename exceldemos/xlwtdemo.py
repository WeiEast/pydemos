import xlwt
import re


wbk = xlwt.Workbook()

sheet1 = wbk.add_sheet('sheet 1')

sheet1.write(0,1,'test text')
# 修改内容警告解决方式：使用cell_overwrite_ok=True来创建worksheet:
# sheet2 =  wbk.add_sheet('sheet 2', cell_overwrite_ok=True)
wbk.save('test.xls')