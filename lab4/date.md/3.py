import datetime

today = datetime.datetime.today()
s = today.replace(microsecond=0)
print(today)
print(s)
