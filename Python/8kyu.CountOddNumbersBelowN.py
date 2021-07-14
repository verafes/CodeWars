# Solutions in Python

# 8kyu - Count Odd Numbers below n

https://www.codewars.com/kata/59342039eb450e39970000a6/python

# Given a number n, return the number of positive odd numbers below n, EASY!

# oddCount(7) //=> 3, i.e [1, 3, 5] 
# oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

def odd_count(n):
    if n < 1:
        return 0
    else:
        return n // 2
