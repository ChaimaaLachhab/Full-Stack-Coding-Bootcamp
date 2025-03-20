users = {
    'user1': '1',
    'user2': '2',
    'user3': '3'
}

logged_in = None

while True:
    user_input = input("Please type 'login' to login or 'exit' to quit: ").lower()

    if user_input == 'exit':
        print("Exiting the program...")
        break

    if user_input == 'login':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            logged_in = username
            print(f"You are now logged in as {logged_in}.")
            break
        else:
            print("Invalid login credentials. Try again.")

    else:
        print("Invalid input. Please type 'login' or 'exit'.")
