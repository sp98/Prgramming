import datetime

now = datetime.datetime.now()
print(now)
print(now.date())
print(now.time())
print(now.second)
print(now.microsecond)

bday = now.replace(year=1990, day=8, month=9, hour=10)
how_much_I_lived = now - bday
print("I've lived " + str(how_much_I_lived.days) + " days till now!")
print("I've been living for last " + str(datetime.timedelta(days=(now-bday).days).total_seconds()) + " seconds.")


print(datetime.timedelta(hours=3))
print(datetime.timedelta(days=3))
print(now)
print(now + datetime.timedelta(days=3, hours=4, minutes=4, seconds=4, microseconds=4))

print("I've been living for last " + str(datetime.timedelta(days=(now-bday).days).total_seconds()) + " seconds.")


#strftime

print(now.strftime('%B %dx'))