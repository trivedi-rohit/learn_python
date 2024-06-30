# Program to check Leap Year:
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"The year {year} a leap year.")
else:
    print(f"The year {year} is not a leap year.")