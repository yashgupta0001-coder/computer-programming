# Write a function find_max that returns the largest number from a list of numbers, without using the built-in max() function.

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Test case
print(find_max([1, 2, 3, 4, 5]))  # Output: 5
