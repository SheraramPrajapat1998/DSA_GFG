# Q. Given an array find it's subarray whose sum is equal to given sum 

def subarray_with_given_sum(arr, target):
    hashmap = {}
    pre_sum = 0
    result = []
    for index, element in enumerate(arr):
        pre_sum += element
        if pre_sum - target in hashmap:
            start = hashmap[pre_sum-target] + 1
            end = index + 1
            result.append(arr[start:end])
        elif pre_sum == target:
            start = 0
            end = index + 1
            result.append(arr[start:end])
        else:
            hashmap[pre_sum] = index
    print(hashmap)
    return result

    # Window sliding technique
    # i, j, current_sum = 0, 0, 0
    # n = len(arr)
    # result = []
    # while j < n:
    #     current_sum += arr[j]
    #     if current_sum < target:
    #         j += 1
    #     elif current_sum == target:
    #         result.append((i, j+1))
    #         j += 1
    #     else:
    #         while current_sum > target:
    #             current_sum -= arr[i]
    #             i += 1
    #         j += 1
    # return result

if __name__ == "__main__":
    arr = [5, 8, 6, 13, 3, -1, 1]
    sum = 22
    print(f"subarrays with sum={sum} start and end index are:", subarray_with_given_sum(arr, sum))
