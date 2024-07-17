"""Write a program that simulates a menu navigation
system using a while loop and break statement
The user can select from a list of options, and the loop terminates
when the user selects the 'Exit' option."""

print("1. Start Game")
print("2. Load Game")
print("3. Exit")

option = int(input("Choose your option: 1, 2, or 3: "))

MESSAGE = ""

if option == 1:
    MESSAGE = "Starting a game..."
elif option == 2:
    MESSAGE = "Loading..."
elif option == 3:
    MESSAGE = "Exiting the menu..."

COUNT = 0
while True:
    COUNT += 1
    if COUNT == option:
        print(MESSAGE)
        break

## Why option can be lowercase but message and count have to be uppercase?
