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
Idea - Every number can be written as sum of odd + even.
power(x, n) = {
    if n % 2 == 0: power(x, n/2) * power(x, n/2)
    else: power(x, n-1) * x
}
"""
def efficient_sol1(x, n):
    """
    Time Complexity: Θ(logN)
    Space Complexity: Θ(logN)
    """
    if n == 0:
        return 1
    temp = efficient_sol1(x, n/2)
    temp = temp * temp
    if n & 1 == 0: return temp
    return temp * x


def power(x, n):
    """
    Return x raise to power n
    """
    return naive_method(x, n)
    # return efficient_sol1(x, n)


if __name__ == '__main__':
    value = power(x=5, n=3)
    print(value)
