# Find the second largest element in a list.
nums = [10, 20, 4, 45, 99]
unique_nums = list(set(nums))
unique_nums.sort()
second_largest = unique_nums[-2]
print(second_largest)

