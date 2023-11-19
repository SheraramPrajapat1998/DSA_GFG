

def check_ispallindrome(string):
    # check ith index from start and last are same or not
    # n = len(string)
    # for i in range(n//2):
    #     if string[i] != string[n-i-1]:
    #         return False
    # return True
    # TC: O(n) / Ω(1) -> we compare atmost one char i.e. starting and last if these are not same then Ω(1) else O(n) 


    # using reversed function -> returns an iterator
    # rev = "".join(reversed(string))
    # if rev == string:
    #     return True
    # return False

    return string == string[::-1]


if __name__ == '__main__':
    string = "ABCD1CBA"
    print(check_ispallindrome(string))
