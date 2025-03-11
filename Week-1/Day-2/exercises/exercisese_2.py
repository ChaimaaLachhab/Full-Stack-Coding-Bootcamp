# 🌟 Exercise 2 : Cinemax #2

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

# Function to determine ticket price based on age
def get_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

# Calculate individual ticket prices and total cost
total_cost = 0
for name, age in family.items():
    price = get_ticket_price(age)
    print(f"{name.capitalize()} has to pay ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")

##################################################

family = {}

# Ask the user for family members
while True:
    name = input("Enter family member's name (or type 'done' to finish): ").strip()
    if name.lower() == "done":
        break
    age = int(input(f"Enter {name}'s age: "))
    
    family.update({name: age})

    # family[name] = age
    
    print(family)

# Calculate and display the ticket prices
total_cost = 0
for name, age in family.items():
    price = get_ticket_price(age)
    print(f"{name.capitalize()} has to pay ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")
