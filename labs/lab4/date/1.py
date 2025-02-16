import datetime

today = datetime.datetime.now()

new_date = today - datetime.timedelta(days=5)

print(new_date)