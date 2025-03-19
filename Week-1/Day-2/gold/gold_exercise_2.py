# Exercise 2: Birthdays Advanced

birthdays = {
    "Alice": "1990/05/14",
    "Bob": "1985/09/23",
    "Charlie": "1992/12/04",
    "Diana": "2000/07/19",
    "Eve": "1995/03/28"
}

print("🎉 Welcome to the Advanced Birthday Look-up System!")
print("Here are the names in our database:")

for person in birthdays.keys():
    print(person)

name = input("\nEnter a name: ")

if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}.")
