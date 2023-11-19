
from typing import List
# Q. Given an array arr[] of N non-negative integers representing the height of
# blocks. If width of each block is 1, compute how much water can be trapped
# between the blocks during the rainy season.

# Keep track of left max and right max

def get_water(arr: List):
    # res = 0
    # for i in range(1, len(arr)):
    #     lmax = arr[i]
    #     for j in range(i):
    #         lmax = max(lmax, arr[j])
    #     rmax = arr[i]
    #     for j in range(i+1, len(arr)):
    #         rmax = max(rmax, arr[j])
    #     res += min(lmax, rmax) - arr[i]
    # return res
    # TC: O(n^2)
    # ---------------- OR --------------------------------

    n = len(arr)
    res = 0
    lmax = [0]*n
    rmax = [0]*n
    lmax[0] = arr[0]
    rmax[-1] = arr[-1]

    for i in range(1, n):
        lmax[i] = max(lmax[i-1], arr[i])

    for i in range(n-2, -1, -1):
        rmax[i] = max(rmax[i+1], arr[i])

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(n):
        res += min(rmax[i], lmax[i]) - arr[i]
    return res
    # TC: O(n)
    # SC: O(n)

if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(get_water(arr))
