# Solutions in Python

# 7kyu - Calculate Two People's Individual Ages

https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1

# Create a function that takes in the sum and age difference of two people, calculates their individual ages, 
# and returns a pair of values (oldest age first) if those exist or null/None if:
# sum < 0, difference < 0 -> Either of the calculated ages come out to be negative

def get_ages(sum, difference):
    if sum < 0 or difference < 0 or sum < difference:
        return None
    a = (sum + difference)/2
    b = sum - a
    if sum == difference:
        return a, 0
    return a, b
