#Current Date,Year,Month,Day,Time:-
import datetime as dt
Today_date=dt.date.today()
current_datetime=dt.datetime.now()
Day_name=current_datetime.strftime("%A")
Exact_time=current_datetime.strftime("%I%p")
print("Today_date with all y,m,d:",Today_date)
print("current date year:",Today_date.year)
print("current date month:",Today_date.month)
print("Today date:",Today_date.day)
print("Current datetime:",current_datetime)
print("Day_name:",Day_name)
print(Exact_time)

