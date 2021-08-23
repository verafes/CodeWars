# Solutions in Python

# 8kyu - Get Planet Name By ID

https://www.codewars.com/kata/515e188a311df01cba000003/ 

# The function is not returning the correct values. Can you figure out why?
# get_planet_name(3) # should return 'Earth'

# Given

def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    switch id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

# Solution

def get_planet_name(id):
    name=""
    if id == 1: name = "Mercury"
    if id == 2: name = "Venus"
    if id == 3: name = "Earth"
    if id == 4: name = "Mars"
    if id == 5: name = "Jupiter"
    if id == 6: name = "Saturn"
    if id == 7: name = "Uranus"  
    if id == 8: name = "Neptune"
    return name
