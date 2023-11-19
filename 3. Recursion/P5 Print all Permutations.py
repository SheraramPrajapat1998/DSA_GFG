
def permutations(string):

    return recur(0, string)


def recur(index, string):
    if index == len(string):
        print("".join(string))
        return
    for i in range(index, len(string)):
        string[index], string[i] = string[i], string[index]
        recur(index+1, string)
        string[i], string[index] = string[index], string[i]
        # string[l], string[index] = string[index], string[l]


if __name__ == '__main__':
    string = list("ABC")
    permutations(string)
