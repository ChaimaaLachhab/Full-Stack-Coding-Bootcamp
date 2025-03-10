# 🌟 Exercise 7: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove Banana
basket.remove("Banana")

# Remove Blueberries
basket.remove("Blueberries")

# Add Kiwi to the end
basket.append("Kiwi")

# Add Apples to the beginning
basket.insert(0, "Apples")

# Count apples
apple_count = basket.count("Apples")
print(f"There are {apple_count} apples in the basket.")

# Empty the basket
basket.clear()

# Print the empty basket
print(basket)
