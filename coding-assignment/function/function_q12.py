# Write a function count_words that takes a string and returns the number of words in the string. A word is defined as a sequence of non-space characters.


def count_words(s):
    return len(s.split())

# Test case
print(count_words("Hello, how are you today?"))  # Output: 5
