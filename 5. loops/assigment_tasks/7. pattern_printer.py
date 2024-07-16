# Create a program that prints out a pattern of stars, forming a right-angled triangle

# Input: 
# Enter the number of rows for the triangle: 5
# Output:
# *
# **
# ***
# ****
# *****

rows = int(input("Number of rows: "))

for i in range(rows):
    for j in range(i + 1):
      print("*", end="")
    print("")
    