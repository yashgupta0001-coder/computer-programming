# Write a function sum_of_squares that returns the sum of the squares of the elements in a list.


def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

# Test case
print(sum_of_squares([1, 2, 3]))  # Output: 14 (1^2 + 2^2 + 3^2)
