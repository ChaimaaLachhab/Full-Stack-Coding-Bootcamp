# Predicting the output of these expressions

print(3 <= 3 < 9)  # True (because 3 <= 3 is True and 3 < 9 is True)

print(3 == 3 == 3)  # True (because all three comparisons hold True)

print(bool(0))  # False (0 is considered False in a boolean context)

print(bool(5 == "5"))  # False (5 is an int, "5" is a string, so the comparison is False)

print(bool(4 == 4) == bool("4" == "4"))  # True (both comparisons return True, so True == True)

print(bool(bool(None)))  # False (None is False, bool(None) is False, and bool(False) is False)

# Additional expressions
x = (1 == True)  # True (1 is equivalent to True)
y = (1 == False)  # False (1 is not equivalent to False)
a = True + 4  # 5 (True is equivalent to 1, so 1 + 4 = 5)
b = False + 10  # 10 (False is equivalent to 0, so 0 + 10 = 10)

print("x is", x)  # x is True
print("y is", y)  # y is False
print("a:", a)  # a: 5
print("b:", b)  # b: 10
