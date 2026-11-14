def fibonacci(a, b, n):
    # Base case
    if n == 0:
        return

    print(a, end=" ")

    # Recursive case
    fibonacci(b, a + b, n - 1)


terms = 7

print("Fibonacci series:")
fibonacci(0, 1, terms)