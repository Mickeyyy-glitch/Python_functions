def factorials(n: int) -> int:
    res = 1
    for num in range(1, n + 1):
        res *= num
        yield res


print(*[elem for elem in factorials(5)])