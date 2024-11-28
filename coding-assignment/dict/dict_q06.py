#Write a function that removes all keys from a dictionary that have a specific value.
def remove_keys_by_value(d, value_to_remove):
    return {k: v for k, v in d.items() if v != value_to_remove}

input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(remove_keys_by_value(input_dict, 1))  

