import time

print(time.gmtime(0))
print(time.localtime())
print(time.time())

time_val_now = time.localtime()
print("Year:", time_val_now.tm_year, "or", time_val_now[0])
print("Month", time_val_now.tm_mon, "or", time_val_now[1])
print("Day", time_val_now.tm_mday, "or", time_val_now[2])

