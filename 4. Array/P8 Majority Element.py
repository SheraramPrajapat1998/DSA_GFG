
def find_majority_element(arr):
    # Moore's Voting Algorithm
    res = 0
    count = 1
    n = len(arr)

    # find a candidate
    for i in range(n):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1

    # check if the candidate is actually a majority element.
    count = 0
    for i in range(n):
        if arr[res] == arr[i]:
            count += 1
    if count <= n//2:
        return -1
    return res
