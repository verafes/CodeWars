# Solutions in Python

# 8kyu - Beginner Series #2 Clock

https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make 'Past' function which returns time converted to milliseconds.

# Example:
# past(0, 1, 1) == 61000
# Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59

h = int(input("Enter h: "))
m = int(input("Enter m: "))
s = int(input("Enter s: "))
def past(h,m,s):
  if 0 <= h <= 23 and  0 <= m <= 59 and 0 <= s <= 59:
    return (h * 3600000 + m * 60000 + s * 1000)
  else: 
    return 0
print(f"Given '{h}' hours, '{m}' minutes and 'S' seconds after midnight")  
print("Total milliseconds = ", past(h,m,s))
