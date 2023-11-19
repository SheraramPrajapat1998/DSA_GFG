from typing import List

def union_naive(a: List, b: List, m: int, n: int):
    arr = [0 for i in range(m+n)]
    for i in range(m):
        arr[i] = a[i]
    for i in range(n):
        arr[m+i] = b[i]

    arr.sort()
    # don't print duplicates elements
    for i in range(m+n):
        if(i==0 or arr[i]!=arr[i-1]):
            print(arr[i])

    # TC: (m+n)log(m+n)


def union(a:List,b:List, m:int, n:int ):
    i = 0
    j = 0
    while i < m and j < n:
        if i > 0 and a[i] == a[i-1]:
            i += 1
            continue
        if j > 0 and b[j] == b[j-1]:
            j += 1
            continue
        if a[i] == b[j]:
            print(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            print(a[i])
            i += 1
        else:
            print(b[j])
            j += 1

    while i < m:
        if(i > 0 and a[i] != a[i-1]):
            print(a[i])
            i += 1
    while j < m:
        if(j > 0 and b[j] != b[j-1]):
            print(b[j])
            j += 1

    # TC: O(m+n)
    # Auxilary Space: O(1)

if __name__ == "__main__":
    a = [10, 20, 20, 40, 60]
    b = [2, 20, 20, 20, 40]
    union(a, b, len(a), len(b))
