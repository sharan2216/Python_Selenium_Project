#here only Excel sheet (.xls format)taken for practice--so we have used xlrd package----------------------
import xlrd

workbook=xlrd.open_workbook_xls('C:/Users/shashi/Desktop/XLS.xls')
sheet = workbook.sheet_by_name("Sheet1")

#total no of rows----------
rowcount=sheet.nrows
colcount=sheet.ncols

print(rowcount)
print(colcount)