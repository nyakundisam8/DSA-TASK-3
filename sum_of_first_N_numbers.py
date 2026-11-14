def sum_numbers(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return n + sum_numbers(n - 1)


number = 5
print("Sum:", sum_numbers(number))