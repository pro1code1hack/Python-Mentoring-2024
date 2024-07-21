"""Develop a script that prints out a matrix of numbers, 
where each row contains numbers incremented by 1 from the previous row."""

# Input:
# Enter the number of rows: 3
# Enter the number of columns: 4
# Output:
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))
for i in range(1, rows + 1):
    for j in range(0, cols):
        print(j + i, end="")
    print("")
