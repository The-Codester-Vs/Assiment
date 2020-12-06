import datetime

x = datetime.datetime.now()
date = x.day
month = x.strftime('%b')
year = x.year
day = x.strftime('%A')
print(f"{date} {month} {year} {day}")

if month == "Jan" or month == "Mar" or month ==  "May" or month == "July" or month == "Aug" or month ==  "Oct" or month ==  "Dec":
    print("The number of days left in this month are",31 - date)
        
elif month == "April" or month == "Jun" or month == "Sept" or month == "Nov":
    print("The number of days left in this month are",30 - date)
    
elif month=="Feb":
    print("The number of days left in this month are",28 - date)