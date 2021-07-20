# Solutions in Python

# 7kyu - [Code Golf] Return Odd No Matter What

https://www.codewars.com/kata/5f882dcc272e7a00287743f5 

# Given the integer n return odd numbers as they are, but subtract 1 from even numbers.
# Note: Your solution should be 36 or less characters long.
# Examples
# Input  = 2, Output = 1
# Input  = 13, Output = 13
# Input  = 46, Output = 45

def always_odd(n): return n-(n+1)%2
