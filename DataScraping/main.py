# Python Requests Module - Extracting quotes manually
import requests
r = requests.get('https://quotes.toscrape.com')
# print(r.status_code)  # Prints the status code from the URL
# print(r.encoding) # Displays the site encoding
# print(r.text) # Prints the r text

html = r.text # assignment statement
with open('quotes.txt', 'w') as f: # Opens a new file called quotes.txt in write mode as f to hold our output
    for line in html.split('\n'):  # Splits string by line in for loop
        if '<span class="text" itemprop="text">' in line: # Condition to search for
        # print(line) # Will print out line including the condition
        #print(line.replace('<span class="text" itemprop="text">', '').replace('</span>', '')) # Replaces condition with empty string and prints
# The print statement allows for removing the prefix and suffix text as specified.
            line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
        # Removes all the prefix and suffix text and quotations from the line of text
            line = line.strip() # Removes all the blank space from the line of text
            f.write(line) # Writes each line of text to the file
            f.write('\n') # puts each line of text on a new line
            #print(line) # prints the line output to the screen
