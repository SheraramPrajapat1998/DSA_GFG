# Q. Given a number count the number of digits in it.
#

def count_digits(number):
    # count = 0
    # while number:
    #     count += 1
    #     number = number//10
    # return count
    # Time Complexity : O(log10(n)) or O(num digits)
    # Auxiliary Space: O(1) or constant

    # ------------------- OR -------------------
    if number//10 == 0:
        return 1
    return 1 + count_digits(number//10)
    # Time Complexity : O(log(n))
    # Auxiliary Space: O(log(n))

    # ------------------- OR -------------------
    # number of digits in N = log10(N) + 1.
    # Derivation: Suppose the number of digits in the number N is K.
    # Therefore, we can say that:
    # 10K-1 <= N < 10K

    # Applying base-10 logarithm to both sides in the above equation, we get:
    # K-1 <= log10(N) < K.

    # or, K - 1 + 1 <= log10(N) + 1 < K + 1
    # or, K <= log10(N) + 1 < K + 1

    # Therefore,
    # K = floor(log10(N) + 1)

print(count_digits(9))
print(count_digits(15))
print(count_digits(25))
print(count_digits(205))
print(count_digits(2051))
print(count_digits(42055))
