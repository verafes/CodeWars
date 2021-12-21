# Solutions in Python

# 7kyu - Cat Years, Dog Years (2)

https://www.codewars.com/kata/5a6d3bd238f80014a2000187

## I have a cat and a dog which I got as kitten / puppy.
# I forget when that was, but I do know their current ages as catYears and dogYears.
# Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]
# NOTES:
# Results are truncated whole numbers of "human" years
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

def owned_cat_and_dog(cat_years, dog_years):
    if cat_years < 15:
        cat = 0
    elif cat_years < 24:
        cat = 1
    else: 
        cat = 2 + ((cat_years - 24)//4)
    if dog_years < 15:
        dog = 0
    elif dog_years < 24:
        dog = 1
    else: 
        dog = 2 + ((dog_years - 24)//5)
    return [cat, dog]
