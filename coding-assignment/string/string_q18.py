#  Write a program that takes a paragraph of text and capitalizes the first letter of each sentence.

# Input: A paragraph of text
paragraph = input("Enter a paragraph of text: ")

# Split the paragraph into sentences
sentences = paragraph.split('. ')

# Capitalize the first letter of each sentence and rejoin
capitalized_paragraph = '. '.join(sentence.capitalize() for sentence in sentences)

# Output: The paragraph with capitalized sentences
print(capitalized_paragraph)
