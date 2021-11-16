# Solutions in Python

# 7kyu - Multiples!

https://www.codewars.com/kata/55a8a36703fe4c45ed00005b 

# Make a program that takes a value (x) and returns "Bang" if the number is divisible by 3, 
# "Boom" if it is divisible by 5, "BangBoom" if it divisible by 3 and 5, and "Miss" if it isn't divisible by any of them. 
# Note: Your program should only return one value
# Ex: Input: 105 --> Output: "BangBoom" Ex: Input: 9 --> Output: "Bang" Ex:Input: 25 --> Output: "Boom"

def multiple(x):
    if x % 3 == 0 and x % 5 != 0:
        return "Bang"
    if x % 3 != 0 and x % 5 == 0:
        return  "Boom"
    if x % 3 == 0 and x % 5 == 0:
        return "BangBoom"
    else: 
        return "Miss"
