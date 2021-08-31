# Solutions in Python

# 8kyu - Leap Years

https://www.codewars.com/kata/526c7363236867513f0005ca 

# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:
# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years

def isLeapYear(year):
    return (year%4 == 0 and not year%100 ==0) or year%400 == 0
