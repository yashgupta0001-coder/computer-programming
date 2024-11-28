#Find all elements greater than the mean of the list.
nums = [1, 2, 3, 4, 5]
mean = sum(nums) / len(nums)
greater_than_mean = [x for x in nums if x > mean]
print(greater_than_mean)

