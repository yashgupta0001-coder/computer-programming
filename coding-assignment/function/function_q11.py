# Write a function sum_digits that takes an integer and returns the sum of its digits.

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

# Test case
print(sum_digits(1234))  # Output: 10
