# Write a function count_characters that takes a string and returns a dictionary with the count of each character in the string.

def count_characters(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count

# Test case
print(count_characters("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
