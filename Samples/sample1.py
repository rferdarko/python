import threading

print('Sample 1 Test\n')

print('Python Fundamental Data Types: ')
print('int, ' + 'float, ' + 'bool, ' + 'str, ' + 'list, ' + 'tuple, ' + 'set, ' + 'dict\n')

print('Classes: ')

print('Specialized Data Types: ')

print('None: \n')

x = 2 + 4
print('2 + 4 =  ' + str(x))
print(type(6))
print(type(3.0))
print(2 ** 3)
print(5 // 3)
print(6 % 4)

# Math Functions
print(round(3.9))
print(abs(-20))
print()

# Multithreading
print('Number of threads running: ' + str(threading.active_count()))
print('Thread Name: ' + str(threading.current_thread()))
print()

# Binary Numbers - gives a binary representation of numbers.
x = bin(5)
print('Binary number for 5 is: ' + x)

# We can also achieve the same result by using
print(bin(5))
# Or
print('The binary number of 5 is: ' + bin(5))

# To convert binary to integer, we use base 2
print('The integer value of binary number 0b101 is: ' + str(int('0b101', 2)))


# Augmented Assignment Operator
# if we assign a value to an operator such as
iq = 100
print(iq)
# we can change the value by using an assignment operator such as + or - , etc...
iq += 10 # This will increase the value of iq by adding 10 to the assigned value
print(iq)
iq -= 20
print(iq)
print()

# Strings
a = str('Hi')
print(a)

# Long String
# use 3 single quotes to start and end a long string
long_string = '''
Hi
How 
Are 
you?
'''
print(long_string)

first_name = 'Robert'
last_name = 'Ferdarko'
full_name = first_name + ' ' + last_name
print(full_name)



# Escape Sequences
# The \ creates an escape sequence to tell python, everything after the \ is a string
# This allows you to use a ' or " or \ in the statement
print('It\'s kinda sunny')
print("It\'s \"kinda\" sunny")

# tab = \t
# This allows you to place a tab between elements in the statement
print('It\'s \t \"Kinda\" \t sunny')

# New Line = \n
# This injects a new line break following the \n
# Any space after the \n will be placed on the next line
print('Hello\n how are you?')
# If you eliminate the space, it will start the next line with text instead of a space character
print('Hello\nhow are you?')

# Formatted Strings
# we can create a string to greet someone with their name and age using the + to concatenate strings
name = 'Johnny'
age = 55
print('Hi ' + name + '. You are ' + str(age) + ' years old.')

# Or, we can use the f for formatted strings and place the fields in {}
print(f'Hi {name}. You are {age} years old.')
# by adding the f at the beginning it tells python this is a formatted string
# and I want to add the fields as formatted strings.

# In python 2 the .format feature was used to accomplish this as follows:
print('Hi {}. You are {} years old.'.format('Johnny', '55'))
# In this example we get rid of the f at the beginning, add .format to the end of the string
# remove the names from the brackets and add the values as strings in parenthesis to the end in order

# However, we can also use the field names in order
print('Hi {}. You are {} years old.'.format(name, age))
# This still accomplishes the task
# But
# We can also use index values for the name fields
print('Hi {0}. You are {1} years old.'.format(name, age))
# and if we reverse the indexes, this changes the output by reversing the names
print('Hi {1}. You are {0} years old.'.format(name, age))
# However, we can also add the name fields directly in the formatted string
print('Hi {new_name}. You are {new_age} years old.'.format(new_name='Sally', new_age='100'))

# While all of these methods can be used, the f at the beginning is the cleanest method
print()

# String slicing
selfish = '01234567'
print(selfish)  # Prints the entire string
# print(selfish[start:finish]) will print the string between the start and finish points
print(selfish[1:4]) # prints 1 through 3 because the endpoint is exclusive
print(selfish[1:]) # tells python to print character 1 to the end of the string
print(selfish[:5]) # prints from 0 to 5 exclusive)
print()

# The next topic is called stepover or string slicing
# print(selfish[start:finish:stepover])
# if we use a stepover of 1, it prints the whole string
print(selfish[0:8:1]) # whole string prints
print(selfish[0:8:2]) # steps over by 2 characters in the string
print(selfish[0:8:3]) # steps over by 3
print()

# prints from the end
print(selfish[-1])
print(selfish[::-1]) # will print in reverse - quite a popular method
print(selfish[::-2]) # same reverse printing, but skip by 2
