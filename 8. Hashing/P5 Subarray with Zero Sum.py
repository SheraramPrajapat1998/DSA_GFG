# Q. Given an array find it's subarray whose sum is zero

def subarray_with_zero_sum(arr):
    hashmap = {}
    prefix_sum = 0
    result = []
    for index, element in enumerate(arr):
        prefix_sum += element
        if prefix_sum in hashmap:
            start = hashmap[prefix_sum] + 1
            end = index + 1
            result.append(arr[start : end])
        elif prefix_sum == 0:
            start = 0
            end = index+1
            result.append(arr[start : end])
        else:
            hashmap[prefix_sum] = index
    return result


if __name__ == '__main__':
    arr = [2, 1, 4, 13, -3, -10, 5]
    print(subarray_with_zero_sum(arr))