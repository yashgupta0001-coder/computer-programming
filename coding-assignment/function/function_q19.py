# Write a function capitalize_words that takes a sentence as input and returns the sentence with each word capitalized.

def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

# Test case
print(capitalize_words("hello world from python"))  # Output: "Hello World From Python"
