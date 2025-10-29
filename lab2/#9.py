def count_divisors(n):
    return len([i for i in range(1, n + 1) if n % i == 0])

N = int(input("Enter N: "))
result = {i: count_divisors(i) for i in range(1, N + 1)}

print(result)
