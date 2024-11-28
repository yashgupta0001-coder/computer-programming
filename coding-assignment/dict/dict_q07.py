#Write a function that checks if a specific key exists in a dictionary.
def key_exists(d, key):
    return key in d

input_dict = {'apple': 10, 'banana': 20, 'orange': 30}
print(key_exists(input_dict, 'banana'))  
print(key_exists(input_dict, 'grape'))   
