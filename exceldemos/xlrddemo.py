import xlrd
import re


wb = xlrd.open_workbook('1.xls') # 打开文件

sh = wb.sheet_by_name('考试成绩')


sh=wb.sheet_by_index(0)#第一个表

sheetNames = wb.sheet_names() # 查看包含的工作表

# 获得工作表的两种方法
sh = wb.sheet_by_index(0)
sh = wb.sheet_by_name(u'Sheet1')

# 单元格的值
cellA1 = sh.cell(0,0)
cellA1Value = cellA1.value



# 第一列的值
columnValueList = sh.col_values(0) 