# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how you work out whether if a particular year is a leap year.
    # on every year that is evenly divisible by 4
    # **except** every year that is evenly divisible by 100
    # **unless** the year is also evenly divisible by 400
year = int(input("Which year do you want to check? "))

leap_year = year % 4
leap_year400 = year % 400
leap_year100 = year % 100
if leap_year == 0:
  if leap_year400 == 0:
    print("leap year")
  elif leap_year100 == 0:
    print("not leap year")
  else:
    print("leap year")
else:
  print("not leap year")
 
