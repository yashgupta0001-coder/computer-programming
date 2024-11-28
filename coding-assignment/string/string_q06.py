# Write a function to find the longest word in a given sentence.

sentence = "Find the longest word in this sentence"
words = sentence.split()
longest_word = max(words, key=len)
print(f"The longest word is: '{longest_word}'")
