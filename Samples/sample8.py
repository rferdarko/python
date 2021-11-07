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
print(set(my_list)) # Prints set of my_list - will not print duplicates
my_set2 = set(my_list) # Creates a SET from the LIST to eliminate duplicates
print(my_set2)  # Prints the new set
my_list2 = list(my_set2)  # Creates a NEW LIST from the SET, there are NO Duplicates in this list
print(my_list2) # Prints the new list





