#Create an app which checks user's password and based on your rules states if it's secure 
import re

password = input('Enter your password: ')

if len(password) >= 8 and re.search(r'\d', password):
 print('Strong password')

elif len(password) >= 8:
 print('Medium password')
 
else: 
 print('Weak password')