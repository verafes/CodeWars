# Solutions in Python

# 7kyu - Discover The Original Price

https://www.codewars.com/kata/552564a82142d701f5001228

# We need to write some code to return the original price of a product, 
# the return type must be of type decimal and the number must be rounded to two decimal places.
# We will be given the sale price (discounted price), 
# and the sale percentage, our job is to figure out the original price.

def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / (1 - sale_percentage/100), 2)
