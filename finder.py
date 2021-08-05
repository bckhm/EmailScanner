import re
import pandas as pd

# Function that searches data.txt for email/phone numbers before returning a dictionary
def find_data(pattern, column_name):
    with open('data.txt', 'r') as file:
        contents = file.read()
        matches = pattern.findall(contents)
    matches_dict = {column_name: matches}
    return matches_dict

# Function that converts aobve dictionary to excel
def save_excel(matches, filename):
    df = pd.DataFrame(data=matches)
    df.to_excel(filename)
    print(f"{filename} has been created.")

print("--- Ensure that you have copied the text into data.txt---")

# Allows users to select between fidning email addresses/phone numbers
choice = input("Type N to find phone numbers and E to find emails: ")

if re.search('n', choice, re.IGNORECASE):
    #pattern to find Singaporean phone numbers
    pattern = re.compile(r'\d{4}\s*\d{4}')
    column_name = 'Numbers'
    matches = find_data(pattern, column_name)
    save_excel(matches, 'numbers.xlsx')

if re.search('e', choice, re.IGNORECASE):
    #pattern to find email addresses that include '-', '.', '_', numbers and words
    pattern = re.compile(r'[\w._-]*@[\w._-]*\.\w+')
    column_name = 'Email Adresses'
    matches = find_data(pattern, column_name)
    save_excel(matches, 'emails.xlsx')

exit = input("\nPress any key to exit...")






