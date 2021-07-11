# Solutions in Python

# 7kyu - Debug the functions EASY 

https://www.codewars.com/kata/5844a422cbd2279a0c000281/ 

# Should be easy, begin by looking at the code. Debug the code and the functions should work.
# There are three functions: Multiplication (x) Addition (+) and Reverse (!esreveR)

def multi(l_st):
    product = 1
    for x in l_st:
        product *= x
    return product
def add(l_st):
    return sum(l_st)
def reverse(string):
    return string[::-1]
