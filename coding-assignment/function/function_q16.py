# Write a function find_gcd that computes the greatest common divisor (GCD) of two numbers using recursion.


def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)

# Test case
print(find_gcd(56, 98))  # Output: 14
