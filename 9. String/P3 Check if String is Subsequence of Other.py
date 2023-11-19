# Q. Given a string check if subsequence of other string or not.


def check_issubsequence(string, substring):
    # naive method
    # generate all possinble subsequences and check if there exists subsequence
    # equal to substring.
    # TC: O(n * 2^n) -> 2^n for generating all subsequences and n for checking in it

    # compare for ith and jth index for both string and if value is same then increment
    # both indexes else increment ith index. In the end, if jth index is last index of
    # substring then substirng is subsequence else it's not.
    string_idx = 0
    substring_idx = 0
    string_size = len(string)
    substring_size = len(substring)

    if string_size < substring_size:
        return False

    while ((string_idx < string_size) and (substring_idx < substring_size)):
        if(string[string_idx] == substring[substring_idx]):
            string_idx += 1
            substring_idx += 1
        else:
            string_idx += 1
    return substring_idx == substring_size
    # TC: O(n+m)
    # Aux Space: O(1)

    

if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    substring = "GRGES"
    # substring = "GEEKZ"
    print(check_issubsequence(string, substring))
