# Working with date and time

from datetime import datetime

now = datetime.now()

print(now.strftime("%Y"))   # year, e.g. 2026
print(now.strftime("%m"))   # month, e.g. 05
print(now.strftime("%d"))   # day
print(now.strftime("%H"))   # hour (00-23)
print(now.strftime("%M"))   # minute

print(now.strftime("%Y-%m-%d %H:%M"))   # 2026-05-10 14:30
print(now.strftime("%y-%m-%d %H:%M"))   # two-digit year: 26-05-10 14:30
print(now.strftime("%Y-%b-%d %H:%M"))   # %b short month name: 2026-May-10 14:30
