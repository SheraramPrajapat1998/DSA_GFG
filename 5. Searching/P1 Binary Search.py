# Given a sorted array. Check if element is present or not if its
# present return it's index else -1.

# Naive solution: For each element check if it's equal to given element.
def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def binary_search_recursive(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        high = mid - 1
        return binary_search_recursive(arr, low, high, key)
    else:
        low = mid + 1
        return binary_search_recursive(arr, low, high, key)


if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60, 70]
    key = 20
    print(binary_search_recursive(arr, 0, len(arr)-1, key))
    # print(binary_search_iterative(arr, key))
