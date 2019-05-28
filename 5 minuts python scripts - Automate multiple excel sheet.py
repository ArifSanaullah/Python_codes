import xlrd
import os


excelsheet1 = os.path.expanduser("youtubeexcelsheet.xlsx")
excelsheet2 = os.path.expanduser("youtubeexcelsheet2.xlsx")

book_1 = xlrd.open_workbook(excelsheet1)
book_2 = xlrd.open_workbook(excelsheet2)

first_sheet = book_1.sheet_by_index(0)
second_sheet = book_1.sheet_by_index(0)

print(first_sheet.row_values(0))

headings = first_sheet.row_values(0)
column2Heading = headings[7]
print(column2Heading)

i = 0
total = 0
for row in range(first_sheet.nrows):
    if str(first_sheet.cell(row,1).value) == "Key Lime":
        i += 1
        total = total + first_sheet.cell(row,2).value
    else:
        pass
for row in range(second_sheet.nrows):
    if str(second_sheet.cell(row,1).value) == "Key Lime":
        i += 1
        total = total + second_sheet.cell(row,2).value
    else:
        pass

print(i)
print(total)