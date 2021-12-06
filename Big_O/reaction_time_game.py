import time
from time import perf_counter as my_timer
import random
input("Press enter to start")
a_val = random.randint(1, 6)
time.sleep(a_val)
start_time = my_timer()
input("Press enter to end")
end_time = my_timer()

print("Start time is:" + time.strftime("%X", time.localtime(start_time)))
print("End time is:" + time.strftime("%X", time.localtime(end_time)))
print(f"Reaction time was {end_time - start_time}")