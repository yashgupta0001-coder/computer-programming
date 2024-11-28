# Write a function to check if one string is a rotation of another string.

string1 = input()
string2 = input()

if len(string1) == len(string2) and string2 in (string1 + string1):
    result = True
else:
    result = False

print(result)
