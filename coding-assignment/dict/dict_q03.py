#Write a function that takes a dictionary and returns a new dictionary sorted by the values in ascending order.

def sort_dict_by_value(d):
    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    return sorted_dict

input_dict = {'apple': 4, 'banana': 2, 'orange': 3}
print(sort_dict_by_value(input_dict))  

