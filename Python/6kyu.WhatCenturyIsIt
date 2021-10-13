# Solutions in Python

# 6kyu - What century is it?

https://www.codewars.com/kata/52fb87703c1351ebd200081f 

# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
# Examples: "1999" --> "20th", "2011" --> "21st", "2154" --> "22nd", "2259" --> "23rd", "1124" --> "12th", "2000" --> "20th"

import math
def what_century(year):
    century = math.ceil(int(year)/100)
    last = century%10
    if last == 1 and century != 11:
        return f"{century}st"
    elif last == 2 and century != 12:
        return f"{century}nd"
    elif last == 3 and century != 13:
        return f"{century}rd"
    else:
        return f"{century}th"
