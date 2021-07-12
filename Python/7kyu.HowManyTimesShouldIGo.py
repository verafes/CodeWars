# Solutions in Python

# 7kyu - How many times should I go? 

https://www.codewars.com/kata/57efcb78e77282f4790003d8

# Lot of museum allow you to be a member, 
# for a certain amount amount_by_year you can have unlimitted acces to the museum.
# In this kata you should complete a function in order to know after 
# how many visit it will be better to take an annual pass. 
# The function take 2 arguments annual_price and individual_price.
# Test.describe('Basic Tests')
# Test.assert_equals(how_many_times(40,15), 3)
# Test.assert_equals(how_many_times(30,10), 3)
# Test.assert_equals(how_many_times(80,15), 6)

import math
def how_many_times(annual_price, individual_price):
    return math.ceil(annual_price/individual_price)
	

# Solution #2
def how_many_times(annual_price, individual_price):
    count = int(annual_price / individual_price)
    return count if annual_price % individual_price == 0 else count + 1
