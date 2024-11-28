# Write a function remove_vowels that takes a string and returns a new string with all vowels removed.


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in s if char not in vowels])

# Test case
print(remove_vowels("Hello World"))  # Output: "Hll Wrld"
