def generate_fibonacci_sequence(n: int) -> tuple[int]:
    a, b = 0, 1
    fibs = []
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return tuple(fibs)

def generate_fibonacci_sequence2(n: int) -> tuple[int]:
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return tuple(fibs[:n])

print("First 10 Fibonacci numbers stored in a tuple:")
fib_10 = generate_fibonacci_sequence(10)
print(fib_10)

print("First 20 Fibonacci numbers stored in a tuple:")
fib_20 = generate_fibonacci_sequence2(20)
print(fib_20)