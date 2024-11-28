# Write a function to count the number of vowels in a string.

string = input()
vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print(f"The number of vowels are {count}")