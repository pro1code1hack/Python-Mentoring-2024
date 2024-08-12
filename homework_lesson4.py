"""

### Task 1: ASCII/Unicode Converter
**Objective**: Develop an application that can encrypt and decrypt multiple messages using ASCII and Unicode code points.
The program should allow the user to choose between encryption and decryption and specify the number of messages.
python
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
print('Please type 1 to Encrypt a Message')
print('Please type 2 to Decrypt a Message')
x = int(input())
if x == 1:
    word = input('Type a word ')
    for char in word:
        print(ord(word))
elif x ==2:
    word = input('Type a word ')
    for char in word:
        print(int(chr(char)))








