import calendar

# cal= calendar.month(2022,8)
# print(cal)

# cal= calendar.prcal(2022,4)

# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime(2022,8,22))
# print(datetime.datetime(2022,8,22,12,45,00))

import time
print(time.time())
print(time.localtime())
print(time.asctime(time.localtime(time.time())))
for i in range(1,6):
    print(i,end=" ")
    time.sleep(2)