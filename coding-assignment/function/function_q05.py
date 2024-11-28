# Write a function filter_odd_numbers that returns a list of only odd numbers from the input list

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Test case
print(filter_odd_numbers([1, 2, 3, 4, 5]))  # Output: [1, 3, 5]
