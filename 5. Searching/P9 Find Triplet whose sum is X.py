

def find_triplet(arr, target):
    arr.sort()
    hashmap = {}
    result = []
    n = len(arr)
    # for ele in arr:
    #     hashmap[ele] = hashmap.get(ele, 0) + 1

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         temp = arr[i] + arr[j]
    #         if target - temp in hashmap:
    #             result.append((arr[i], arr[j], target-temp))
    # return result

    for i in range(len(arr)):
        low = 0
        high = len(arr) - 1
        while low <= high:
            print(i, low, high)
            temp_sum = arr[low] + arr[high] + arr[i]
            if target == temp_sum:
                result.append((arr[i], arr[low], arr[high]))
                i += 1
            elif temp_sum < target:
                low += 1
            else:
                high -= 1
    return result

if __name__ == "__main__":
    arr = [2, 3, 4, 8, 9, 20, 40]
    target = 32
    print(find_triplet(arr, target))
