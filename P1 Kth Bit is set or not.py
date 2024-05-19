"""
Q: Given a number n and k, find if kth bit in n is set or not i.e. it's value is 1 or not at kth place.
"""

def is_bit_set(number, bit_position):
    """
    Left shift 1 by position places will give 1 bit set at kth position
    (basically raising to power of 2 by k times). and then and operation with number.
    ----------- OR ---------------
    Right shift number by k-1 position
    """
    # mask = 1 << (bit_position - 1)
    # return (number & mask) == 1

    # -------------- OR -------------
    mask = number >> (bit_position - 1)
    return mask & 1 == 1


if __name__ == '__main__':
    print(is_bit_set(5, 1)) # True
    print(is_bit_set(8, 2)) # False
    print(is_bit_set(0, 3)) # False
