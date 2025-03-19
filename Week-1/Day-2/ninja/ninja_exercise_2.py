# Exercise 2: What’s your name?

def get_full_name(first_name, last_name, middle_name=""):
    """Returns a full name, including middle name if provided."""
    if middle_name:
        return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    return f"{first_name.capitalize()} {last_name.capitalize()}"

print(get_full_name(first_name="Chaimaa", middle_name="Ahmed", last_name="LACHHAB"))
print(get_full_name(first_name="Chaimaa", last_name="LACHHAB"))
