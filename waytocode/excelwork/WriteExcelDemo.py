import xlsxwriter

book = xlsxwriter.Workbook("Students.xls")

sheet = book.add_worksheet()

row = 0
column = 0

content = ['Name', 'Email', 'Number']


for i in content:
    sheet.write(row, column, i)
    column += 1



content1 = ["Aakash", "aakash@test.com", "7894561230"]
row1 = 1
column1 = 0

for i in content1:
    sheet.write(row1, column1, i)
    column1 += 1

book.close()
