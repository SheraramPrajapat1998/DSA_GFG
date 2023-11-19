
arr = [10, 10, 10, 25, 30, 30, 30]
result = []
temp = arr[0]
count = 1
for i in range(1, len(arr)):
    if arr[i] == temp:
        count += 1
    elif arr[i] !=temp or i == len(arr) - 1:
        result.append(count)
        count = 1
        temp = arr[i]

print(result)