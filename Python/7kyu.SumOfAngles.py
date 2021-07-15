# Solutions in Python

# 7kyu - Sum of angles


# Find the total sum of internal angles (in degrees) in an n-sided simple polygon. 
# N will be greater than 2.

def angle(n):
    return 180 * (n - 2)
