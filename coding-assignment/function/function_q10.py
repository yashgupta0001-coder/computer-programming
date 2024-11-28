# Write a function is_anagram that checks if two strings are anagrams of each other. Two strings are anagrams if they contain the same characters in any order.


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Test case
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))    # Output: False
