"""Simulate an escape room challenge where the user must find
the correct code to "escape the room". 
The loop should break once the correct code is entered"""

# Input:
# Enter the escape code: 1234
# Wrong code, try again.
# Enter the escape code: 9999
# Correct! You've escaped!
# Output:
# You've successfully escaped the room!

CODE = 1431

while True:
    number = int(input("Enter the 4-digit escape code: "))
    if number != CODE:
        print("Wrong code, try again.")
        continue
    print("Correct! You've escaped!")
    break
print("You've successfully escaped the room!")
