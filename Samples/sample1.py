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




