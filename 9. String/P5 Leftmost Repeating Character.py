# Given a string. Find the index of the leftmost repeating character else return -1.

# IP: str = "geeksforgeeks"
# OP: 0 -> "g" is the leftmost char that is being repeating.

# IP: str = "abbcc"
# OP: 1

# IP: "abcd"
# OP: -1

import sys


def get_leftmost_repeating(string):
    NUMBER_OF_CHARS = 256
    # count_arr = [0] * NUMBER_OF_CHARS
    # for char in string:
    #     count_arr[ord(char) - ord('a')] += 1

    # for index, char in enumerate(string):
    #     current_value = count_arr[ord(char) - ord('a')]
    #     if current_value > 1:
    #         return index
    # return -1

    # Efficient Approach - 1
    # result = sys.maxsize
    # findex = [-1] * NUMBER_OF_CHARS
    # for idx in range(len(string)):
    #     current_index = ord(string[idx]) - ord('a')
    #     fi = findex[current_index]
    #     if(fi == -1):
    #         findex[current_index] = idx
    #     else:
    #         result = min(result, fi)
    # return -1 if result == sys.maxsize else result

    # Efficient Approach - 2
    # `iterate the string from right side and updated visited boolean array as well as index`
    visited = [False] * NUMBER_OF_CHARS
    result = -1
    for idx in range(string):
        current_index = ord(string[idx])-ord('a')
        if(visited[current_index]):
            result = idx
        else:
            visited[current_index] = True
    return result



if __name__ == "__main__":
    string = "geeksforgeeks"
    string = "abbcc"
    string = "abcd"
    print(get_leftmost_repeating(string))
