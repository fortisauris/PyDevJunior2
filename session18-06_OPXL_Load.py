from openpyxl import load_workbook

wb = load_workbook('format.xlsx')
print(type(wb))
print(dir(wb))
print(id(wb))

print(wb.worksheets)
print(wb.views)

ws2 = wb['PANDAS']
print(ws2['A4'])
print(ws2['A4'].value)
ws2['A4'] = 'Dudince'
print(ws2['A4'].value)

# TODO Prestavka do 19:52

