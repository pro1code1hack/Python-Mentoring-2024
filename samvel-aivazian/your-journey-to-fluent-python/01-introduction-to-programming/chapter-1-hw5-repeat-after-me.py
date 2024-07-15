# Task 5: Repeat after me
# Objective: Create a Python program that captures three lines of text, one at a time,
# and then prints them out in reverse order.

def repeat_after_me():
    lines = []
    for _ in range(3):
        line = input()
        lines.append(line)

    for line in lines:
        print(line)


if __name__ == "__main__":
    repeat_after_me()
