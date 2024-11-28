#Write a function that returns the key associated with the maximum value in a dictionary.
def get_key_with_max_value(d):
    return max(d, key=d.get)

input_dict = {'apple': 10, 'banana': 20, 'orange': 15}
print(get_key_with_max_value(input_dict)) 
