# Q. Given an array print frequencies(number of times element occurs) of elements.


def frequencies_of_elements(arr):
    # use a hashmap to store the occurences of elements
    hashmap = {}
    for element in arr:
        hashmap[element] = hashmap.get(element, 0) + 1

    for key, value in hashmap.items():
        print(f"{key}: {value}") 


if __name__ == "__main__":
    arr = [10, 20, 20, 30, 15, 10, 2, 10]
    frequencies_of_elements(arr)