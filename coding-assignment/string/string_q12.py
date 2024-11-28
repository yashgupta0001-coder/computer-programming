#  Write a Python program that takes a list of names and removes any duplicates, then prints the unique names.


# Input list of names
names = "John Mary John Alex Alex"

# Convert the input string into a list of names
names_list = names.split()

# Create an empty list to store unique names
unique_names = []

# Iterate through the list and add names to unique_names only if they aren't already in it
for name in names_list:
    if name not in unique_names:
        unique_names.append(name)

# Print the unique names as a space-separated string
print(" ".join(unique_names))

