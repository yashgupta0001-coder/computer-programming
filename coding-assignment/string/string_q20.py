#  Write a program that takes a sentence and reverses the order of the words.

# Input: A sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words, reverse the order of words, and join them back
reversed_sentence = " ".join(sentence.split()[::-1])

# Output: The sentence with words in reverse order
print(reversed_sentence)
