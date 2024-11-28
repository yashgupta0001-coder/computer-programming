# Write a program that takes a list of prices and prints them in ascending order.

# Input: A list of prices
prices = list(map(int, input("Enter prices separated by spaces: ").split()))

# Sort the prices in ascending order
sorted_prices = sorted(prices)

# Output: Sorted prices
print(" ".join(map(str, sorted_prices)))
