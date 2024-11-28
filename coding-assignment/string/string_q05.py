# Write a function to check if two strings are anagrams.

string1 = input().strip()
string2 = input().strip()

if sorted(string1) == sorted(string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
