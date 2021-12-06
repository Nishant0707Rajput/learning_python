# import time
# print(f"The epoch event starts from {time.strftime('%c',time.gmtime(0))}")
# print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")
# if time.daylight:
#     print("Daylight saving time is in effect for this location.")
#     print(f"The DST timezone is {time.timezone[1]}")
# print(f"Local time is {time.strftime('%d-%m-%Y %H-%M-%S',time.localtime())}")
# print(f"UTC time is {time.strftime('%d-%m-%Y %H-%M-%S',time.gmtime())}")
import datetime
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())