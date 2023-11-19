
def find_max_subarray_sum(arr):
    # res = arr[0]
    # for i in range(len(arr)):
    #     curr = 0
    #     for j in range(i, len(arr)):
    #         curr += arr[j]
    #         res = max(res, curr)
    # return res
    # TC: O(n^2)
    # SC: O(1)
    # ------------------- OR --------------------------------

    res = arr[0]
    max_ending = arr[0]
    for i in range(1, len(arr)):
        max_ending = max(max_ending + arr[i], arr[i])
        res = max(res, max_ending)
    return res
    # TC: O(n)


if __name__ == '__main__':
    arr = [2, 3, -8, 7, -1, 2, 3]  # 11
    # arr = [5, 8, 3] # 16
    # arr = [-6, -1, -8] # -1
    print(find_max_subarray_sum(arr))
