import random

# Exercise 1: What is the Season?
month = int(input("Enter a month (1-12): "))
if 3 <= month <= 5:
    print("Season: Spring")
elif 6 <= month <= 8:
    print("Season: Summer")
elif 9 <= month <= 11:
    print("Season: Autumn")
else:
    print("Season: Winter")
