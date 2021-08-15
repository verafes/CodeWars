# Solutions in Python

# 7kyu - Right in the Centre

https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69 

# This is inspired by one of Nick Parlante's exercises on the CodingBat online code practice tool.
# Given a sequence of characters, does "abc" appear in the CENTER of the sequence?
# The sequence of characters could contain more than one "abc".
# To define CENTER, the number of characters in the sequence to the left and right of the "abc" (which is in the middle) must differ by at most one.
# If it is in the CENTER, return True. Otherwise, return False.
# Write a function as the solution for this problem. This kata looks simple, but it might not be easy.
# Example
# is_in_middle("AAabcBB")  ->  True
# is_in_middle("AabcBB")   ->  True
# is_in_middle("AabcBBB")  ->  False

def is_in_middle(sequence):
    return 'abc' in sequence[(len(sequence)-1)//2-1 : (len(sequence)+2)//2+1]
