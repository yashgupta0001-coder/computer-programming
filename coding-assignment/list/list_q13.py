#Sort a list of tuples by the second element of each tuple.
tuples = [(1, 3), (4, 1), (2, 2)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)

