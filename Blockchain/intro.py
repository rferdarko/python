# This example creates a file, requests user input, writes it to the file and prints to the screen

my_name = input('Please enter your name: ')  # Requests user input and assigns it to my_name variable
file = open('name.txt' , mode='w') # creates a name.txt file in write mode
file.write(my_name) # writes mt_name variable content to the name.txt file
file.close() # closes the file
file = open('name.txt' , mode='r') # opens name.txt file in read mode
content = file.read() # reads file and assigns data to content variable
print(content) # prints content if the file from the content assignment

