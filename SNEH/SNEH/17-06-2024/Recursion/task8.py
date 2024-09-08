# Implement a function that checks if a given year is a leap year.


def leap_year(year):

    if (year%400==0) or (year%4==0 and year%100!=0):
        return ("leap year")
        
    else:
        return ("not leap year")
    
year=int(input("enter a year:"))

call=leap_year(year)

print(call)