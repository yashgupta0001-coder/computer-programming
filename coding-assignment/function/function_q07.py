# Write a function count_vowels that counts how many vowels (a, e, i, o, u) are in a given string.

def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s if char.lower() in vowels)

# Test case
print(count_vowels("Hello World"))  # Output: 3
