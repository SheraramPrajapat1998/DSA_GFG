
def max_even_odd(arr):
    # res = 1
    # n = len(arr)
    # for i in range(n):
    #     curr = 1
    #     for j in range(i+1, n):
    #         if ((arr[j] % 2 == 0 and arr[j-1] % 2 != 0) or
    #                 (arr[j] % 2 != 0 and arr[j-1] % 2 == 0)):
    #             curr += 1
    #         else:
    #             break
    #     res = max(res, curr)
    # return res
    # TC: O(n^2)
    # ------------------------ OR ------------------------

    # Kadane's Algorithm
    res = 1
    curr = 1
    n = len(arr)
    for i in range(1, n):
        if ((arr[i] % 2 == 0 and arr[i-1] % 2 != 0) or
                (arr[i] % 2 != 0 and arr[i-1] % 2 == 0)):
            curr += 1
            res = max(res, curr)
        else:
            curr = 1
    return res
    # TC: O(n)


if __name__ == "__main__":
    arr = [5, 10, 20, 6, 3, 8]
    print(max_even_odd(arr))
