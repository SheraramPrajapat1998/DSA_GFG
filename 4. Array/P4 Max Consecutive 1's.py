

def count_max_consecutive_1s(arr):
    max_count = 0
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            max_count = max(max_count, count)
    return max_count


if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 0]
    # arr = [1, 1, 1, 1]
    print(count_max_consecutive_1s(arr))
