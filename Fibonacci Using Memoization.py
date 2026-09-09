def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

N = int(input("Enter N: "))

sequence = [fibonacci(i) for i in range(N)]

print(sequence)
