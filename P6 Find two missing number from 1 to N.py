"""
Q: Given an array of n number that has values in range [1, ... n+1]. Every no. appears exactly once.
Hence, one number is missing. Find the missing no.

Q 2.: Another variant of this question. Given a range of number and a number is missing in it. Same logic.
"""

def find_missing_numbers(arr):
    """
    Idea: XOR of a number with itself is zero and XOR of zero and number is number itself. So Find XOR of
    all number from 1 to N and then XOR that result with each number in array. You will get missing number.
    Time Complexity: Θ(N)
    """
    xor = 0
    for num in arr:
        xor ^= num
    # now result is xor of two odd occuring numbers.
    print(xor)
    right_most_set_bit = xor & ~(xor - 1)
    print(right_most_set_bit)
    missing_num1, missing_num2 = 0, 0
    for number in arr:
        if (number & right_most_set_bit):
            missing_num1 ^= number
        else:
            missing_num2 ^= number
        print(number & right_most_set_bit, missing_num1, missing_num2)
    return missing_num1, missing_num2


if __name__ == '__main__':
    arr = [3, 4, 3, 4, 5, 4, 4, 6, 7, 7]
    print(find_missing_numbers(arr)) # (5, 6)
    arr = [3, 4, 3, 4, 8, 4, 4, 32, 7, 7] # (8, 32)
    print(find_missing_numbers(arr)) 
