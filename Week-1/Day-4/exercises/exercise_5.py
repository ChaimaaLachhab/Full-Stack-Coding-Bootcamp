# 🌟 Exercise 5: The Incredibles Family

from exercise_4 import Family

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    print(f"{name} uses their power: {member['power']}!")
                else:
                    raise Exception(f"{name} is not old enough to use their power!")

    def incredible_presentation(self):
        print(f"✨ Here is our powerful family, The {self.last_name} Family! ✨")
        super().family_presentation()

# ✅ Creating an instance of The Incredibles family
incredible_family = TheIncredibles("Incredibles", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
])

# ✅ Calling methods
incredible_family.incredible_presentation()
incredible_family.use_power("Michael")

# ✅ Adding a new baby member
incredible_family.born(name="Jack", age=0, gender="Male", is_child=True, power="Unknown Power", incredible_name="BabyJack")

# ✅ Calling presentation again
incredible_family.incredible_presentation()
