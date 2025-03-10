# Exercise 4: Check the Index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter a name: ")
if user_name in names:
    print(f"{user_name} is at index {names.index(user_name)}")
else:
    print("Name not found!")
