# Q. Given N people in a circle, Kill Kth person in each iteration,
# till last servivor remains.


def josephus(n, k):
    """Return last servivor with respect to 0"""
    if n == 1:
        return 0
    return (josephus(n-1, k)+k) % n


def josephus_start_from_position(n, k, position=0):
    if position >= n:
        position = position % n
    return josephus(n, k) + position


if __name__ == '__main__':
    n = 5
    k = 3
    print(josephus_start_from_position(n, k, 1))
