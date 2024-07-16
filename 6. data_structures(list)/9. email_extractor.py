# Create a program to extract email addresses from a block of text. 
# The program should identify strings that resemble email addresses and separate them using semicolons.

# Input:
# Enter the text: Please contact us at support@example.com or sales@example.com for assistance.

# # Output:
# Extracted Emails: support@example.com; sales@example.com

text = input("Enter the text: ")

emails = []
for word in text.split(" "):
    if "@" in word:
        emails.append(word)

print("Extracted Emails:", "; ".join(emails))