#Remove Duplicates While Maintaining Order:
lst = [1, 2, 2, 3, 4, 4, 5]
seen = set()
result = []
for item in lst:
    if item not in seen:
        seen.add(item)
        result.append(item)
print(result)  
