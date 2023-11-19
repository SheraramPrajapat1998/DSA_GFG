def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    k = 0
    temp = [0 for i in range(len(arr1)+len(arr2))]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            temp[k] = arr1[i]
            i += 1
        else:
            temp[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        temp[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        temp[k] = arr2[j]
        j += 1
        k += 1
    return temp
    # TC: Θ(m+n) where m and n are size of arrays respectively.

arr1 = [10, 15, 20]
arr2 = [5, 6, 6, 15]
# print(merge_sorted_arrays(arr1, arr2))


def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    left = [arr[low+i] for i in range(n1)]
    right = [arr[mid+i+1] for i in range(n2)]

    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    return arr
    # TC: Θ(n)
    # Auxilary Space: Θ(n)

print(merge([10, 20, 40, 20, 30], 0, 2, 4))

