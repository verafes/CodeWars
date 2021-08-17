// Solutions in JavaScript

// 7kyu - Cat Years, Dog Years (2)

https://www.codewars.com/kata/can-we-divide-it

/* Task
I have a cat and a dog which I got as kitten / puppy.
I forget when that was, but I do know their current ages as catYears and dogYears.
Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]

NOTES: 
Results are truncated whole numbers of "human" years

Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that

Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
*/ 

def owned_cat_and_dog(cat_years, dog_years):
    if cat_years < 15:
        ownedCat = 0
    elif cat_years < 24:
        ownedCat = 1
    else:
        ownedCat = (cat_years-24)//4 + 2
    if dog_years < 15:
        ownedDog = 0
    elif dog_years < 24:
        ownedDog = 1
    else:
        ownedDog = (dog_years-24)//5 + 2
    return [ownedCat, ownedDog]
