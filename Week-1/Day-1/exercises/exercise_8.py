# 🌟 Exercise 8 : Sandwich Orders
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich",
    "Pastrami sandwich"
]

# Remove all occurrences of "Pastrami sandwich"
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    # Take the first sandwich
    sandwich = sandwich_orders.pop(0)
    
    # Add to finished list
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")
