

from sys import maxsize


def max_subarray_sum(arr):
    n = len(arr)
    max_ending_here = 0
    max_so_far = -maxsize - 1
    start = end = s = 0
    for i in range(n):
        max_ending_here += arr[i]
        # max_so_far = max(max_ending_here, max_so_far)
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))
    return max_so_far


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_subarray_sum(arr))
