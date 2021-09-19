# Solutions in Python

# 8kyu - Simple calculator

https://www.codewars.com/kata/5810085c533d69f4980001cf/ 

# You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.
# if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
# Example:
# calculator(1, 2, '+') => 3
# calculator(1, 2, '$') # result will be "unknown value"

def calculator(x,y,op):
    if type(x) is int and type(y) is int:
        if op == '-':
            return x-y
        if op == '+':
            return x+y
        if op == '*':
            return x*y
        if op == '/':
            return x/y
        else: 
            return "unknown value"
    return "unknown value"

# Solution 2

def calculator(x,y,op):
    if str(op) not in '+-/*' or not str(x).isnumeric() or not str(y).isnumeric():
        return 'unknown value'
    return x + y if op == '+' else x - y if op == '-' else x * y if op == '*' else x / y
