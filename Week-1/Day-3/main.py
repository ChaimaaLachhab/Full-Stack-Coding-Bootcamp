# class Dog():
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} is barking!")

# # Create an instance outside the class
# shelter_dog = Dog("Buddy")  
# shelter_dog.bark()

#######################################################

# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_details(self):
#     print("Hello my name is " + self.name)

#   def rename(self, new_nam):
#     self.name = new_nam
#     print("Hello my name is " + self.name)

# first_person = Person("John", 36)
# first_person.show_details()
# first_person.rename("chaimaa")

########################################################################

# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")

