# Tuples
# Tuples are like lists, but they are IMMUTABLE, so it makes code more predictable
# Tuples CANNOT be sorted, reversed or modified and are ideal if your code doesn't need to ne changed
# Tuples are usually FASTER than LISTS, amd works great from things like GPS Coordinates
# If you don't need a list to change, use a TUPLE

my_tuple = (1,2,3,4,5,6)
print(my_tuple)        # Prints entire tuple
print(3 in my_tuple)   # Boolean check to see if 3 is in the tuple, returns true or false

user = {
    (1,2): [1,2,3],  # (1,2) is a tuple and can be accessed as follows:
    }
print(user[(1,2)]) # calls the key (1,2) which is a tuple for a key in the dictionary

# Tuple has 2 methods, 'count()' and 'index()'
print((1,2).count(2))  # Returns the number of 2's in the tuple (1,2)

das_tuple = ('a','b','c','d','e','f','f','f','g')  # tuple
print(das_tuple)  # Prints the tuple
print(das_tuple.index('e')) # Prints the index number in the tuple for 'e', Returns 4
print(das_tuple.count('f')) # Prints the number of 'f''s in the tuple, Returns 3
print(len(das_tuple))  # Prints the length of the tuple






