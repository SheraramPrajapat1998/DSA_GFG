#


def count_inversions(arr):
    n = len(arr)
    res = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if(arr[i] > arr[j]):
                res += 1
    return res