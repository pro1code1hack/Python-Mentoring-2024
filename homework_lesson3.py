"""

#### Task 1: Secure Password Generator
**Objective**: Create an app which checks user's password and based on your rules states if it's secure or not.

Input: The user inputs a password.
Output: The program outputs whether the password is 'Strong', 'Medium', or 'Weak'.
Input:
Pass123!
evaluate password
1 lenght (moer then 6
more then 6
symbols if containse number

Output:

Strong password


password=input('Please provide your pasword:')
length = len(password)
if length < 7:
    print('Your password is weak')
else:
    if '1' in password:
        print('Your password is medium')
    else:
        if '!' and '1' in password:
            print('Your password is strong')
"""




password = input('Please type a password')
length = len(password)
if length > 7:
    print('week')
else:
    if '!' in password:
        print('MEDIUM')
    else:
     if '!' in password:
        print('STRONG')



print(password)

