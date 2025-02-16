from datetime import datetime

date1 = datetime(2025, 2, 16, 10, 35, 45)
date2 = datetime(2025, 2, 14, 12, 45, 30)

diff = date1 - date2

seconds = diff.days * 86400 + diff.seconds

print(seconds)