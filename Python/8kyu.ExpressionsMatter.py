# Solutions in Python

# 8kyu - Expressions Matter

https://www.codewars.com/kata/5ae62fcf252e66d44d00008e

# Given three integers a ,b ,c, return the largest number obtained after inserting 
# the following operators and brackets: +, *, () 
# In other words , try every combination of a,b,c with [*+()], 
# and return the Maximum Obtained

# !!! Notes
# The numbers are always positive. 
# The numbers are in the range (1 ≤ a, b, c ≤ 10).
# You can use the same operation more than once.
# It's not necessary to place all the signs and brackets.
# Repetition in numbers may occur.
# You cannot swap the operands. For instance, 
# in the given example you cannot get expression (1 + 3) * 2 = 8.

def expressionsMatter(a,b,c):
  # for i in range(1,10):
  # for i in range(1,10):
    if a <= 0 or b<= 0 or c <= 0:
      return ("Error. Value of a, b, c should be greater than zero")
    else:
      n1 = a * (b + c) 
      n2 = a * b * c
      n3 = a + b * c
      n4 = (a + b) * c
      n5 = a + b + c
      n6 = a * b + c
    return(max(n1, n2, n3, n4, n5, n6))
