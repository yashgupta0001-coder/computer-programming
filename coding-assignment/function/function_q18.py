# Write a function find_missing_number that takes a list of n-1 numbers from 1 to n, with one number missing. It should return the missing number.

def find_missing_number(lst, n):
    return n * (n + 1) // 2 - sum(lst)

# Test case
print(find_missing_number([1, 2, 4, 5, 6], 6))  # Output: 3
