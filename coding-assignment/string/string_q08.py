# Write a function to find the first non-repeating character in a string.

string = input()
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

first_non_repeating = None
for char in string:
    if char_count[char] == 1:
        first_non_repeating = char
        break

print(first_non_repeating)