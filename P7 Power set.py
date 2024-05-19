import math
"""
Q: Given a string, print the power set of that string.
Power set is a set of all possible combinations of strings, but the order will of characters in string will be same.
Total elements in set: 2^N
Ex: string: 'abc' -> total elements: power(2, 3) = 8
PowerSet: {'', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'}
"""

def find_power_set(string):
    power_set = set()
    n = len(string)
    power_set_size = int(math.pow(2, n))
    for counter in range(power_set_size):
        sub_string = ''
        for j in range(n):
            if counter & (1 << j) != 0:
                sub_string += string[j]
        power_set.add(sub_string)
    return power_set


if __name__ == '__main__':
    string = 'abc'
    print(find_power_set(string))
