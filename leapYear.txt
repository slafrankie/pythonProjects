#Program accepts input of year and checks if it is a leap year
#If year is divisible by 100 and it meets either %400 or %4 criteria
#And %100, it will be a leap year, if not the program says otherwise

year = int(input("What year is it: "))


if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
    print("Leap year, 366 days")
else:
    print("Not a leap year")
