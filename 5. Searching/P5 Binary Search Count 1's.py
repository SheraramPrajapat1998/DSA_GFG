# Q. Given a binary sorted array i.e. array of only 0 and 1's. Count the
# no. of 1's in it.

# Approach: Since array is sorted, all 0's occure first and all 1's
# are in the last. So, find the 1st occurance of 1 the find count by
# substracting it from total length of array.

def binary_search_count_1s(arr, key=1):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key > arr[mid]:
            low = mid + 1
        elif mid == 0 or arr[mid] != arr[mid-1]:
            return mid
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    arr = [0]
    index = binary_search_count_1s(arr)
    print(index, len(arr))
    count = len(arr) - index if index != -1 else 0
    print(count)
