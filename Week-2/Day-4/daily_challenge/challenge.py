import sqlite3
import requests
import random

conn = sqlite3.connect('countries.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    capital TEXT,
    flag TEXT,
    subregion TEXT,
    population INTEGER
)
''')

response = requests.get('https://restcountries.com/v3.1/all')
countries_data = response.json()

random_countries = random.sample(countries_data, 10)

def insert_country(name, capital, flag, subregion, population):
    query = "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, (name, capital, flag, subregion, population))
    conn.commit()

for country in random_countries:
    name = country.get('name', {}).get('common', 'N/A')
    capital = country.get('capital', ['N/A'])[0]
    flag = country.get('flags', {}).get('svg', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 0)

    insert_country(name, capital, flag, subregion, population)

print("Countries successfully added to the database!")
cursor.execute("SELECT * FROM countries")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
