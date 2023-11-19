# Q. Given two arrays return number of elements after union


def union(arr1, arr2):
    hashmap = {}
    for element in arr1:
        hashmap[element] = hashmap.get(element, 0) + 1
    for element in arr2:
        hashmap[element] = hashmap.get(element, 0) + 1
    
    return len(hashmap)


if __name__ == '__main__':
    arr1 = [10, 20, 30, 10, 5]
    arr2 = [5, 10, 20, 1]
    print(union(arr1, arr2))