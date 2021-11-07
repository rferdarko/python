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


