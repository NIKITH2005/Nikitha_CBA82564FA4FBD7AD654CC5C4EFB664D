# user enters the year
year = int(input ("Enter year:"))

# leap year check
if year % 4 == 0 and year % 100 != 0:
   print(year, "is a leap year")
elif year % 100 == 0:
   print(year, "is not a leap year")
elif year % 400 ==0:
  print(year, "is a leap year")
else:
  print(year, "is not a leap year")