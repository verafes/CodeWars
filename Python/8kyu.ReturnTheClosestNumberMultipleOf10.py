# Solutions in Python

# 8kyu - Return the closest number multiple of 10 

https://www.codewars.com/kata/58249d08b81f70a2fc0001a4

# Given a number return the closest number to it that is divisible by 10.
# Example input:
# 22
# 25
# 37
# Expected output:
# 20
# 30
# 40
 
def closest_multiple_10(i):
    return round(i / 10) * 10


