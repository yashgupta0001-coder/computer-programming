# Write a function to count the frequency of each character in a string.

string = "example"
frequency = {}

for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)