#task1
from datetime import date, timedelta

current_date = date.today()  
new_date = current_date - timedelta(days=5)  

print("Current Date:", current_date)
print("Date 5 Days Ago:", new_date)
#task2
from datetime import date , timedelta
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Today: " ,  today)
print("Yesterday: " , yesterday)
print("Tomorrow: " , tomorrow)
#task3
from datetime import datetime
now = datetime.now()
no_microsec = now.replace(microsecond=0)
print(no_microsec)
#task4
from datetime import datetime
date1 = datetime(2024 , 5 , 1 , 12 , 0 , 0)
date2 = datetime(2025 , 6 , 18 , 5 , 6 , 0)
diff = abs((date2 - date1).total_seconds())
print(diff)