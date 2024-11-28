# Write a Python program that reads a list of prices, reverses the digits of each price, and prints the reversed prices.


# Input string of prices
prices = "123 456 789"

# Split the input string into a list of prices
prices_list = prices.split()

# Reverse the digits of each price
reversed_prices = [price[::-1] for price in prices_list]

# Print the reversed prices as a space-separated string
print(" ".join(reversed_prices))
