#here only Excel sheet(.xlsx format) taken for practice--so we have used openpyxl package----------------------
import openpyxl

from openpyxl import workbook
workbook = openpyxl.load_workbook("C:/Users/shashi/Desktop/ExcelSheet.xlsx")
sheet = workbook.sheetnames
print(sheet)
print(workbook.active.title)
sh1=workbook['Login']
data=sh1['B2'].value
print(data)
