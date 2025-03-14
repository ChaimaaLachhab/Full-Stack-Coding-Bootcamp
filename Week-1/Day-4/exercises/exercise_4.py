# 🌟 Exercise 4: Family

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! A new family member {kwargs['name']} is born!")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] >= 18
        return False

    def family_presentation(self):
        print(f"The {self.last_name} Family:")
        for member in self.members:
            print(member)

# ✅ Creating a family instance
family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

# ✅ Calling methods
family.family_presentation()
print(f"Is Michael over 18? {family.is_18('Michael')}")
family.born(name="Emma", age=0, gender="Female", is_child=True)
family.family_presentation()
