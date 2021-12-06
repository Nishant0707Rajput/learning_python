import pytz
import datetime


country = 'Asia/Kolkata'      #-------->We can find other_countries time as now() tells local time
an_obj = pytz.timezone(country)
print(f"The local time in {country} is {datetime.datetime.now(tz=an_obj).strftime('%I-%M-%S:%p')}")
print(f"UTC is {datetime.datetime.utcnow()}")

# for x in pytz.all_timezones:
#     print(x)

# for code in pytz.country_names:
    # print(f"{code}: {pytz.country_names[code]}")

# print(dict(pytz.country_timezones))
# print(dict(pytz.country_names))

for x in pytz.country_names:
    # print(f"{x}: {pytz.country_names[x]}: {pytz.country_timezones.get(x)}")
    if pytz.country_timezones.get(x) is not None:
        for a_var in pytz.country_timezones.get(x):
            val = pytz.timezone(a_var)
            print(f"{pytz.country_names[x]} : {a_var}: {datetime.datetime.now(val)}")
    else:
        print(pytz.country_names[x],": No time zone")
