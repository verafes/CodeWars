# Solutions in Python

# 8kyu - Fuel Calculator

https://www.codewars.com/kata/57b58827d2a31c57720012e8

# In this kata you will have to write a function that takes litres and price_per_litre as arguments. 
# Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres 
# get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. 
# But total discount per litre cannot be more than 25 cents. Return the toal cost rounded to 2 decimal places. 
#Also you can guess that there will not be negative or non-numeric inputs.

def fuel_price(litres, price_per_litre):
    if litres < 2:
        price = litres * price_per_litre
    elif litres < 4:
        price = litres * (price_per_litre - 0.05)
    elif litres < 6:
        price = litres * (price_per_litre - 0.1)
    elif litres < 8:
        price = litres * (price_per_litre - 0.15)
    elif litres < 10:
        price = litres * (price_per_litre - 0.2)
    else:
        price = litres * (price_per_litre - 0.25)
    return round(price, 2)

// solution #2:

def fuel_price(litres, price_per_litre):
    return round(litres * (price_per_litre - min((litres // 2) * 0.05, 0.25)), 2)
