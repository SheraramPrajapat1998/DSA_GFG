# Q. Find any one peak element in array. A peak element is an element which is not less
# than it's neighbours.

# Approach: use binary search and check if middle element is peak element or not. If
# it's not, then check it's left neighbour if it's less than or equal then one peak
# element must present in the right side of array else check in left side of array.

# NOTE: if left neighbour is less than or equal then atleast one peak element must be
# present in the right side of the array. It doesn't mean that peak element can't be
# present in left side of the array.

def find_peak_element_index(arr):
    n = len(arr)
    if n == 0:
        return -1
    elif n == 1:
        return arr[0]
    elif n == 2:
        if arr[0] > arr[1]:
            return arr[0]
        return arr[1]
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low)//2
        if (
            (arr[mid] == 0 or arr[mid] >= arr[mid - 1]) and
            (arr[mid] == n-1 or arr[mid] >= arr[mid + 1])
        ):
            return mid
        elif mid > 0 and arr[mid] <= arr[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    arr = [5, 10, 20, 15, 7]
    peak_element_index = find_peak_element_index(arr)
    print(
        f'peak_element_index:{peak_element_index}, peak_element: {arr[peak_element_index]}')
