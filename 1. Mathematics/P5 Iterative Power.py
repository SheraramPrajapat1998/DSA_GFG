"""
Q.: Given a number and value, return number raised to power value.
i.e. x = 3, n = 4, return value of 3*3*3*3
"""
"""
Sol 1: Naive Method
Multiply n times
"""
def naive_method(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


"""
Sol 2: Efficient Sol - 1
Idea - Every number can be written as sum of powers of 2 i.e. binary number.
x = 3
10: 1010 -> 8 + 2 -> pow(3, 8) * pow(3, 2)
9: 0101 -> 8 + 1 -> pow(3, 8) * pow(3, 1)
Iterate through each bit and then multiply all results.
"""
def efficient_sol1(x, n):
    result = 1
    while n:
        if n & 1:
            result *= x
        x *= x
        n /= 2
    return result


def power(x, n):
    """
    Return x raise to power n
    """
    return naive_method(x, n)
    # return efficient_sol1(x, n)


if __name__ == '__main__':
    value = power(x=5, n=3)
    print(value)
