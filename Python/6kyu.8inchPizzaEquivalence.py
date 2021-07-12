# Solutions in Python

# 6kyu - 8 inch pizza equivalence

https://www.codewars.com/kata/599bb194b7a047b04d000077

# How much bigger is a 16-inch pizza compared to an 8-inch pizza? 
# A more pragmatic question is: How many 8-inch pizzas "fit" in a 16-incher?

# The answer, as it turns out, is exactly four 8-inch pizzas. 
# For sizes that don't correspond to a round number of 8-inchers, you must round the number of slices 
# (one 8-inch pizza = 8 slices), e.g.:
# how_many_pizzas(16) -> "pizzas: 4, slices: 0"
# how_many_pizzas(12) -> "pizzas: 2, slices: 2"
# how_many_pizzas(8) -> "pizzas: 1, slices: 0"
# how_many_pizzas(6) -> "pizzas: 0, slices: 4"
# how_many_pizzas(0) -> "pizzas: 0, slices: 0"

n = int(input("Please enter the diameter of the pizza: "))

def how_many_pizzas(n):
  import math
  area = math.pi * (n/2)**2
  area8 = math.pi * 4**2
  if n <= 0:
    return 0
  else: 
    pizzas = math.floor(area//area8)
    over_slices = round((area/8)%(area8/8))
	slices = math.floor(over_slices/(area8/8))
    return (f"pizzas: {pizzas}, slices: {slices}")
