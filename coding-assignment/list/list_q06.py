#Find the common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = []
for item in list1:
    if item in list2:
        intersection.append(item)
print(intersection)

