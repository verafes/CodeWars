# Solutions in Python

# 8kyu - Area of a Square 

https://www.codewars.com/kata/5748838ce2fab90b86001b1a

#Complete the function that calculates the area of the red square, 
#when the length of the circular arc A is given as the input. 
#Return the result rounded to two decimals.

def square_area(A):
    from math import pi
    r = (A*4)/(2*pi)
    area = r**2
    return (round(area, 2))
