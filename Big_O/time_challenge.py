import time
# a = time.perf_counter()
# b = time.time()
# c = time.monotonic()
# d = time.process_time()
print(time.get_clock_info("time"))
print(time.get_clock_info("perf_counter"))
print(time.get_clock_info("monotonic"))
print(time.get_clock_info("process_time"))