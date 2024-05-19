"""
Q: Given a number n, Check if it's power of 2 or not.
"""

def naive_sol(number):
    """
    Keep dividing number by 2 until it becomes zero.
    Time Complexity: Θ(Total Bits in N)
    """
    if number == 0: return False
    while number:
        if number % 2 == 1: return False
        n >>= 1
    return True


def optimised_sol(number):
    """
    Idea: If it's power of 2 then it'll have only 1 bit set. So it's `and` operation with (number - 1) should result in 0.
    Time Complexity: Θ(1)
    """
    return number != 0 and ((number & (number - 1)) == 0)


def is_power_of_two(number):
    # return naive_sol(number=number)
    return optimised_sol(number=number)


if __name__ == '__main__':
    print(is_power_of_two(5)) # False
    print(is_power_of_two(7)) # False
    print(is_power_of_two(13)) # False
    print(is_power_of_two(16)) # True
