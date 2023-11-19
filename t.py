
def find_power(x, y, count=0):
    if y == 0:
        count += 1
        print(count)
        return 1
    temp = find_power(x, y//2)
    if y & 1:
        count += 1
        return x * temp * temp
    else:
        count += 1
        return temp * temp
    # TC: O(logN)


# print(find_power(5, 4))


def print_prime_numbers(N):
    isprime = [True for i in range(N+1)]
    isprime[1]= False
    for i in range(2, N+1):
        if(isprime[i]):
            for j in range(2*i, N+1, i):
                isprime[j] = False
    for i in range(1, N+1):
        if(isprime[i]):
            print(i, end=' ')
    print('\n')
print_prime_numbers(100)

