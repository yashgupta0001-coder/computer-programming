#Group consecutive elements of a list into pairs.
nums = [1, 2, 3, 4, 5, 6]
pairs = [(nums[i], nums[i+1]) for i in range(len(nums)-1)]
print(pairs)
