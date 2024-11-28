# Write a function fibonacci that returns the nth number in the Fibonacci sequence.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test case
print(fibonacci(6))  # Output: 8
