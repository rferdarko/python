# lists  lists in python are like arrays in other languages

li1 = [1, 2, 3, 4, 5]
li2 = [
    'Hair Dryer',
    'Ballpoint Pen',
    'Candle',
    'Grapes',
    'Butter'
]
li3 = [1, 2, 'a', True]

# Data Structure, container or carts are a good representation of a list

shopping_cart = li2
print(shopping_cart[0::])

# List slicing
li2[0] = 'Laptop'  # Changes index 0 in the shopping cart from 'Hair Dryer' to 'Laptop'
print(shopping_cart[0:len(li2):])
print(f'Your shopping cart contains {len(li2)} items.')
print()
new_cart = li2[:] # This format copies item by item from the li2 cart to new_cart
new_cart[0]= 'Peaches' # changes index 2 and replaces 'Candle' with 'Peaches'
print(f'New Cart = {new_cart}') # formatted printing of new cart
print(f'Your shopping cart contains {len(new_cart)} items.') #  cart contains # items
print()
print(f'li2 = {li2}') # formatted printing of cart li2
print(f'Your shopping cart contains {len(li2)} items.')  # cart contains # items

