# Q. Given an array. Find the longest subarray containing equal number of 0's and 1's.

def longest_subarray_containing_equal_zeros_and_ones(arr):
    # efficient solution
    # Approach: Replace each 0 with -1 and then use concept of longest subarray wiht sum zero
    hashmap = {}
    prefix_sum = 0
    target = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
    start, end = 0, 0
    max_subarray_length = 0
    for index, element in enumerate(arr):
        prefix_sum += element
        if prefix_sum - target in hashmap:
            start = hashmap[prefix_sum - target] + 1
            end = index + 1
            if max_subarray_length < end - start:
                max_subarray_length = end - start
        elif prefix_sum == target:
            end = index + 1
            if max_subarray_length < end - start:
                max_subarray_length = end - start
        else:
            hashmap[prefix_sum] = index
    return max_subarray_length

if __name__ == '__main__':
    arr = [1, 0, 1, 1, 1, 0, 0]
    print(longest_subarray_containing_equal_zeros_and_ones(arr))
