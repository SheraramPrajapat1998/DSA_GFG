"""
Q: Given an array containing numbers such that exactly one number occurs odd times and rest occurs even times.
"""

def naive_sol(arr):
    """
    Iterate through all numbers and check if their count is any of one is odd.
    Time Complexity: O(N^2)
    """
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]: count += 1
        if count & 1: return arr[i]
    return -1



def optimised_sol(arr):
    """
    Idea: XOR of a number with itself is zero and XOR of zero and number is number itself.
    Time Complexity: Θ(N)
    """
    result = 0
    for num in arr:
        result ^= num
    return result


def find_odd(arr):
    # return naive_sol(arr)
    return optimised_sol(arr)


if __name__ == '__main__':
    arr = [1, 2, 5, 4, 5, 2, 1, 5, 2, 4, 2]
    print(find_odd(arr)) 
