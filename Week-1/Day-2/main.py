# lst = [1, 2, 3, 4, "a", "b", "c", 38.5, "56.7"]
# print(lst)
# print(type(lst))
# print(type(lst[-1])) 

#################################################

# l1 = [1, 2, 3, 4, 5, 6]
# l1.append(3)
# l1.append([7, 8, 9])
# l1.extend([6, 7, 8])
# print(l1)


##################################################

# l1=[1, 2, 3, 4, 5, 6]
# l1.insert(2, 40)
# print(l1)


#################################################

# l2 = [1, 2, 3, 4, 5, "a", "a", "b", 1, 2, 4]
# s = l2.count(4)
# print(s)

##################################################

# a = ["b", "g", "a", "d", "f", "c", "h", "e"]
# x = sorted(a)
# print("a after sorted function")
# print(a)
# print(x)
# b = [1, 2, 5, 8, 3]
# b.sort()
# print(b)

#################################################

# lst = [0, 1, 2, 3, 4, 5, 6, 7]
# print(lst[0:4])
# print(lst[::])
# print(lst[::-1])

##################################################

# lst = [1, 2, 3, 4, 5, 6, 7]
# print(lst.pop())
# print(lst)
# lst.remove(4)
# print(lst) 
# lst.clear()
# print(lst)

##################################################

# t = (1, 2, 3, 4, 5, "a", "b", "c")
# t1 = 1, 2, 3, 4, "g", "l"
# print(t)
# print(t1)
# print(len(t))

#################################################

# t1 = (1, 2, 3, 4, 5)
# t2 = (6, 7, 8, 9)
# t3 = t1 + t2 
# print(t3)

################################################

# t = (1, 2, 10, 4, 5)
# print("Minimum element in the tuple",min(t))
# print("Maximum element in the tuple",max(t))

################################################

# dict = {1:'a', 2:'b', 5:'c', 4:'d'}
# print(dict)
# print(dict[5])

###############################################

# cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
# print(cubes.pop(4))
# print(cubes)
# print(cubes.popitem())
# print(cubes)
# cubes.clear()
# print(cubes)

##############################################

# d = {1:'10', 2:'20', 3:'30', 4:'40', 5:'50'}
# l1 =list(d.keys())
# print("the key values are:")
# print(l1)
# l2 = list(d.values())
# print("The values are of dictionary is")
# print(l2)
# l3 = list(d.items())
# print("the list items are")
# print(l3)

#############################################

# set1 = {1, 2, 3, 4, "hi", "world", "python"}
# print("python" in set1)
# set1.remove(4)
# print(set1)

############################################

# a = {1, 2, 3, 4, 5}
# b = {2, 3, 6, 7, 5}
# c = a^b 
# print(c)
# d = a - b
# print(d)
# e = b - a 
# print(e)

##########################################

# # A squaring lambda function
# square = lambda n : n*n
# num = square(5)
# print(num)

#########################################

# myList = [10, 25, 17, 9, 30, -5]
# # Double the value of each element
# myList2 = map(lambda n : n*2, myList)
# print(myList2)

#########################################

# myList = [10, 25, 17, 9, 30, -5]
# # Filters the elements which are not multiples of 5
# myList2 = filter(lambda n : n%5 == 0, myList)
# print(myList2)

########################################

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# print(sample_dict)
# del sample_dict["name"]
# del sample_dict["salary"]
# print(sample_dict)

#################################################

# my_books = {
#   "title": "Harry Potter",
#   "author": "JK Rowling",
# }

# for x, y in my_books.items():
#     print("the " + x + " is " + y)


################################################

# # range(start, stop[, step]) : iterator in loops.

# print(list(range(1, 10, 2)))

###############################################

# # enumerate(iterable) : enumerate each item in the iterable

# for item in enumerate('abcd'):
#     print(item)

# for (index_count, letter) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(index_count, letter))


################################################

# zip(iterable,..) : concat [iterables, …] in a tuple.

# list1 = [1,2,3]
# list2 = ['a','b','c']
# list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

# for item in zip(list1, list2, list3): # only go as far it is possible
#     print(item)

################################################

# x = 0
# while x < 2:
#     print(f'x is {x}')
#     x += 1
# else:
#     print('x is bigger than 2')

###############################################

# for letter in 'Leonardo':
#     if letter == 'a':
#         break
#     print(letter, end='') # end='' renders each letter next to the other


##############################################

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')

##############################################

