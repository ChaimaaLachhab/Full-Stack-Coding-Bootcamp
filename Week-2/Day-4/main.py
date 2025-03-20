# import sqlite3

# conn = sqlite3.connect('database.sqlite')
# cursor = conn.cursor()
# print("Opened database successfully")

# cursor.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE
#          (ID INT PRIMARY KEY NOT NULL,
#          NAME TEXT NOT NULL,
#          AGE INT NOT NULL);''')

# cursor.execute("DELETE FROM EMPLOYEE")
# conn.commit()

# try:
#     cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (1, 'Razi', 14)")
#     cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (2, 'Jon', 19)")
#     cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (3, 'Martha', 35)")
#     conn.commit()
#     print("Inserted records successfully")
# except sqlite3.IntegrityError as e:
#     print("Error inserting data:", e)

# conn.close()

# conn = sqlite3.connect('database.sqlite')
# cursor = conn.cursor()

# try:
#     cursor.execute("DELETE FROM EMPLOYEE WHERE ID = 2")
#     conn.commit()
#     print("Deleted record with ID = 2 from EMPLOYEE")
# except sqlite3.OperationalError as e:
#     print("Error deleting record:", e)

# conn.close()

# conn = sqlite3.connect('database.sqlite')
# cursor = conn.cursor()

# try:
#     cursor.execute("SELECT * FROM EMPLOYEE")
#     results = cursor.fetchall()
# except sqlite3.OperationalError as e:
#     print("Error:", e)

# conn.close()

# for item in results:
#     print(item)


###################################################

# import requests
# import sqlite3
# from faker import Faker
# from time import time

# def create_table():
#     connection = sqlite3.connect('jokes.db')
#     cursor = connection.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS jokes (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             joke TEXT NOT NULL
#         );
#     ''')
#     connection.commit()
#     connection.close()
#     print("✅ Table 'jokes' is ready!")


# def get_jokes(n):
#     for i in range(n):
#         print(f"🔹 Fetching joke {i + 1}...")

#         # Appel API
#         url = 'https://api.chucknorris.io/jokes/random'
#         response = requests.get(url)

#         if response.status_code != 200:
#             print("❌ Failed to fetch joke!")
#             continue

#         data = response.json()
#         joke = data['value']

#         # Connexion à la base de données et insertion
#         connection = sqlite3.connect('jokes.db')
#         cursor = connection.cursor()

#         # Insertion sécurisée
#         cursor.execute("INSERT INTO jokes (joke) VALUES (?)", (joke,))

#         connection.commit()
#         connection.close()

#     print(f"✅ {n} jokes have been added!")


# # ===========================
# # 3. Générer de fausses données (faux noms en blagues)
# # ===========================
# def gen_fake_data(n):
#     start = time()
#     faker = Faker()

#     connection = sqlite3.connect('jokes.db')
#     cursor = connection.cursor()

#     for i in range(n):
#         name = faker.name()
#         print(f"🔸 Inserting fake joke {i + 1}: {name}")

#         cursor.execute("INSERT INTO jokes (joke) VALUES (?)", (name,))

#     connection.commit()
#     connection.close()

#     end = time()
#     print(f"✅ Inserted {n} fake jokes in {round(end - start, 2)}s!")


# # ===========================
# # 4. Afficher les blagues enregistrées
# # ===========================
# def show_jokes():
#     connection = sqlite3.connect('jokes.db')
#     cursor = connection.cursor()

#     cursor.execute("SELECT * FROM jokes")
#     jokes = cursor.fetchall()

#     connection.close()

#     print("\n📜 List of Jokes:")
#     for joke in jokes:
#         print(f"{joke[0]}. {joke[1]}")


# # ===========================
# # 5. Exécuter le script
# # ===========================
# if __name__ == "__main__":
#     create_table()

#     while True:
#         print("\n=== MENU ===")
#         print("1. Fetch Chuck Norris jokes from API")
#         print("2. Generate fake joke data")
#         print("3. Show all jokes in database")
#         print("4. Exit")

#         choice = input("Choose an option (1-4): ")

#         if choice == "1":
#             number = int(input("How many jokes do you want to fetch? "))
#             get_jokes(number)

#         elif choice == "2":
#             number = int(input("How many fake jokes do you want to generate? "))
#             gen_fake_data(number)

#         elif choice == "3":
#             show_jokes()

#         elif choice == "4":
#             print("👋 Goodbye!")
#             break

#         else:
#             print("❌ Invalid choice. Please try again.")


#################################################################
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1234'
DATABASE = 'dvdrental'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

cursor = connection.cursor()

query = "SELECT * FROM customer LIMIT 20;"

cursor.execute(query)

results = cursor.fetchall()

connection.close()

for item in results:
    print(item)