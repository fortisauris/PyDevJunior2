from PyQt6.QtCore import *

now = QDate.currentDate()
print(now)
print(type(now))
print(dir(now))

print(now.toString(Qt.DateFormat.ISODate))  # 2022-12-19
print(now.toString(Qt.DateFormat.RFC2822Date))  # 19 dec 2022

print(now.toJulianDay())

datum = QDate(2045, 12, 19)
print(datum)
print(datum.toString(Qt.DateFormat.RFC2822Date))

now = QDateTime.currentDateTime()
print(now)
print(now.toString(Qt.DateFormat.ISODate))
print(now.toString(Qt.DateFormat.RFC2822Date))

now_UTC = now.toUTC()
print(now_UTC)
print(now_UTC.toString(Qt.DateFormat.ISODate))
print(now_UTC.toString(Qt.DateFormat.RFC2822Date))

print(now.offsetFromUtc())

d = QDate(1989, 11, 17)
print(d.daysInMonth())
print(d.daysInYear())
now = QDate.currentDate()
kolkodni = d.daysTo(now)
print(kolkodni)
# DOKONCIT V PONDELOK

print(now.addDays(11).toString(Qt.DateFormat.RFC2822Date))

t = QDateTime(2022,11,12,6,23)
t.addSecs(3600)
print(t.toString(Qt.DateFormat.RFC2822Date))

pydate = t.toPyDateTime()
print(pydate)
print(type(pydate))

datestring = '15.12.2022'
d = QDate().fromString(datestring, 'dd.MM.yyyy')
print(d)