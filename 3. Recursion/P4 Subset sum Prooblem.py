
def func(arr, total):
    temp = []
    return recur(0, total, arr)


def recur(index, total, arr):
    if index == len(arr):
        return 0
    if total == 0:
        return 1
    elif total < 0:
        return 0

    total -= arr[index]
    count = recur(index+1, total, arr)
    total += arr[index]
    count += recur(index+1, total, arr)
    return count


if __name__ == '__main__':
    arr = [4, 9, 1, 2, 3, 5, 7]
    print(func(arr, 10))
