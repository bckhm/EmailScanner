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


# Dictionary that gives varying patterns. column names and file names based on user input
choice_dict = {'e': [r'[\w._-]*@[\w._-]*\.\w+', 'Email Addresses', 'emails.xlsx'], 'n': [r'\d{4}\s*\d{4}', 'Numbers', 'numbers.xlsx']}

try:
    # Allows users to select between finding email addresses/phone numbers
    choice = input("Type N to find phone numbers and E to find emails: ")
    choice_lower = choice.lower()
    pattern = re.compile(choice_dict[choice_lower][0])
except KeyError as e:
    print(f"You typed {e}, that's not 'E' or 'N'!")
except Exception:
    print("Something went wrong")
else:
    matches = find_data(pattern, choice_dict[choice_lower][1])
    save_excel(matches, choice_dict[choice_lower][2])
finally:
    exit = input("Press Enter key to exit...")








