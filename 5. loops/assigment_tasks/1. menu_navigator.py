# Write a program that simulates a menu navigation system using a while loop and break statement.
# The user can select from a list of options, and the loop terminates when the user selects the 'Exit' option.

print ("1. Start Game") 
print ("2. Load Game")
print("3. Exit")

option = int (input ("Choose your option: 1, 2, or 3: "))

message = ""

if option == 1:
    message = "Starting a game..."
elif option == 2:
    message = "Loading..."
elif option == 3:
    message = "Exiting the menu..."

count = 0
while True:
    count += 1
    if count == option:
        print (message)
        break
