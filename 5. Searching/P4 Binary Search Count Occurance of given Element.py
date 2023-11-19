

def first_occurance(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        elif mid == 0 or arr[mid] != arr[mid - 1]:
            return mid
        else:
            high = mid - 1
    return -1


def last_occurance(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        elif mid == len(arr)-1 or arr[mid] != arr[mid + 1]:
            return mid
        else:
            low = mid + 1
    return -1

def first_and_last_occurance(arr, key):
    first = first_occurance(arr, key)
    if first == -1:
        print("Element not present in array")
        return [-1, -1]
    last = last_occurance(arr, key)
    return [first, last]

if __name__ == '__main__':
    arr = [10, 10, 20, 30, 30, 30, 40, 50, 60, 60, 60]
    key = 00
    first, last = first_and_last_occurance(arr, key)
    count = last - first + 1 if first != -1 else 0
    print(count)