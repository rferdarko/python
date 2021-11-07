# SET
# Unordered Collections of UNIQUE Objects
# IN A SET THERE ARE NO DUPLICATES

my_set = {1,2,3,4,5}
print(my_set)
my_set.add(100) # Will get added to the set because 100 is not already in the set
my_set.add(5) # 5 WILL NOT get added to the set because it is already in the set and not UNIQUE
print(my_set)

