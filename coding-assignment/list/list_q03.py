# Write a program to find the missing number in an array containing n unique integers from 1 to n+1.

arr = [1, 2, 4, 5, 6]  
n = len(arr)  

total_sum = (n + 1) * (n + 2) // 2

array_sum = sum(arr)

missing_number = total_sum - array_sum

print("The missing number is:", missing_number)
