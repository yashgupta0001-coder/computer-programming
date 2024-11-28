# Remove every third element from a list.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x for i, x in enumerate(nums) if (i + 1) % 3 != 0]
print(result)

