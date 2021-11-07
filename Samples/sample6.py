# Dictionary Methods
# .get method to locate a key

user = {
    'race': 'black',
    'sex': 'male',
    'city': 'Chicago'

}

print((user.get('age', 55)))  # checks dictionary for 'age' key and returns value if present, otherwise returns 55
print(user.get('sex', 'female'))    # .get checks dictionary for key 'sex' and returns value.
                                    # If sex key not present, returns default value of female instead of error

print('city' in user.keys())  # Boolean returns True or False if 'key' is not in the dictionary
print('state' in user.keys())  # Boolean check if 'state' exists in keys
print('Chicago' in user.values()) # Boolean check if 'Chicago' exists in values

print(user.items()) # Grabs all the key:value entries in the dictionary - Returns a tuple

user2 = user.copy()  # Creates a copy of the dictionary
print(user)
print(user2)

print(user.pop('sex')) # will remove the key 'state' and return the value of what got removed - 'male'
print(user) # as you'll see, 'sex' no longer exists in user

print(user.popitem()) # will remove the last item in the dictionary in Python 3.7 and later versions
print(user)  # now there is only one item left in the dictionary

print(user.update({'city': 'Philadelphia'})) # Used to update a value, but can also add the 'key':'value to dict
print(user) # As you will see, the update actually added the item 'city':'Philadelphia' to the dictionary

user.clear() # Clears dictionary - creates an empty dictionary
print(user)
print(user.clear()) # will clear the dictionary - Return 'None'




