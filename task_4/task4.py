def factorials(n):
    res = 1
    for num in range(1, n + 1):
        res *= num
        yield res

print(*[i for i in factorials(5)])