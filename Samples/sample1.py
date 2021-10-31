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
