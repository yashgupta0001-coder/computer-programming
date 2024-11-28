#Write a program to find the second largest element in an array of integers.
arr = [12, 35, 1, 10, 34, 1]

if len(arr) < 2:
    print("There is no second largest element.")
else:
    first = second = float('-inf')  
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    if second == float('-inf'):
        print("There is no second largest element.")
    else:
        print("Second largest element is:", second)
