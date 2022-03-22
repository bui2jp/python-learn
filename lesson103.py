import os
import datetime
import shutil

now = datetime.datetime.now()
print(now)
print(now.isoformat)
print(now.strftime('%d-%m-%Y %H:%M:%S'))

today = datetime.date.today()
print(today)


t = datetime.time(hour=1, minute=10, second=5, microsecond=123)
print(t)
print(t.isoformat())
print(t.strftime('%d-%m-%Y %H:%M:%S'))

print(now)
d = datetime.timedelta(weeks=1)
print(d)
print(now - d)

import time
print('####')
print(time.time())
time.sleep(5)
print('####')
print(time.time())

# backup
file_name='test.txt'
if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y%m%d%H%M%S')
    ))
