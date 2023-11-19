# Given two strings. Check if they are anagram for each other or not ?
# Two strings are anagram if their number of occura

def are_anagrams(string1, string2):
    # Naive method: sort both the string and check if they are equal.
    # size1 = len(string1)
    # size2 = len(string2)
    # if size1 != size2:
    #     return False

    # string1.sort()
    # string2.sort()
    # return string1 == string2
    # TC: O(nlogn)

    # -----------------------------------------------------------------------------
    # Efficient Sol
    NUMBER_OF_CHARS = 256
    count_arr = [0] * NUMBER_OF_CHARS
    for char in string1:
        count_arr[ord(char) - ord('a')] += 1

    for char in string2:
        count_arr[ord(char) - ord('a')] -= 1

    for num in count_arr:
        if num != 0:
            return False
    return True


if __name__ == '__main__':
    string1 = "listen"
    string2 = "silent"
    print(are_anagrams(string1, string2))
