# Remove Duplicates from a List
nums = [4, 5, 6, 4, 2, 6, 7, 8, 5]
result = []
for num in nums:
    if num not in result:
        result.append(num)
print(result)

