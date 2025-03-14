# Exercise 2: Custom List Class

import random

class MyList:
    def __init__(self, letters):
        """Initialize the list with a given list of letters."""
        self.letters = letters

    def reverse_list(self):
        """Return the reversed list."""
        return self.letters[::-1]

    def sorted_list(self):
        """Return the sorted list."""
        return sorted(self.letters)

    def generate_random_list(self):
        """Generate a list of random numbers with the same length as self.letters."""
        return [random.randint(1, 100) for _ in range(len(self.letters))]

# Example usage:
mylist = MyList(['b', 'd', 'a', 'c'])
print("Reversed List:", mylist.reverse_list())
print("Sorted List:", mylist.sorted_list())
print("Random List:", mylist.generate_random_list())
