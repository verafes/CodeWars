# Solutions in Python

# 8kyu - Super Duper Easy 

https://www.codewars.com/kata/55a5bfaa756cfede78000026

# Make a function that returns the value multiplied by 50 and increased by 6. 
# If the value entered is a string it should return "Error".

def problem(a):
    return 'Error' if type(a) is str else a*50+6
