# Solve the problem from the second set here
#problem 1 (6)

def leap_or_not(year): #the function just verify if its a leap year or nah
    if year%100==0:
        if year%400==0:
           return True
        else:
            return False
    else:
        if year%4==0:
           return True
        else:
           return False
def leap(a,months): # the function just put the number of days corespondent to month february
    if a:
        months[1] = 29  # if its a leap year the month feb will have 29 days
    else:
        months[1] = 28
def result(year,day,months,months_names):
    for i in range(0,12):
        if(day-months[i])<=0:   #if we cant substract anymore than that means that our day is in that month
            print(year, " ", months_names[i], " ", day)
            break
        else:
            day = day - months[i]
def function():
    year=int(input())
    day=int(input())
    months=[31,0,31,30,31,30,31,31,30,31,30,31]
    months_names=["January","February","March","April","May","June","July","August","September","October","November","December"]
    bisect=bool(leap_or_not(year))
    leap(bisect,months)
    result(year, day, months, months_names)
function()