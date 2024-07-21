"""Write a program which creates alphabet and stores it into the list"""

# Output
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
# 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = []
for num in range(97, 123):
    alphabet.append(chr(num))
print("Alphabet is: ", alphabet)
