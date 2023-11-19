
def max_profit(arr):
    res  = 0
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            res += arr[i] - arr[i-1]
    return res

arr = [1, 5, 3, 8, 12]
print(max_profit(arr))