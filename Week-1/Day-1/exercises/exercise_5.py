# 🌟 Exercise 5 : Favorite Numbers

my_fav_numbers = {0, 1, 2}

# Adding two new numbers
my_fav_numbers.update({3, 4})

# Removing the last number
my_fav_numbers.remove(max(my_fav_numbers))


friend_fav_numbers = {6, 8, 15}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)
