"""Create a program that prints out all numbers from 1 to 20,
but skips odd numbers using one of control statements"""

# Output:
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
