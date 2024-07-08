"""
Task 1: List Manipulator
Objective: Create a program that allows the user to manipulate a list in various ways. The user can choose to add, remove, or modify items in the list.

# Example of how the program should work

# Menu:
# 1. Add an item
# 2. Remove an item
# 3. Modify an item

# User chooses option 1:
Enter the item to add: Apple
Output: List: ['Apple']

# User chooses option 2:
Enter the item to remove: Apple
Output: List: []

# User chooses option 3:
Enter the item to modify: Apple
Enter the new item: Banana
Output: List: ['Banana']
"""

def list_manipulator():
    my_list = []
    
    while True:
        print("\nMenu:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Modify an item")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            item = input("Enter the item to add: ").strip()
            my_list.append(item)
            print(f"List: {my_list}")
        
        elif choice == "2":
            if not my_list:
                print("List is empty. Nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in my_list:
                    my_list.remove(item)
                    print(f"List: {my_list}")
                else:
                    print(f"{item} not found in the list.")
        
        elif choice == "3":
            if not my_list:
                print("List is empty. Nothing to modify.")
            else:
                item = input("Enter the item to modify: ").strip()
                if item in my_list:
                    new_item = input("Enter the new item: ").strip()
                    index = my_list.index(item)
                    my_list[index] = new_item
                    print(f"List: {my_list}")
                else:
                    print(f"{item} not found in the list.")
        
        elif choice == "4":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

"""
Task 2: Slicer and Dicer
Objective: Develop a program that allows users to input a list and then perform various slicing operations based on the user input.

Input:
Enter a list of numbers (separated by space): 10 20 30 40 50
Enter start index for slicing: 1
Enter stop index for slicing: 4

Output:
The sliced list is: [20, 30, 40]
"""
def slicer_and_dicer():
    
    input_list = input("Enter a list of numbers (separated by space): ").strip().split()
    num_list = [int(num) for num in input_list]  
    
    start_index = int(input("Enter start index for slicing: ").strip())
    stop_index = int(input("Enter stop index for slicing: ").strip())
    
    sliced_list = num_list[start_index:stop_index]
    
    print(f"The sliced list is: {sliced_list}")

"""
### Task 3: Shopping List Organizer

**Objective:**  Develop a program that helps users organize their shopping list by `adding`, `viewing`, `removing` and `sort` items alphabetically.

Additionaly, we would want to check if we add strings to the list. You can use `isinstance()` function documented [here](https://docs.python.org/3/library/functions.html#isinstance).

```python
# Example of how the program should work

# Menu:
# 1. Add item
# 2. View list
# 3. Remove item
# 4. Exit

# User Interaction Example:
Choose an action (add/view/remove/exit): add
Enter an item to add: Milk
Item added. Your current list is: ['Milk']

Choose an action (add/view/remove/exit): add
Enter an item to add: Eggs
Item added. Your current list is: ['Eggs', 'Milk']

Choose an action (add/view/remove/exit): add
Enter an item to add: 25
Sorry, it is not a string

Choose an action (add/view/remove/exit): view
Shopping List: ['Eggs', 'Milk']

Choose an action (add/view/remove/exit): remove
Enter an item to remove: Milk
Item removed. Your current list is: ['Apples']

Choose an action (add/view/remove/exit): exit
Exiting the program.

# Don't forget to check if item exists in the list using operator ``in``
"""
def movie_recommendation_system():
    movie_database = {
        "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
        "Inception": ["Action", "Adventure", "Sci-Fi"],
        "The Dark Knight": ["Action", "Crime", "Drama"],
        "The Shawshank Redemption": ["Drama"],
        "Pulp Fiction": ["Crime", "Drama"],
        "The Matrix": ["Action", "Sci-Fi"],
        "Forrest Gump": ["Drama", "Romance"],
        "The Lord of the Rings: The Fellowship of the Ring": ["Adventure", "Drama", "Fantasy"],
    }

    def recommend_movie(preferred_genres):
        recommendations = []
        for movie, genres in movie_database.items():
            if any(genre in genres for genre in preferred_genres):
                recommendations.append(movie)
        if recommendations:
            print(f"Recommended movies: {recommendations}")
        else:
            print("No movies found for the preferred genres.")

    while True:
        genres = input("Enter your preferred genres (comma-separated) or type 'exit' to quit: ").strip().lower()
        if genres == 'exit':
            print("Exiting the recommendation system.")
            break
        preferred_genres = [genre.strip().title() for genre in genres.split(",")]
        recommend_movie(preferred_genres)


"""
Task 4: Average of Evens
Objective: Generate a list of even elements using range from the input and display the average of them.

"""
def average_of_evens(start, end):
    evens = [num for num in range(start, end) if num % 2 == 0]
    if evens:
        average = sum(evens) / len(evens)
        print(f"The average of even numbers in the range [{start}, {end}) is: {average}")
    else:
        print(f"No even numbers found in the range [{start}, {end})")

# start = 1
# end = 21
# average_of_evens(start, end)


""""
Task 5: List of numbers operations
Objective: Enhance the provided code to perform the following actions on a given list:

Display the length of the list.
Print the sum, max, min and the average.
Print the last element of the list.
Output the list in reverse order (remember to use slicing).
Print "YES" if the list contains the numbers 4 and 9, and "NO" otherwise.
Show the list with the first and last elements removed (create a new list object instead).
Print the third element from the end of the list.
If the second element is > 10, replace it with 10.
"""
def list_operations(numbers):
    print(f"Length of the list: {len(numbers)}")
    
    print(f"Sum of the list: {sum(numbers)}")
    print(f"Max of the list: {max(numbers)}")
    print(f"Min of the list: {min(numbers)}")
    print(f"Average of the list: {sum(numbers) / len(numbers)}")

    print(f"Last element of the list: {numbers[-1]}")
    
    print(f"List in reverse order: {numbers[::-1]}")
    
    if 4 in numbers and 9 in numbers:
        print("YES")
    else:
        print("NO")
    
    new_list = numbers[1:-1]
    print(f"New list with first and last elements removed: {new_list}")
    
    if len(numbers) >= 3:
        print(f"Third element from the end of the list: {numbers[-3]}")
    else:
        print("List has less than 3 elements.")
    
    if len(numbers) >= 2:
        if numbers[1] > 10:
            numbers[1] = 10
            print(f"Modified list with second element replaced if > 10: {numbers}")
        else:
            print("Second element is not greater than 10.")
    else:
        print("List has less than 2 elements.")

# numbers = [3, 7, 11, 5, 8, 9, 4, 6, 12]
# list_operations(numbers)

"""
Task 6: ASCII alphabet
Objective: Write a program which creates alphabet and stores it into the list.
"""
def create_alphabet():
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    
    return alphabet

# alphabet_list = create_alphabet()
# print(alphabet_list)

"""
Task 7: Mini Database
Objective: Develop a program that stores detailed information about a person using nested lists.
"""
def store_personal_information():
    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    hobbies = input("Enter your hobbies (separated by commas): ").strip().split(',')
    favorite_foods = input("Enter your favorite foods (separated by commas): ").strip().split(',')
    
    personal_info = [name, age, hobbies, favorite_foods]
    
    return personal_info

def display_personal_information(personal_info):
    print("Personal Information:")
    print(f"Name: {personal_info[0]}")
    print(f"Age: {personal_info[1]}")
    print(f"Hobbies: {personal_info[2]}")
    print(f"Favorite Foods: {personal_info[3]}")

# personal_info = store_personal_information()
# display_personal_information(personal_info)

"""
Validating IP Addresses
Objective: Write a program that validates if the entered string is a correct IP address.

Note: An IP address is considered valid if it consists of four non-negative integers separated by dots, with each integer ranging from 0 to 254 inclusive.
"""
import re

def validate_ip_address(ip_str):
    ip_pattern = r"^((25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    
    if re.match(ip_pattern, ip_str):
        return True
    else:
        return False

ip_address = input("Enter an IP address to validate: ").strip()
if validate_ip_address(ip_address):
    print(f"{ip_address} is a valid IP address.")
else:
    print(f"{ip_address} is not a valid IP address.")

"""
Email Extractor
Objective: Create a program to extract email addresses from a block of text. The program should identify strings that resemble email addresses and separate them using semicolons.

# Input:
Enter the text: Please contact us at support@example.com or sales@example.com for assistance.

# Output:
Extracted Emails: support@example.com; sales@example.com
"""

import re

def extract_emails(text):
    email_pattern = r'[\w\.-]+@[\w\.-]+'
    
    emails = re.findall(email_pattern, text)
    
    return emails

text = input("Enter the text to extract emails from: ")
extracted_emails = extract_emails(text)

if extracted_emails:
    print("Extracted Emails:")
    for email in extracted_emails:
        print(email)
else:
    print("No email addresses found.")
