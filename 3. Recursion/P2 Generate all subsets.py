def generate_subsets(index, string, temp):
    if index == len(string):
        print(temp)
        return
    temp.append(string[index])
    generate_subsets(index+1, string, temp)
    temp.pop()
    generate_subsets(index+1, string, temp)


if __name__ == '__main__':
    stirng = "ABC"
    generate_subsets(index=0, string=stirng, temp=[])
