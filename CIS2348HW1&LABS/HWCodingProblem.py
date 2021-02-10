#Ali Rajgarah 1586471

from datetime import date

currentMonth = int(input("Enter the current month:\n"))
print("Month:" , (currentMonth))
currentDay = int(input("Enter the current day: \n"))
print("Day: " , (currentDay))
currentYear = int(input("Enter the current year: \n"))
print("Year:" , (currentYear))

d1 = date(year=currentYear, month=currentMonth, day=currentDay)

birthdayMonth = int(input("Enter your birthday month: \n"))
print("Month:" , (birthdayMonth))
birthdayDay = int(input("Enter your birthday day: \n"))
print("Day:" , (birthdayDay))
birthdayYear = int(input("Enter your birthday year: \n"))
print("Year:" , (birthdayYear))

d2 = date(year=birthdayYear, month=birthdayMonth, day=birthdayDay)

d3 = (d1.year-d2.year)
d4 = (d1.month-d2.month)
d5 = (d1.month and d1.day)
d6 = (d2.month and d2.day)

if (d5 == d6):
    print ("Happy Birthday!")

print("You are",d3, "years and",d4, "months old")

