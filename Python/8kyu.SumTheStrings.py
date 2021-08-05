# Solutions in Python

# 8kyu - Sum The Strings

https://www.codewars.com/kata/5966e33c4e686b508700002d

# Create a function that takes 2 positive integers 
# in form of a string as an input, and outputs the sum (also as a string):
#  sumStr("4", "5")    // should output "9"
#  sumStr("34", "5")   // should output "39"
# If either input is an empty string, consider it as zero.

def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))
