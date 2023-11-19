# Q. Given an array find the longest subarray whose sum is equal to the given sum.



def find_longest_subarray_with_given_sum(arr, target):
    hashmap = {}
    prefix_sum = 0
    largest_subarray_size = 0
    for index, element in enumerate(arr):
        prefix_sum += element
        if prefix_sum - target in hashmap:
            start = hashmap[prefix_sum-target] + 1
            end = index + 1
            if end-start > largest_subarray_size:
                largest_subarray_size = end - start
            print(arr[start:end])
        elif prefix_sum == target:
            start = 0
            end = index + 1
            if end-start > largest_subarray_size:
                largest_subarray_size = end - start
            print(arr[start:end])
        else:
            hashmap[prefix_sum] = index

    return largest_subarray_size

    # Brute Force Approach
    # result = []
    # start, end, current_sum = 0, 0, 0
    # for i in range(len(arr)):
    #     current_sum = arr[i]
    #     start = i
    #     for j in range(i+1, len(arr)):
    #         current_sum += arr[j]
    #         if current_sum == target:
    #             end = j
    #             result.append(arr[start: end+1])
    # return result



if __name__ == '__main__':
    arr = [5, 8, -4, -4, -2, 2, 9]
    sum = 5
    print(find_longest_subarray_with_given_sum(arr, sum))