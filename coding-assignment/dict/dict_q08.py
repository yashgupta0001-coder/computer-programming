#Write a function that updates a dictionary with default values if certain keys do not exist.
def update_with_defaults(d, defaults):
    d.update((k, d.get(k, v)) for k, v in defaults.items())
    return d

input_dict = {'apple': 10, 'banana': 20}
defaults = {'banana': 5, 'orange': 15, 'grape': 8}
print(update_with_defaults(input_dict, defaults))  

