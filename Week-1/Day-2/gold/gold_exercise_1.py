# Exercise 1 : Birthday Look-up
birthdays = {
    "Alice": "1990/05/14",
    "Bob": "1985/09/23",
    "Charlie": "1992/12/04",
    "Diana": "2000/07/19",
    "Eve": "1995/03/28"
}

print("Welcome to the Birthday Look-up System!")
print("You can look up the birthdays of the people in the list!")

name = input("Enter a name: ")

if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don't have the birthday information for {name}.")
