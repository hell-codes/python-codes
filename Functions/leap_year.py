#Takes year and returns it is leap year or not
def check_leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"
    
print(check_leap_year(2020))
print("The year 2020 is a:", check_leap_year(2020))
print(check_leap_year(1900))
print("The year 1900 is a:", check_leap_year(1900))

    