# Python Lists

protocolList = []  # New list

# Append
protocolList.append('ftp')
protocolList.append('ssh')
protocolList.append('smtp')
protocolList.append('http')
print(protocolList)  # Print list

# Sort
protocolList.sort()
print(protocolList)  # Print sorted list

# List type
print(type(protocolList)) # Prints list type

# Length
print(len(protocolList))  # Prints length of the list
print() # Blank line

# Position
position = protocolList.index('ssh')
print('ssh is in position '+str(position))

# Remove
protocolList.remove('ssh')
print(protocolList)

# Count
count = len(protocolList)
print('Protocol List Elements = '+str(count))
