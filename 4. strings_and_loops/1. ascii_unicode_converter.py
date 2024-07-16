# Develop an application that can encrypt and decrypt multiple messages using ASCII and Unicode code points

# Example of how the program should work
# Menu:
# 1. Encrypt Messages
# 2. Decrypt Messages
# Encrypt Input:
#Enter the number of messages to encrypt: 2
#Enter message 1: Hello
#Enter message 2: World
# Encrypt Output:
#Encrypted Message 1: 72 101 108 108 111
#Encrypted Message 2: 87 111 114 108 100
# Decrypt Input:
#Enter the number of messages to decrypt: 2
#Enter message 1: 72 101 108 108 111
#Enter message 2: 87 111 114 108 100
# Decrypt Output:
#Decrypted Message 1: Hello
#Decrypted Message 2: World

purpose = input("Choose method (encrypt/decrypt): ")
count = int(input(f"Number of messages to {purpose}: "))

for indexCount in range(1, count + 1):
    message = input(f"Enter Message {indexCount}: ")

    if purpose == "encrypt":
        enctypted_message = []
        for char in message:
            enctypted_message.append(ord(char))
        print(f"Encrypted Message {indexCount}: {' '.join(str(x) for x in enctypted_message)}") 

    if purpose == "decrypt": 
        dectypted_message = []
        for num in message.split():
           dectypted_message.append(chr(int(num)))
        print(f"Decrypted Message {indexCount}: {''.join(dectypted_message)}")

           