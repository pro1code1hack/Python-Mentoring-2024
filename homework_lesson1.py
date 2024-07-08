"""
###Task 4: My favourite football team

**Objective**: Write a Python program that asks for the name of a soccer team and then prints a cheer for that team.

**Requirements**:
The program should take the name of the soccer team as input.
It should then output the name of the team followed by the cheer "are the champions!".
Example:

# Sample Input
Barcelona

# Sample Output
Barcelona is a champion!
"""

def cheer_for_team():
    team_name = input("Enter the name of a soccer team: ")
    print(f"{team_name} are the champions!")


"""
Task 5: Repeat after me
Objective: Create a Python program that captures three lines of text, one at a time, and then prints them out in reverse order.

# Sample Input

I love
Python
so much

# Sample Output

I love
Python
so much

"""

def repeat_after_me():
    text_1 = input("Input first string: ")
    text_2 = input("Input second string: ")
    text_3 = input("Input third string: ")
    print(f"{text_1}\n{text_2}\n{text_3}")


"""
Task 6: Reverse Echo
Objective: Write a Python program that takes in three separate lines of text and then prints them out in reverse order.

# Sample Input

I love
Python
so much

# Sample Output

so much
Python
I love
"""

def reverse_echo():
    text_1 = input("Input first string: ")
    text_2 = input("Input second string: ")
    text_3 = input("Input third string: ")
    reverse_text1 = "".join(reversed(text_1))
    reverse_text2 = "".join(reversed(text_2))
    reverse_text3 = "".join(reversed(text_3))
    print(f"{reverse_text1}\n{reverse_text2}\n{reverse_text3}")

reverse_echo()