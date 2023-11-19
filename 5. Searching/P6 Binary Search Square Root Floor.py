

def sqroot_floor(number):
    low = 0
    high = number
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        midsq = mid*mid
        if midsq == number:
            return mid
        elif midsq > number:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    return ans


if __name__ == '__main__':
    number = 26
    print(sqroot_floor(number))
