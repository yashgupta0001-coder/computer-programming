#Write a function that takes a list of elements and returns a dictionary with the count of each element.
def count_occurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

lst = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
print(count_occurrences(lst))  

