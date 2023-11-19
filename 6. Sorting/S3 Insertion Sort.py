# TC: O(n^2) Worst case
# O(n) in best case
# Inplace and stable
# used in practice for small array(Timsort(uses Merge sort and Insertion sort)
# and Introsort(Heap sort, quick sort and insertion sort))
# Python uses Timsort to sort the array, i.e. uses Merge sort for large arrays and
# uses insertion sort for small arrays or arrays becomes smaller


def insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key: # condition arr[j] > key will make this sorting stable
            # condition arr[j] >= key will make this sorting unstable
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


