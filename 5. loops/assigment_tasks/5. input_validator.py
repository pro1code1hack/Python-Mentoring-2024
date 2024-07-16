# Write a program that asks users to enter their age and ensures the input is valid using a while loop. 
# If the input is not a number, use continue to prompt them again until a valid number is entered.

# Input:
# Enter your age: twenty
# Invalid input, please enter a number.
# Enter your age: 20
# Output:
# Age entered: 20

while True:
  try:
    age = int(input ("Enter your age: ") )
  except:
    print("Invalid input, please enter a number.")
    continue

  print(f"Age entered: {age}")
  break


   