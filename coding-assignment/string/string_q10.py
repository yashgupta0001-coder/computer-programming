# Write a program that takes a list of names, rearranges them so that names starting with a vowel come first, and then prints the rearranged list.

# Input string
input_str = "Alice Bob Uma Charlie Eve"

# Convert the input string into a list of names
names = input_str.split()

# Separate names starting with a vowel and those that don't
vowels = 'AEIOUaeiou'
vowel_names = [name for name in names if name[0] in vowels]
non_vowel_names = [name for name in names if name[0] not in vowels]

# Combine the lists with vowel names first
rearranged_names = vowel_names + non_vowel_names

# Print the rearranged list
print(" ".join(rearranged_names))
