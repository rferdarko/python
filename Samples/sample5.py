# Dictionary   dict()
# A way to organize data in Python through 'key' : 'value' pairs

dictionary = {
    'a': [1,2,3,4,5,6],
    'b': 2,
    'c': 3,
    'd': 4
}
print('Dictionary')
print(dictionary) # Prints entire dictionary
print(dictionary['b'])  # Prints the value for dictionary key 'b'
print(dictionary['a'][4])


# This option created multiple dictionaries contained withing a list
mylist = [     # Start of list
    {  # dictionary 0
        'a': [99,88,77,66,55,44,33,22,11],   # key: value array
        'b': 'X',                            # key : value
        'c': [21,22,23,24,25,26]             # key:value array
},     # End of dictionary 0
{      # dictionary 1
    'a': [15,16,17],     # key:value array
    'b': 'z',            # key:value
    'c': 'w'             #kay:value
}   # End of dictionary 1

]   # End of list

print(mylist[1]['a'][2])   # Prints from list, dictionary '1' key 'a' value '2'
print(mylist[0]['a'][3])   # Prints from list, dictionary '0' key 'a' value '3'
print(mylist[1]['b'])   # Prints from list, dictionary '1' key 'b'
print(mylist[0]['c'][4])   # Prints from list, dictionary '0' key 'c' value '4'
