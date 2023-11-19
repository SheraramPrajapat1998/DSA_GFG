# Q. Given sorted array with duplicate elements in it. Find if an
# element is present in the array then return highest index at which
# element is present else -1.

def binary_search_last_occurance_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        elif mid == len(arr) - 1 or arr[mid] != arr[mid+1]:
            return mid
        else:
            low = mid + 1
    return -1


def binary_search_last_occurance_recursive(arr, low, high, key):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if key < arr[mid]:
        high = mid - 1
        return binary_search_last_occurance_recursive(arr, low, high, key)
    elif key > arr[mid]:
        low = mid + 1
        return binary_search_last_occurance_recursive(arr, low, high, key)
    elif mid == len(arr) - 1 or arr[mid] != arr[mid+1]:
        return mid
    else:
        low = mid + 1
        return binary_search_last_occurance_recursive(arr, low, high, key)

def find_last_occurance(arr, key):
    low = 0
    high = len(arr) - 1
    last_occurance = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid]==key:
            last_occurance = mid
            low = mid + 1
        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
    return last_occurance

if __name__ == '__main__':
    arr = [10, 10, 20, 30, 30, 30, 40, 50, 60, 60]
    key = 60
    # print(binary_search_last_occurance_iterative(arr, key))
    low = 0
    high = len(arr) - 1
    print(find_last_occurance(arr, key))
    print(binary_search_last_occurance_recursive(arr, low, high, key))