# Write a Python program that takes a list of names in "First Last" format and prints them in "Last First" format.

# Input: A string of names in "First Last" format
names = input("Enter names in 'First Last' format separated by spaces: ").split()

# Convert each name to "Last First" format
reversed_names = [" ".join(name.split()[::-1]) for name in zip(names[::2], names[1::2])]

# Output: Names in "Last First" format
print(" ".join(reversed_names))