# Write a function find_prime_numbers that takes an integer n and returns a list of all prime numbers less than or equal to n.

def find_prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Test case
print(find_prime_numbers(10))  # Output: [2, 3, 5, 7]
