# Matrix Index

basket = ['x','a','b','c','d','e','d']
print(basket.index('a',0,6)) # prints the index for 'a' in the list
print(basket.index('c',0,6)) # Prints the index for 'c' in the list
print(basket.index('d',0,6)) # prints the index for 'd' in the list

# How to see if something is in the basket when you're not sure where to search
print('d' in basket) # this returns 'True' if d is in the list


# Count
# we can see how many times an item is in the list
print(basket.count('d')) # Returns 2 because 'd' is in the list 2 times

# Sort
#basket.sort() # Sorts the basket
print(basket)

# Sorted
print(sorted(basket))  # Creates a new copy of the basket and sorts it

# Copy
# Another method of copying a list
new_basket = basket.copy()
print(new_basket)

# Reverse
# This reverses the order of the list
# This example creates a Sorted and Reversed list
basket.sort()  # Sorts the list
basket.reverse()  # Reverses the order of the list
print(basket)  # Prints the list

# Reverse again
basket.sort()  # Sorts the list
basket.reverse()  # Reverses the order of the list
print(basket[::-1])  # Creates and prints a new list in reverse order using list slicing

# Range List
# To quickly create a list from a range
print(list(range(1, 101))) # Prints a list from 1 through 100
print(list(range(100))) # Prints a list from 0 through 99

# .join
sentence = ' '.join(['Hi', 'my', 'name', 'is', 'Bob']) # This method joins a list of items
print(sentence) # prints the new string


# List Unpacking
# This allows us to unpack a list any way we want and assign variables
a,b,c, * other, d = [1,2,3,4,5,6,7,8,9]
print(a)  # Prints the first item assigned to variable 'a'
print(b)  # Prints the 2nd item assigned to variable 'b'
print(c)  # Prints the 3rd item assigned  to variable 'c'
print(other) # Prints the remainder of the list assigned to to variable 'other' or whatever you want to name it
print(d)


# None
# None is the same as NULL in other languages and can be assigned to a variable when needed
weapons = None
print(weapons)
# In this case, game development, the user starts the game without any weapons and this is valid Python code











