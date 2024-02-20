import datetime

today = datetime.datetime.today()
birthday = datetime.datetime(2006, 11, 14)
m = today - birthday
print("Difference : ", {m.total_seconds()})