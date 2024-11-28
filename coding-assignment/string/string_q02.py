#  Write a function to check if a given string is a palindrome.

string_to_check = "Madam"
cleaned_string = string_to_check.replace(" ", "").lower()

if cleaned_string == cleaned_string[::-1]:
    print(f'"{string_to_check}" is a palindrome.')
else:
    print(f'"{string_to_check}" is not a palindrome.')
