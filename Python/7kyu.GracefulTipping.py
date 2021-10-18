# Solutions in Python

# 7kyu - Graceful Tipping

https://www.codewars.com/kata/5eb27d81077a7400171c6820 

# Adding tip to a restaurant bill in a graceful way can be tricky, thats why you need make a function for it.
# The function will receive the restaurant bill (always a positive number) as an argument. 
# You need to 1) add at least 15% in tip, 2) round that number up to an elegant value and 3) return it.
# What is an elegant number? It depends on the magnitude of the number to be rounded. 
# Numbers below 10 should simply be rounded to whole numbers. Numbers 10 and above should be rounded like this:
# 10 - 99.99... ---> Round to number divisible by 5
# 100 - 999.99... ---> Round to number divisible by 50
# 1000 - 9999.99... ---> Round to number divisible by 500
# Examples
#  1  -->    2
#  7  -->    9
# 12  -->   15
# 86  -->  100

import math
def graceful_tipping(bill):
    bill = math.ceil(bill * 1.15)
    divisible = 5
    n = 100
    if bill < 10: 
        return bill
    while True:
        if bill < n:
            while bill % divisible != 0:
                bill += 1
            return bill
        n = n * 10
        divisible = divisible * 10
