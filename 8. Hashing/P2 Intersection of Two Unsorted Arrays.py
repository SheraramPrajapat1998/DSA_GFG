# Q. given

def find_intersection_of_arr(arr1, arr2):
    hashmap = {}
    for element in arr1:
        hashmap[element] = hashmap.get(element, 0) + 1

    count = 0
    for element in arr2:
        if element in hashmap and hashmap[element]:
            del hashmap[element]
            count += 1
    return count

if __name__ == "__main__":
    arr1 = [10, 15, 20, 15, 30, 30, 5]
    arr2 = [30, 5, 30, 80]
    # arr1 = [10, 10, 10]
    # arr2 = [10, 10, 10]

    print(find_intersection_of_arr(arr1, arr2))