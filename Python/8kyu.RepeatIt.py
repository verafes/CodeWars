# Solutions in Python

# 8kyu - RepeatIt

https://www.codewars.com/kata/557af9418895e44de7000053

# Create a function that takes a string and an integer (n).
# The function should return a string that repeats the input string n number of times.
# If anything other than a string is passed in you should return "Not a string"

def repeat_it(string,n):
    return string*n if type(string) is str else 'Not a string'
