from typing import List


def intersection(a:List,b:List, m:int, n:int ):
    i = 0
    j = 0
    while i < m and j < n:
        if i > 0 and a[i] == a[i-1]: i += 1
        if a[i] < b[j]: i += 1
        elif a[i] > b[j]: j += 1
        else:
            print(a[i])
            i += 1

if __name__ == "__main__":
    a = [10, 20, 20, 40, 60]
    b = [2, 20, 20, 20, 40]
    intersection(a, b, len(a), len(b))