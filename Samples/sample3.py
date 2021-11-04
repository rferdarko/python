# Matrix - multidimensional array
my_matrix = [
    [1,2,3,4,5,6,7,8,9,10],  # Row Index 0
    [2,4,6,8,10,12,14,16,18,20],  # Row Index 1
    [7,8,9,10,11,12,13,14,15,16]   # Row Index 2
]
print()
print('Matrix')
print(my_matrix[0][2]) # prints top row, 3rd column index
print(my_matrix[1][4]) # prints 2nd row, 5th column index
print(my_matrix[2][9]) # prints 3rd row, 10th column index
print()

# Adding
print('Adding')
basket = [1,2,3,4,5]
new_list = basket  # both point at the same list
new_list.append(100) # This function appends the same list for both pointers
new_list = basket[:] # This creates a new list by copying the items from basket one for one
new_list.append(200) # this appends ONLY the new_list list
print(basket)
print(new_list)
print()

# Insert
print('Insert')
basket2 = [1,2,3,4,5]
print(basket2)
basket2.insert(5,6) # Inserts Index, Object to add 6 to Index 5
print(basket2)

# Extend
print('Extend')
basket3 = [1,2,3,4,5]
print(basket3)
basket3.extend([120, 125, 130]) # extends the list to include the new objects
print(basket3)

# Removing
print('Removing')
basket3.pop() # pop removes the object at the end of the list
print(basket3) # prints basket3 after object 130 was removed
basket3.pop(0) # removes the item at Index 0
print(basket3) # shows object 1 from Index 0 was removed


# .remove(Index) will remove the item for the Index number indicated
basket3.remove(2) # will remove the object at Index 2 (from original index)
print(basket3)

# pop returns whatever you removed, but remove returns nothing. So, you can create a new list from pop items
basket4 = basket3.pop()
print(basket4) # Contains the last item popped from basket3
print(basket3)

# Clear
# This will empty the list
basket3.clear()  # clears the contents of the list
print(basket3)  # prints the empty list

