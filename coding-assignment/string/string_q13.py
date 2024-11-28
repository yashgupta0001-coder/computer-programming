# Write a Python program that takes a paragraph of text and capitalizes the first letter of each sentence.

# Input paragraph of text
paragraph = "hello. my name is john. i love programming."

# Split the paragraph into sentences based on periods followed by spaces
sentences = paragraph.split('. ')

# Capitalize the first letter of each sentence and keep the rest of the sentence intact
capitalized_sentences = [sentence[0].upper() + sentence[1:] if sentence else '' for sentence in sentences]

# Join the sentences back together with '. ' and add a period at the end if needed
capitalized_paragraph = '. '.join(capitalized_sentences)

# Ensure the paragraph ends with a period
if capitalized_paragraph and capitalized_paragraph[-1] != '.':
    capitalized_paragraph += '.'

print(capitalized_paragraph)
