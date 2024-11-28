# Define a function is_prime that checks if a number is a prime number.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(5))  # Output: True
print(is_prime(4))  # Output: False
