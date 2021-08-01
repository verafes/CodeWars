# Solutions in Python

# 7kyu - Cat and Mouse - Easy Version

https://www.codewars.com/kata/57ee24e17b45eff6d6000164 

# You will be given a string (x) featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'.
# You need to find out if the cat can catch the mouse from it's current position. The cat can jump over three characters. So:
# C.....m returns 'Escaped!' <-- more than three characters between
# C...m returns 'Caught!' <-- as there are three characters between the two, the cat can jump.

def cat_mouse(x):
    c = x.index("C")
    m = x.index("m")
    return 'Caught!' if abs(c-m) <= 4 else 'Escaped!'
	
# Solution 2
def cat_mouse(x):
    return "Escaped!" if len(x) > 5 else "Caught!"


