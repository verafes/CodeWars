# Solutions in Python

# 8kyu - Area of an arrow 

https://www.codewars.com/kata/589478160c0f8a40870000bc

# Complete the function that calculates the area of the red square, 
# when the length of the circular arc A is given as the input. 
# Return the result rounded to two decimals.
# Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

def square_area(A):
    from math import pi
    r = (A*4)/(2*pi)
    area = r**2
    return (round(area, 2))
