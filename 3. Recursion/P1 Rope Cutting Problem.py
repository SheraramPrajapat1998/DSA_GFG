def cut_rope(n: int, a: int, b: int, c: int):
    if n == 0:
        return 0
    elif n < 0:
        return -1

    res = max(
        cut_rope(n-a, a, b, c),
        cut_rope(n-b, a, b, c),
        cut_rope(n-c, a, b, c),
    )

    if res == -1:
        return -1
    return res + 1
