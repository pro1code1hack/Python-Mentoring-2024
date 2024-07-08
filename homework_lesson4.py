"""
Task 1: ASCII/Unicode Converter
Objective: Develop an application that can encrypt and decrypt multiple messages using ASCII and Unicode code points.

The program should allow the user to choose between encryption and decryption and specify the number of messages.

# Example of how the program should work

# Menu:
# 1. Encrypt Messages
# 2. Decrypt Messages

# Encrypt Input:
Enter the number of messages to encrypt: 2
Enter message 1: Hello
Enter message 2: World

# Encrypt Output:
Encrypted Message 1: 72 101 108 108 111
Encrypted Message 2: 87 111 114 108 100

# Decrypt Input:
Enter the number of messages to decrypt: 2
Enter message 1: 72 101 108 108 111
Enter message 2: 87 111 114 108 100

# Decrypt Output:
Decrypted Message 1: Hello
Decrypted Message 2: World
"""
def ascii_unicode_converter():
    def encrypt_message(message):
        return ' '.join(str(ord(char)) for char in message)

    def decrypt_message(message):
        return ''.join(chr(int(code)) for code in message.split())

    while True:
        print("\nMenu:")
        print("1. Encrypt Messages")
        print("2. Decrypt Messages")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            num_messages = int(input("Enter the number of messages to encrypt: ").strip())
            encrypted_messages = []

            for i in range(num_messages):
                message = input(f"Enter message {i + 1}: ").strip()
                encrypted_messages.append(encrypt_message(message))

            for i, encrypted_message in enumerate(encrypted_messages, 1):
                print(f"Encrypted Message {i}: {encrypted_message}")

        elif choice == "2":
            num_messages = int(input("Enter the number of messages to decrypt: ").strip())
            decrypted_messages = []

            for i in range(num_messages):
                message = input(f"Enter message {i + 1}: ").strip()
                decrypted_messages.append(decrypt_message(message))

            for i, decrypted_message in enumerate(decrypted_messages, 1):
                print(f"Decrypted Message {i}: {decrypted_message}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


"""
Task 2: The Custom String Slicer
Objective: Develop a program that allows users to input a string and then perform various slicing operations based on the user input.
Ask if the user wants to add a step and process the request accordingly

Input:
Enter a string: Hello World
Enter start index: 2
Enter stop index: 8
Do you want to add a step (yes/no)? yes
Enter step: 2

Output:
The sliced string with step is: l  o
"""
def string_slicer():
    input_string = input("Enter a string: ").strip()
    
    start_index = int(input("Enter start index: ").strip())
    stop_index = int(input("Enter stop index: ").strip())
    
    step_option = input("Do you want to add a step (yes/no)? ").strip().lower()
    
    if step_option == 'yes':
        step = int(input("Enter step: ").strip())
        result = input_string[start_index:stop_index:step]
    else:
        result = input_string[start_index:stop_index]
    
    print(f"Sliced string: {result}")

"""
Task 3: Story using f stings
Objective: Write a program that builds a story based on the user's choices. Use f strings for dynamic storytelling.

Input:
Choose your character's name: Alice
Choose a companion (dog/cat): dog
Choose a destination (forest/beach): forest

Output:
Alice, along with her loyal dog, set out on an adventure to the forest. [Continue the story...]

# Be creative! You can add more variables and sentences to the story!
"""

def vampire_adventure():
    name = input("Choose your character's name: ").strip()
    companion = input("Choose a companion (bat/wolf): ").strip().lower()
    destination = input("Choose a destination (castle/cemetery): ").strip().lower()
    
    if companion not in ["bat", "wolf"]:
        print("Invalid choice for companion. Please choose 'bat' or 'wolf'.")
        return
    if destination not in ["castle", "cemetery"]:
        print("Invalid choice for destination. Please choose 'castle' or 'cemetery'.")
        return

    story = f"{name}, along with their loyal {companion}, set out on an adventure to the {destination}."
    story += "\nAs the night grew darker, the eerie silence of the place sent shivers down their spine."
    
    if destination == "castle":
        story += f"\nThe ancient castle loomed ahead, its towers piercing the night sky. {name} felt a strange pull, drawing them closer."
        story += f"\nInside the castle, the air was thick with mystery. Suddenly, a shadow moved, revealing a powerful vampire lord."
        story += f"\n{name} and their {companion} must now find a way to escape the vampire's clutches and uncover the secrets of the castle."
    else:
        story += f"\nThe cemetery was filled with old, crumbling tombstones and the whispers of the undead."
        story += f"\n{name} noticed a crypt that seemed to emanate an otherworldly glow. Curiosity took over as they approached the crypt."
        story += f"\nInside the crypt, they discovered an ancient vampire awakening from its slumber. {name} and their {companion} must now outsmart the vampire and find a way to survive the night."
    print(story)




"""
The URL Shortener
Objective:: Develop a simple URL shortener. The program will take a URL and provide a shortened version using slicing and concatenation.

Input: Enter a URL: www.example.com
Output: Shortened URL: www.exa...com
"""

def url_shortener():
    url = input("Enter a URL: ").strip()

    url_length = len(url)

    if url_length > 10:
        beginning = url[:7]
        end = url[-3:]
        shortened_url = f"{beginning}...{end}"
    else:
        shortened_url = url
    print(f"Shortened URL: {shortened_url}")

url_shortener()
