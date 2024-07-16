# Objective:: Write a program using nested loops to match the following output.

# Output:
# 1
# 22
# 333
# 4444
# 55555

rows = int(input("Number of rows: "))

for i in range(1, rows+1):
    for j in range(i):
        print(i, end="")
    print("")