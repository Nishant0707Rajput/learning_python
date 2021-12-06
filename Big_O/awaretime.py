import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print(f"Naive local time {local_time}")
print(f"Naive UTC {utc_time}")

aware_local_time = pytz.utc.localize(local_time)
aware_utc_time = pytz.utc.localize(utc_time)

print(f"Aware local time {local_time.astimezone()}, time zone {aware_local_time.tzinfo}")
print(f"Aware UTC time {aware_utc_time}, time zone {aware_utc_time.tzinfo}")