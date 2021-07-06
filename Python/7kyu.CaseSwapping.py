# Solutions in Python

# 7kyu - Case swapping

https://www.codewars.com/kata/5590961e6620c0825000008f

# Given a string, swap the case for each of the letters.
# e.g. CodEwArs --> cODeWaRS
# Examples
# ""           ->   ""
# "CodeWars"   ->   "cODEwARS"
# "abc"        ->   "ABC"
# "ABC"        ->   "abc"
# "123235"     ->   "123235"

def swap(string):
    return string.swapcase()
