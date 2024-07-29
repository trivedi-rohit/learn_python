# Find number of days (using function):
def leap_year (year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:   
            return True
    else:
        return False
def result(year,month):
    list1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month == 2:
        return 29
    else:
        return list1[month-1]
year = int(input("Enter the year : "))
month = int(input("Enter month (in numbers) : "))
days = result(year, month)
print(days)