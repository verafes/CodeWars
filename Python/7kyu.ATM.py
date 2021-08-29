# Solutions in Python

# 7kyu - ATM

https://www.codewars.com/kata/5635e7cb49adc7b54500001c  

# There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
# You are given money in nominal value of n with 1<=n<=1500.
# Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

def solve(n):
    count=0
    y = [500,200,100,50,20,10]
    i = 0
    if n % 10 != 0: return -1
    while n > 0:
        count=count + (n//y[i])
        n = int(n%y[i])
        i = i + 1
    return count
