#Write a function that finds all the keys in a dictionary that have a given value.
def find_keys_by_value(d, target_value):
    return [k for k, v in d.items() if v == target_value]
input_dict = {'apple': 10, 'banana': 20, 'orange': 10, 'grape': 15}
target_value = 10
print(find_keys_by_value(input_dict, target_value))  

