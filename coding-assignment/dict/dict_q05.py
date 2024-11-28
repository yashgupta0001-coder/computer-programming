#Write a function that takes a dictionary and swaps its keys and values.
def swap_keys_values(d):
    return {v: k for k, v in d.items()}

input_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(swap_keys_values(input_dict))  

