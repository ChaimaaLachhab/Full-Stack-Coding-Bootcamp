# 🌟 Exercise 3: Zara

# 1. Creating the brand dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": ["Amancio", "Ortega", "Gaona"],
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# 2. Change the number of stores to 2
brand["number_stores"] = 2

# 3. Print a sentence explaining who Zara's customers are
print(f"\nZara dresses {', '.join(brand['type_of_clothes'])}.")

# 4. Add a key "country_creation" with the value "Spain"
brand["country_creation"] = "Spain"

# 5. Check if the key "international_competitors" exists and add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 6. Remove the information about the creation date
del brand["creation_date"]

# 7. Print the last international competitor
print(f"\nLast international competitor: {brand['international_competitors'][-1]}")

# 8. Print the major clothing colors in the US
print(f"\nThe major clothing colors in the US are: {', '.join(brand['major_color']['US'])}")

# 9. Print the number of key-value pairs in the dictionary
print(f"\nThe dictionary contains {len(brand)} key-value pairs.")

# 10. Print the dictionary keys
print("\nDictionary keys:", list(brand.keys()))

# 11. Create another dictionary more_on_zara
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10_000
}

# 12. Add the information from more_on_zara to brand
brand.update(more_on_zara)

# 13. Print the value of "number_stores"
print(f"\nNumber of stores: {brand['number_stores']}")
