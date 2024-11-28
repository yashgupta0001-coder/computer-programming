# Write a function sum_of_even_numbers that takes a list of integers and returns the sum of all even numbers in the list.

def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# Test case
print(sum_of_even_numbers([1, 2, 3, 4, 5, 6]))  # Output: 12
