
from typing import List


def binary_search_rotated_sorted_array(arr:List[int], key:int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        print(f"Searching in {low} to {high}")
        mid = low + (high - low) // 2
        if key == arr[mid]:
            return mid
        elif arr[low] < arr[mid]:
            if key >= arr[low] and key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if key >= arr[mid] and key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [100, 500, 10, 20, 30, 40, 50]
    key = 50
    print(binary_search_rotated_sorted_array(arr, key))
