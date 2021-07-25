# Solutions in Python

# 7kyu - Formatting decimal places #1 

https://www.codewars.com/kata/5641c3f809bf31f008000042

# Each floating-point number should be formatted that only the first two decimal places are returned. 
# You don't need to check whether the input is a valid number because only valid numbers are used in the tests.
# Don't round the numbers! Just cut them after two decimal places!

def two_decimal_places(number):
    return int(number*100)/100
