"""
Q: Given an array of n number that has values in range [1, ... n+1]. Every no. appears exactly once.
Hence, one number is missing. Find the missing no.

Q 2.: Another variant of this question. Given a range of number and a number is missing in it. Same logic.
"""

def find_missing_number(arr):
    """
    Idea: XOR of a number with itself is zero and XOR of zero and number is number itself. So Find XOR of
    all number from 1 to N and then XOR that result with each number in array. You will get missing number.
    Time Complexity: Θ(N)
    """
    result = 0
    for num in range(1, len(arr)+2):
        result ^= num
    for num in arr:
        result ^= num
    return result


if __name__ == '__main__':
    arr = [1, 2, 5, 4]
    print(find_missing_number(arr)) 
