# NOTE: Bubble sort is Stable Algo.

def bubble_sort(arr, n):
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# since the last i elements is always going to be sorted for after ith iteration
# there is no need to check them
def bubble_sort_efficient(arr, n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# In case array is already sorted or becomes sorted in between
# while comparing adjacent elements if any pair is out of order means swap did
# happened and array is sorted so no need to check for the rest of the elements.
def bubble_sort_optimized(arr, n):
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break


if __name__ == "__main__":
    arr = [20, 2, 10, 8, 7]
    bubble_sort(arr, len(arr))
    print(arr)