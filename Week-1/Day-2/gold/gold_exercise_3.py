# Exercise 3: Sum

def calculate_sum(x):
    """Returns the value of X + XX + XXX + XXXX."""
    x_str = str(x)
    return int(x_str) + int(x_str * 2) + int(x_str * 3) + int(x_str * 4)

x = int(input("Enter a number: "))
print(f"Result: {calculate_sum(x)}")
