# Q. Given sorted array with duplicate elements in it. Find if an
# element is present in the array then return lowest index at which
# element is present else -1.

def binary_search_first_occurance(arr, low, high, key):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if key < arr[mid]:
        high = mid - 1
        return binary_search_first_occurance(arr, low, high, key)
    elif key > arr[mid]:
        low = mid + 1
        return binary_search_first_occurance(arr, low, high, key)
    elif mid == 0 or arr[mid] != arr[mid-1]:
        return mid
    else:
        high = mid - 1
        return binary_search_first_occurance(arr, low, high, key)


def binary_search_first_occurance_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        elif mid == 0 or arr[mid] != arr[mid-1]:
            return mid
        else:
            high = mid - 1
    return -1

def find_first_occurance(arr, key):
    low = 0
    high = len(arr) - 1
    first_occurance = -1
    while low <= high:
        mid = low + (high - low) // 2
        if key == arr[mid]:
            first_occurance = mid
            high = mid - 1
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
    return first_occurance

if __name__ == '__main__':
    arr = [10, 10, 20, 30, 30, 30, 40, 50, 60]
    key = 30
    # print(find_first_occurance(arr, key))
    # print(binary_search_first_occurance(arr, 0, len(arr)-1, key))
    print(binary_search_first_occurance_iterative(arr, key))
