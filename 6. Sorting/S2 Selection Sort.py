from math import inf

# Stability: Unstable

def selection_sort(arr, n):
    temp = []
    for i in range(n):
        min_index = 0
        for j in range(n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp.append(arr[min_index])
        arr[min_index] = inf

    for i in range(n):
        arr[i] = temp[i]

    # TC: O(n^2)
    # Auxilary Space: O(n)


def selection_sort_optimized(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # TC: O(n^2)
    # SC: O(1)


if __name__ == '__main__':
    arr = [20,2, 10, 8, 7]
    selection_sort(arr, len(arr))
    print(arr)