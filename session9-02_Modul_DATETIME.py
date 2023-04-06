
'''
MODUL DATETIME
'''
import datetime
import zoneinfo
# import tzdata  # toto nam neslo nainstalovat !!!



d1 = datetime.date(year=2023, month=1, day=1)  # specialny objekt, ktory obsahuje datum
print(d1)
print(type(d1))
print(dir(d1))
print(d1.year)
print(d1.timetuple())
print(d1.toordinal())   #
print(d1.weekday())  # anglicka
print(d1.isoweekday())  # nase
print(d1.isocalendar())
print(d1.isoformat())
print(d1.ctime())

d2 = datetime.date(year=1989, month=11, day=17)
print(d2.toordinal())
print(d2.ctime())
print('STRF: ', d2.strftime("%A %d.%B %Y %z"))  # vie to skonvertovat datum podla nasej sablonu

d_final = d1-d2
print(type(d_final))  # timedelta - objekt v ktorom uchovavame casovy usek.
print(d_final)

t1 = datetime.time(11,2,30,0)  # objekt datetime.time
print(type(t1))
print(t1)

#zone = zoneinfo.ZoneInfo('')
# zone = zoneinfo.ZoneInfo('Europe/Bratislava')
cet = datetime.timedelta(hours=1)  # Central European Time
tz = datetime.timezone(offset=cet)
dt = datetime.datetime(year=2023, month=4, day=3, hour=18, minute=31, second=15, microsecond=0, tzinfo=tz)
print(dt)

dt2 = datetime.datetime(year=2022, month=3, day=1, hour=12, minute=31, second=15, microsecond=0, tzinfo=tz)
print(dt2)

d_final = dt-dt2
print('', d_final)
print(type(d_final))
print(d_final.total_seconds())

print(zoneinfo.available_timezones())


dn = datetime.datetime.now()
print(dn)

zajtra = datetime.datetime.now() + datetime.timedelta(hours=24)
print(zajtra)

# TODO vytvorte dva datetime.datetime objekty a potom ich zratajte alebo odratajte

dt = datetime.timedelta(hours=1) + datetime.timedelta(minutes=60)
print(dt)

