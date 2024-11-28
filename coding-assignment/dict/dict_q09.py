#Write a function that takes a list of words and groups them by their length in a dictionary. The dictionary should have the word length as the key, and the value should be a list of words of that length.
def group_by_length(words):
    length_dict = {}
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)
    return length_dict

words_list = ['apple', 'banana', 'kiwi', 'pear', 'cherry', 'fig']
print(group_by_length(words_list))

