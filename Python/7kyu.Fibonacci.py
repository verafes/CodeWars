# Solutions in Python

# 7kyu - Fibonacci

https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af

# Create function fib that returns n'th element of Fibonacci sequence (classic programming task).

# Solution 1

    arr = [0,1]
    
    for i in range(2,n+1): 
        arr.append(arr[i-1] + arr[i-2])

    return arr[n]


# Solution 2

a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
