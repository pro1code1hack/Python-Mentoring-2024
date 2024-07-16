# Write a program that validates if the entered string is a correct IP address.
# Note: An IP-address is considered valid if it consists of four non-negative integers separated by dots, 
# with each integer ranging from 0 to 255 inclusive.

address = input("Enter an IP-address: x.y.z.a: ")
int_in_address = [int(char) for char in address.split(".")]

if len(int_in_address) == 4:
    for num in int_in_address:
        if num < 0 or num > 255:
            print(f"The IP-address {address} is NOT valid")
            break
    else:
        print(f"The IP-adress {address} is valid")

else:
    print(f"The IP-adress {address} is NOT valid")
        
