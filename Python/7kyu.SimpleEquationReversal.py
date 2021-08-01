# Solutions in Python

# 7kyu - Simple equation reversal

https://www.codewars.com/kata/5aa3af22ba1bb5209f000037

# Given a mathematical equation that has *,+,-,/, reverse it as follows:
#For example: solve("100*b/y") = "y/b*100"
#solve("a+b-c/d*30") = "30*d/c-b+a"

def solve(eq):
    arr = list(eq.replace("*"," * ").replace("/"," / ").replace("-"," - ").replace("+"," + ").split(" "))
    return "".join(arr[::-1])
