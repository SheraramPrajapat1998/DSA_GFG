import math


def digits_in_factorial(number):
    """```number of digits == floor(log10(N)+1)
        Number of digits in the N! = log10(N!)
        N! = (N) x (N-1) x (N-2) x . . . x 3 x 2 x 1
        log10(N!) = log10((N) x (N-1) x (N-2) x . . .  x 2 x 1)
        log10(N!) = log10(N) + log10(N-1) + . . .  + log10(2)+ log10(1)```"""
    res = 0
    for i in range(2, number+1):
        res += math.log10(i)
    return int(math.floor(res)+1)


print(digits_in_factorial(1))
print(digits_in_factorial(3))
print(digits_in_factorial(4))
print(digits_in_factorial(6))
print(digits_in_factorial(10))
