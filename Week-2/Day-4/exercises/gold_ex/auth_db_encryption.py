import sqlite3
import bcrypt

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')

def add_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''
    INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, hashed_password))
    conn.commit()

def verify_user(username, password):
    cursor.execute('''
    SELECT password FROM users WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()
    if result:
        stored_password = result[0]
        return bcrypt.checkpw(password.encode('utf-8'), stored_password)
    return False

logged_in = None

while True:
    user_input = input("Please type 'login' to login, 'signup' to sign up, or 'exit' to quit: ").lower()

    if user_input == 'exit':
        print("Exiting the program...")
        break

    if user_input == 'login':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if verify_user(username, password):
            logged_in = username
            print(f"You are now logged in as {logged_in}.")
            break
        else:
            print("Invalid login credentials. Try again.")

    elif user_input == 'signup':
        while True:
            new_username = input("Enter a new username: ")
            cursor.execute('''
            SELECT * FROM users WHERE username = ?
            ''', (new_username,))
            if cursor.fetchone():
                print("Username already exists. Please try again.")
            else:
                new_password = input("Enter a new password: ")
                add_user(new_username, new_password)
                print(f"Account created successfully for {new_username}.")
                break

    else:
        print("Invalid input. Please type 'login', 'signup', or 'exit'.")

conn.close()
