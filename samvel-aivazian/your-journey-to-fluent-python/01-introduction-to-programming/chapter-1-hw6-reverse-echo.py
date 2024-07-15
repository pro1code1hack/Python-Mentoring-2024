# Task 6: Reverse Echo
# Objective: Write a Python program that takes in three separate lines of text
# and then prints them out in reverse order.

def reverse_echo():
    lines = []
    for _ in range(3):
        line = input()
        lines.append(line)

    for line in reversed(lines):
        print(line)


if __name__ == "__main__":
    reverse_echo()
