def factorial(num):
    if num == 0 or num == 1:
        return num
    a = 1
    b = 2
    for i in range(3, num+1):
        a, b = b, a*b
        print(a, b)
    return a

def count_trailing_zeroes_in_factorial(num):
    # Naive sol: 1st find factorial then count last zeroes.

    # Eff. Sol: 10 = 2 * 5
    # 10 can only be formed from 2's and 5's
    # and in a factorial number  of 2's > number of 5's
    # so count the total number of 5's and that the total number of 0's in the last

    # NOTE: for each power of 5, there will be one more prime factor i.e. for
    # 25 -> 5*5 5 occurs two times and for 125->3 times and so on.

    # Trailing zero count: floor(n/5) + floor(n/25) + floor(n/125) + ...

    res = 0
    i = 5
    while i <= num:
        res += num//i
        i *= 5
    return res

if __name__ == '__main__':
    number = 6
    print(factorial(number))
    print(count_trailing_zeroes_in_factorial(6))