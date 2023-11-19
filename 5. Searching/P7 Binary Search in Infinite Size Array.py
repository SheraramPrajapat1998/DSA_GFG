# Q. Given an infinite size array, return index of element if its
# present in it else -1.

# NOTE: Infinite size array is not possible so generally on coding
# platforms, they put millions of elements and give the searching
# element as left as possible.

# Sol: Keep multiplying the current_index by 2 so that we can get a
# range in which we need to search the element. This is also known as
# unbounded binary search

def binary_search(arr, key, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def search(arr, key):
    if arr[0] == key:
        return 0
    current_index = 1
    while arr[current_index] < key:
        current_index *= 2
    if key == arr[current_index]:
        return current_index
    low = current_index // 2 + 1
    high = current_index - 1
    return binary_search(arr, key, low, high)
    # TC: O(log(2*pos)) i.e. O(log(pos))  # pos -> position or index of key


if __name__ == "__main__":
    arr = [1, 10, 15, 20, 30, 60, 90, 100, 200, 400, 425, 800, 900, 1000, 1100, 1200, 1310,
           1400, 1500, 1800, 1810, 1811, 1812, 1900, 2000, 3000, 4000, 5000, 7000, 8000, 9000, 11111]
    key = 400
    print(search(arr, key))
