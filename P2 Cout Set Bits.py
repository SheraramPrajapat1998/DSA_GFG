"""
Q: Given a number n, count set bits, i.e. number of bits whose value is 1.
"""

def naive_sol(number):
    """
    Iterate through each bit and check if its set or not.
    Time Complexity: Θ(Total Bits in N)
    """
    count = 0
    while number:
        count += 1 if number & 1 else 0
        number >>= 1
    return count


def brian_kernigam_sol(number):
    """
    Idea: and operation of number and (number - 1) will set off the last/lease signicant bit.
    Time Complexity: Θ(Set Bit Count)
    """
    count = 0
    while number:
        number &= (number - 1)
        count += 1
    return count


def count_set_bits(number):
    # return naive_sol(number=number)
    return brian_kernigam_sol(number=number)


if __name__ == '__main__':
    print(count_set_bits(5)) # 2
    print(count_set_bits(7)) # 3
    print(count_set_bits(13)) # 3
