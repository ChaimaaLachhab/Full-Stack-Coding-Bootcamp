# 🌟 Challenge 1 : Multiples List

def generate_multiples(number, length):
    return [number * i for i in range(1, length + 1)]

# Ask the user for a number and a length
num = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

# Generate and display the list of multiples
result = generate_multiples(num, length) 
print("List of multiples:", result)

