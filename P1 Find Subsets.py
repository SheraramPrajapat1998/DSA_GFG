
def subsets_of_arr(arr):
    temp = []
    res = []
    subsets = helper(0, arr, temp, res)
    print(subsets)

def helper(index, arr, temp, res):
    if index == len(arr):
        res.append(temp.copy())
        return
    helper(index+1, arr, temp, res)
    temp.append(arr[index])
    helper(index+1, arr, temp, res)
    temp.pop()
    return res

# arr = [5, 7, 8]
arr = [10, 20, 30, 50]
subsets_of_arr(arr)


def subsets_of_arr_using_bit_manipulation(arr):
    res = []
    n = len(arr)
    for i in range(1 << n): # check for bit
        temp = []
        for j in range(n):
            if (i & 1 << j) != 0 :
                temp.append(arr[j])

        res.append(temp)

    return res
print(subsets_of_arr_using_bit_manipulation(arr))
