# Q. Print frequencies of chars(sorted order according to characters) in a string of lower alphabets.
# Ex: I/P: "geeksforgeeks"
#     O/P: e 4
#          f 1
#          g 2
#          k 2
#          o 1
#          r 1
#          s 2

def print_frequencies(string):
    total_chars = 26
    count = [0]*total_chars
    for char in string:
        count[ord(char) - ord('a')] += 1 
        # ord returns the number representing the unicode code of a specified character.

    for i in range(total_chars):
        if(count[i] > 0):
            print(chr(ord('a')+i), count[i]) 
            # chr convert the ASCII code into its corresponding character.
            
string = "geeksforgeeks"
print_frequencies(string)
