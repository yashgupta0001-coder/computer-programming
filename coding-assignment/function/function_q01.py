# Define a function is_palindrome that takes a string as input and returns True if the string is a palindrome and False otherwise.

def is_palindrome(s):
    return s == s[::-1]

# Test cases
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False