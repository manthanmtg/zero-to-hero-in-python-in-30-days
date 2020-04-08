year = 2020
if year%400 == 0 :
        print("The given year is leap year")
elif year%100 == 0:
    print("The given year is not a leap year")
elif year%4 == 0:
    print("The given year is a leap year")
else:
    print("The given year is not a leap year")
