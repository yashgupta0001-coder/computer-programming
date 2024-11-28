# Write a function count_occurrences that takes a list and an element, and returns the number of times the element appears in the list.

def count_occurrences(lst, element):
    return lst.count(element)

# Test case
print(count_occurrences([1, 2, 3, 2, 4, 2], 2))  # Output: 3
