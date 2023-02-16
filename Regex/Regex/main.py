import re

def menu():
    print("-----------------------------------------Menu-----------------------------------------")
    print("1 - Findall(Returns a list containing all matches)")
    print("2 - Search(Returns a Match object if there is a match anywhere in the string)")
    print("3 - Split(Returns a list where the string has been split at each match)")
    print("4 - Sub(Replaces one or many matches with a string)")
    print("5 - Exit")
    choice = input("Enter your choice: ")
    return choice

while True:
    choice = menu()
    if choice == '1':
        regex = input("Enter a regex pattern: ")
        text = input("Enter a text to search: ")
        matches = re.findall(regex, text)
        print(matches)
    elif choice == '2':
        regex = input("Enter a regular expressions pattern: ")
        text = input("Enter a text to search: ")
        match = re.search(regex, text)
        if match:
            print("Match found:", match.group())
        else:
            print("No match found")
    elif choice == '3':
        regex = input("Enter a regular expressions pattern: ")
        text = input("Enter a text to split: ")
        splitted = re.split(regex, text)
        print(splitted)
    elif choice == '4':
        regex = input("Enter a regular expressions pattern: ")
        replace = input("Enter a replacement text: ")
        text = input("Enter a text to substitute: ")
        replaced = re.sub(regex, replace, text)
        print(replaced)
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again")
