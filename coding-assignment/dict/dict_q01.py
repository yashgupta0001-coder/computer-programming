#Write a function that merges two dictionaries into one. If a key appears in both dictionaries, the value from the second dictionary should be used.
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    merged.update(dict2)   
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))  
