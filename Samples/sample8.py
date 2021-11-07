# SET
# Unordered Collections of UNIQUE Objects
# IN A SET THERE ARE NO DUPLICATES

my_set = {1,5,2,4,3,6}
print(my_set)
my_set.add(100) # Will get added to the set because 100 is not already in the set
my_set.add(5) # 5 WILL NOT get added to the set because it is already in the set and not UNIQUE
print(my_set)


# In order to return a list or a collection that contains only UNIQUE items
# WRAP the LIST in a SET

my_list = [1,2,3,4,5,5,5,6]  # This is a list with duplicates
print(my_list) # Prints my_list
print(len(my_list))  # Prints the length of the list
print(set(my_list)) # Prints set of my_list - will not print duplicates
my_set2 = set(my_list) # Creates a SET from the LIST to eliminate duplicates
print(my_set2)  # Prints the new set
print(len(my_set2))  # Prints the length of the new set
my_list2 = list(my_set2)  # Creates a NEW LIST from the SET, there are NO Duplicates in this list
print(my_list2) # Prints the new list
print(len(my_list2)) # Prints the Length of the New List

# OTHER SET FUNCTIONS

# .copy() will copy the set to a new set
this_set = my_set.copy()  # creates a new copy of the set
print(this_set)  # Prints the new copy of the set

# .clear() will clear the set
this_set.clear()  # Will clear the set
print(this_set) # Prints the now empty set

# .difference()
this_set = my_set.copy() # Makes another new copy of the original set
print(this_set) # Prints the new copy of the set
my_set.add(7)  # Adds 7 to the otiginal set
print(my_set.difference(this_set)) # Compares this_set to the modified original set


# .discard()
my_set.discard(7) # Discards 7 from the original set
print(my_set)

# .difference_update()
my_set.add(7)  # Adds 7 to my_set
print(my_set)  # prints my_set
this_set.difference_update(my_set)  # updates this_set with the difference from my_set
print(this_set)  # prints this_set - shows both sets are now identical

# .intersection()
set_1 = {1,2,3,4}
set_2 = {3,4,5,6}
print(f'set_1 contains {set_1} and set_2 contains {set_2}')
print(f'The intersection of the 2 sets contains {set_1.intersection(set_2)}')  # Prints the intersecting objects in the sets

# .isdisjoint()
# .issubset()
# .issuperset()
# .union()




