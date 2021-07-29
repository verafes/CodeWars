# Solutions in Python

# 7kyu - Exes and Ohs

https://www.codewars.com/kata/55908aad6620c066bc00002a

# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. The string can contain any char.
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    count = 0
    for el in s:
        if el.lower() == "o":
            count += 1
        elif el.lower() == "x":
            count -= 1
    return True if count == 0 else False

# Solution #2
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
