


def pair_sum(arr, sum):
    hashmap = {}
    result = []
    for element in arr:
        if sum - element in hashmap:
            result.append((element, sum - element))
        else:
            hashmap[element] = hashmap.get(element, 0) + 1
    return result
    # TC: O(n)
    # SC: O(n)

if __name__ == '__main__':
    # arr = [3, 2, 8, 15, -8, 17+8]
    arr = [11, 5, 6]
    sum = 10
    print(pair_sum(arr, sum))
        