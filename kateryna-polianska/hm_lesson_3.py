"""

Task 1: Secure Password Generator

Create an app which checks user's password and based on your rules states if it's secure or not.


Input: The user inputs a password.
Output: The program outputs whether the password is 'Strong', 'Medium', or 'Weak'.
evaluate password:
1. length (if less than 6 - weak)
2. more than 6 then:
3. symbols: if contains numbers - medium, else:
4. if contsins numbers, symbols, capital letters  - strong


Input:
Pass123!

Output:
Strong password

"""


password = input("Input password: ")
length = len(password)

if length < 7:
 print('Your password is weak')
elif '1' in password:
    print('Your password is medium')
elif '!' in password:
    print('Your password is strong')
else:
    print('Your password could be stronger') 


