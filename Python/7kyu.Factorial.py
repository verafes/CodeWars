# Solutions in Python

# 7kyu - Factorial

https://www.codewars.com/kata/57a049e253ba33ac5e000212

# Your task is to write function factorial
# https://en.wikipedia.org/wiki/Factorial

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i  
    return res
