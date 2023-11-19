
def merge(arr, left, mid, right):
    arr1 = arr[left:mid]
    arr2 = arr[mid:right]
    print("arr1", arr1, "arr2", arr2)
    i = 0
    j = 0
    k = left
    n1 = len(arr1)
    n2 = len(arr2)

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1
    print("arr afrer sort", arr)

def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        print("merge sort1", arr[left: mid])
        merge_sort(arr, left, mid)
        print("merge sort2", arr[mid+1:right])
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

if __name__ == '__main__':
    arr = [10, 5, 30, 15, 7]
    merge_sort(arr, 0, len(arr))
    print(arr)