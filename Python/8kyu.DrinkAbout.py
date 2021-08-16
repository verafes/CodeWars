# Solutions in Python

# 8kyu - Drink about

https://www.codewars.com/kata/56170e844da7c6f647000063 

# Kids drink toddy. Teens drink coke. Young adults drink beer. Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:
# Children under 14 old. Teens under 18 old. Young under 21 old. Adults have 21 or more.

def people_with_age_drink(age):
    if age >= 21: 
        return "drink whisky"
    elif age >= 18:
        return "drink beer"
    elif age >= 14:
        return "drink coke"
    else: 
        return "drink toddy"
