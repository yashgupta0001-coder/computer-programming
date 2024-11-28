#Write a program to rotate an array k steps to the right.

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3 

k = k % len(arr)  

arr.reverse()

arr[:k] = arr[:k][::-1]
arr[k:] = arr[k:][::-1]

print("Array after rotating", k, "steps to the right:", arr)
