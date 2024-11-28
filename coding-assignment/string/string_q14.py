# Write a Python program that takes a list of destinations and prints them in alphabetical order.

# Input: List of destinations
destinations = input("Enter a list of destinations separated by commas: ").split(',')

# Strip spaces and sort destinations
sorted_destinations = sorted(destination.strip() for destination in destinations)

# Output in one line
print(", ".join(sorted_destinations))