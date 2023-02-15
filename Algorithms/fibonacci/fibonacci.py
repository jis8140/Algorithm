# O(2^n)
def basic_fibo(n: int) -> int:
    return basic_fibo(n - 1) + basic_fibo(n - 2) if n >= 2 else n

# O(n)
def basic_iterative_fibo(n: int) -> int:
    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b

# O(n)
def dp_iterative_fibo(n: int) -> int:
    if n < 2:
        return n

    cache = [0, 1] + [0 for _ in range(n - 1)]
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]

# O(n)
def dp_recursive_fibo(n: int) -> int:
    if n < 2:
        return n

    cache = [0, 1] + [-1 for _ in range(n)]
    def recursive(p: int) -> int:
        if cache[p] != -1:
            return cache[p]

        cache[p] = recursive(p - 1) + recursive(p - 2)
        return cache[p]

    return recursive(n)

# O(n)
def python_fibo(n: int, __cache={0: 0, 1: 1}):
    if n in __cache:
        return __cache[n]

    __cache[n] = python_fibo(n - 1) + python_fibo(n - 2)
    return __cache[n]

# O(log(n))
def matrix_fibo(n: int) -> int:
    if n < 2:
        return n
    SIZE = 2
    matrix = [[1, 1], [1, 0]]

    def matrix_mul(a: list, b: list, size=SIZE) -> list:
        c = [[0] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    c[i][j] += a[i][k] * b[k][j]

        return c

    def matrix_power(a: list, n: int) -> list:
        if n == 1:
            return matrix

        tmp = matrix_power(a, n // 2)
        if n % 2:
            return matrix_mul(tmp, matrix_mul(tmp, a))
        return matrix_mul(tmp, tmp)

    matrix_fibo = matrix_power(matrix, n)
    return matrix_fibo[0][1]

# O(log(n))
def sqrt_fibo(n: int) -> int:
    sqrt_5 = 5 ** (1/2)

    def power(a, n: int):
        if n == 1:
            return a

        tmp = power(a, n // 2)
        if n % 2:
            return tmp * tmp * a
        return tmp * tmp

    ans = 1 / sqrt_5 * (power(((1 + sqrt_5) / 2), n) - power(((1 - sqrt_5) / 2), n))
    return int(ans)