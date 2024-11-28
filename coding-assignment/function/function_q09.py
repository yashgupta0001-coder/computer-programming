# Write a function longest_word that takes a list of words and returns the longest word. If there are multiple words with the same length, return the first one.

def longest_word(words):
    return max(words, key=len)

# Test case
print(longest_word(["apple", "banana", "cherry", "kiwi"]))  # Output: "banana"
