# 🌟 Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Instantiate three Cat objects
cat1 = Cat("Lolo", 3)
cat2 = Cat("Soso", 5)
cat3 = Cat("Mimi", 2)


# Function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat3.age:
        return cat2
    else:
        return cat3

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# OR 

# Function to find the oldest cat
def find_oldest_cat(*cats):
    return max(cats, key=lambda cat: cat.age)

# Get the oldest cat
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Print the result
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
