# Input:
# Enter the escape code: 1234
# Wrong code, try again.
# Enter the escape code: 9999
# Correct! You've escaped!
# Output:
# You've successfully escaped the room!

code = 1431

while True:
    number = int(input("Enter the 4-digit escape code: "))
    if number != code:
        print ("Wrong code, try again.")
        continue
    else: 
        print ("Correct! You've escaped!")
        break
print ("You've successfully escaped the room!")
