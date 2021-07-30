# Solutions in Python

# 7kyu - Greet Me

https://www.codewars.com/kata/535474308bb336c9980006f2

# Write a method that takes one argument as name and then greets that name, capitalized 
# and ends with an exclamation point.
# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"

def greet(name): 
    return f"Hello {name.title()}!"
