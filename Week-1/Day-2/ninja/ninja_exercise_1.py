# Exercise 1: Cars

car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

car_list = car_string.split(", ")

print(f"Number of manufacturers: {len(car_list)}")

print("Manufacturers in reverse order (Z-A):")
print(sorted(car_list, reverse=True))

count_o = sum(1 for car in car_list if 'o' in car.lower())

count_no_i = sum(1 for car in car_list if 'i' not in car.lower())

print(f"Manufacturers with 'o': {count_o}")
print(f"Manufacturers without 'i': {count_no_i}")

car_list_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_cars = sorted(set(car_list_with_duplicates))

print(f"Unique manufacturers ({len(unique_cars)}): {', '.join(unique_cars)}")

reversed_names = sorted([car[::-1] for car in unique_cars])
print("Reversed names sorted alphabetically:", reversed_names)
