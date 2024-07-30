"""Develop a script that identifies whether a number is prime. 
Use a for else construction.
If the loop completes without breaking, the number is prime"""

# Input: Enter a number: 11
# Output: 11 is a prime number.

number = int(input("Enter a number: "))

for i in range(2, number):
    if 1 <= number <= 3:
        print(f"{number} is prime number")
        break

    if number % i == 0:
        print(f"{number} is not prime number")
        break

else:
    print(f"{number} is prime number")
