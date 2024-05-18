import math
"""
Q.: Given a number, check if its prime or not.
"""
"""
Sol 1: Naive Method
Check if number is divisible by any number between from 2 to N.
"""
def naive_method(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

"""
Sol 2: Efficient Sol - 1
Idea - Divisors always appears in a pairs.
If (x, y) is a pair
x * y = n
and If x <= y
x*x <= n
x <= sqrt(n)
So, we only need to check til sqrt(n).
"""
def efficient_sol1(number):
    if number == 1:
        return False
    for i in range(2, math.sqrt(number)):
        if number % i == 0:
            return False
    return True

"""
Sol 3: Optimised Sol
Idea - By checking n % 2 == 0 and n % 3 == 0, we can save many iterations for large n.
Optimise Sol 2 with this condition.
Values for i for large n. from above condition we will only need to check:
Here '~' means no need to check as it will divisible by 2 or 3 and has already been checked.
~2, ~3, ~4, 5, ~6, 7, ~8, ~9, ~10,
11, ~12, 13, ~14, ~15, ~16, 17, ~18, 19, ~20,
~21, ~22, 23, ~24, ~25, ~26, 27, ..... sqrt(n)
i.e. 5, 7, 11, 13, 17, 19, 23, 27
from this we get a pattern to check if it's divisible by i or i+2, where i starts from 5 and
step up by 6.
This sol will be almost 3 times faster that sol2.
"""
def optimised_sol(number):
    if number == 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False 
    for i in range(5, math.sqrt(number), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True


def is_prime(number):
    result = False
    if number == 1:
        return False
    
    