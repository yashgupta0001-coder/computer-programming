# Count how many times each element appears in a list.
nums = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

