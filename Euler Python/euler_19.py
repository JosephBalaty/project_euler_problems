# starting from the first day, we increment the current day one at a 
# time, incrementing a counter when a specific condition is met. 

nextDay = {"Monday":"Tuesday", 
        "Tuesday":"Wednesday", 
        "Wednesday":"Thursday", 
        "Thursday": "Friday",
        "Friday":"Saturday",
        "Saturday": "Sunday",
        "Sunday":"Monday"}

nextMonth = {"January":"February", 
             "February":"March", 
             "March":"April", 
             "April":"May", 
             "May":"June", 
             "June":"July", 
             "July":"August", 
             "August":"September", 
             "September":"October", 
             "October":"November",
             "November": "December",
             "December":"January"}
monthDays = {
    "January":31, 
    "February":28, 
    "March":31, 
    "April":30, 
    "May":31, 
    "June":30, 
    "July":31, 
    "August":31, 
    "September":30, 
    "October":31, 
    "November":30,
    "December":31
}

curday = "Monday"
day = 1
month = "January"
year = 1900

sundayCount = 0

def updateFeb(yr):
    monthDays["February"] = 28
    if yr%4 == 0:
        if yr%100 != 0 or yr%400 == 0:
            monthDays["February"] = 29


while year <= 2000:
    if year > 1900 and curday == "Sunday" and day == 1:
        sundayCount += 1
    if day == monthDays[month]:
        day = 1
        month = nextMonth[month]
        curday = nextDay[curday]
        if month == "January":
            year += 1
            updateFeb(year)
    else:
        day += 1
        curday = nextDay[curday]
    
print(sundayCount)