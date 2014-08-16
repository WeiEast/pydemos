import xlsxwriter

# http://xlsxwriter.readthedocs.org/
# 
# 新建一个文件路径和文件名，然后新建一个工作表.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# 设置A到B列的宽度为20.
worksheet.set_column('A:B', 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)
'''
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1



write_string()
write_number()
write_blank()
write_formula()
write_datetime()
write_boolean()
write_url()
worksheet.write_string  (row, col,     item              )
worksheet.write_datetime(row, col + 1, date, date_format )
worksheet.write_number  (row, col + 2, cost, money_format)
'''
# Insert an image.
# worksheet.insert_image('B5', 'logo.png')

workbook.close()