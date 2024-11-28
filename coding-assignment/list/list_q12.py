#Count how many strings in a list are palindromes.
words = ["radar", "python", "level", "world"]
palindrome_count = sum(1 for word in words if word == word[::-1])
print(palindrome_count)

