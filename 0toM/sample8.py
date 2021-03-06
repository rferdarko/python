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
another_set21 = {1,2,3,4,5}
another_set22 = {4,5,6,7}
print(another_set21.difference_update(another_set22)) # updates this_set with the similarities removed
print(another_set21) # Shows 4,5 contained in set another_set22 were removed from another_set21
print(another_set22)  # Prints another_set22

# .intersection()
set_1 = {1,2,3,4}
set_2 = {3,4,5,6}
print(f'set_1 contains {set_1} and set_2 contains {set_2}')
print(f'The intersection of the 2 sets contains {set_1.intersection(set_2)}')
# Prints the intersecting objects in the sets
print(set_1 & set_2)  # Another intersection method

# .isdisjoint()
print(set_1.isdisjoint(set_2)) # Checks to see if this is 2 circles overlapping, returns False if they are overlapping

# .issubset()
set_3 = {3,4}
set_4 = {3,4,5,6}
print(set_3.issubset(set_4))  # Checks to see if set3 is a subset of set4
# True as the entirety of set3 is inside of set4

# .issuperset()
print((set_4.issuperset(set_3)))  # Checks to se if set4 is a superset of set3 - this is true

# .union()
print(set_1.union(set_2)) # Unites the two sets and removed any duplicates

print(set_1 | set_2)  # another way to create a union in Python


