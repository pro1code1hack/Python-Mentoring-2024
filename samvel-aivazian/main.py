
# print('We are learning Python!')  
# print(type('We are learning Python!'))      # <class 'str'>

# if --> 


# How to define good vars
# 1. Sensible meaning
# 2. Match the Context
# 3. Not complicaten (KISS--> keep it simple, stupid)


# Use Snake Case

# assigment (=) 

string1 = 'We are learning Python!'         # Bad approach
output_text = 'We are learning Python!'     # Bad approach
greeting = 'We are learning Python!'


# Docstring
"""
!!!!Interactive!!!!
"""

# name = input('Input ')    Single comment


"""

\n	Newline - moves to the next line
\t	Horizontal Tab - adds a tab space
\\	Backslash - to use a backslash itself
\'	Single Quote
\"	Double Quote
"""

# print("This is a line.And this is another line.")
# print("This is a line.\nAnd this is another line.")

# print("Name:\tJohn")
# print("Path to the folder: C:\\Users\\John")


# print(
#     """
#     \n	Newline - moves to the next line
#     \t	Horizontal Tab - adds a tab space
#     \\	Backslash - to use a backslash itself
#     \'	Single Quote
#     \"	Double Quote
# """
# )

# # 2 Options how to define a string in Python

# single_quote_str = 'It is John \'s'   
# double_quote_str = "It is John's car"

# print(single_quote_str)
# print(double_quote_str)


# s = '''
# Hello it is a 
#             very very 
# big text
# '''

# print(s)


# # Data Types 

# # 1. Integer

# number_of_apples = 5
# my_age = 22

# print("Number of apples = ", number_of_apples)
# print(type(number_of_apples))


# # 2. Float

# apple_price = 0.01 + 0.01

# print("Apple price:", apple_price, "pounds")
# print("Type of apple_price variable:", type(apple_price))

# # 3. Decimal / Money    


# # Data Operations
# num1 = 15
# num2 = 4

# # Operations
# sum_result = num1 + num2
# difference_result = num1 - num2
# division_result = num1 / num2
# integer_division_result = num1 // num2
# exponentiation_result = num1 ** num2
# modulo_result = num1 % num2

# # Displaying the results
# print("Addition of", num1, "and", num2, "=", sum_result)
# print("Subtraction of", num1, "from", num2, "=", difference_result)
# print("Division of", num1, "by", num2, "=", division_result)
# print("Integer division of", num1, "by", num2, "=", integer_division_result)
# print("Exponentiation of", num1, "to the power of", num2, "=", exponentiation_result)
# print("Modulo of", num1, "by", num2, "=", modulo_result)


# # 4. Boolean Examples
# is_student = True
# is_weekend = False

# print("Is student:", is_student)
# print("Is it the weekend:", is_weekend)



# 1. Offical python docs / Chatgp

# dir() -> 
# help()

# If you need to check any funciton
# print(dir(input))


# Asking the user to input their age and converting it into the integer 
# age= int(input("Please enter your age: "))

# print("Type of age is: ", type(age))
# print("You are", age, "years old.")


# Data Type Conversion

# number = '11'

# # Carefult with re-assigments
# print(type(number))
# print(number)   
# print(int(number))      # Не переписывает 
# print(type(number))


# # Explicitly call and REDEFINE VARIABLES 
# number = int(number)     # Перезаписали и сохранили переменную
# new_str = str(number)    # Convert the string 
# new_float = float(number)


# ### STRING VERY ATTENTIVE

# num1 = 1234
# str1 = str(num1)        # Convert to string         str(1234) == same

# str1 = 'A'
# # num1 = int(str1)        # ValueError


# # Can't substract strings from each other
# # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# salary_str = "1000"
# tax_str = "200"

# print(salary_str - tax_str)


# var_1 = int(input('Variable 1\n'))
# var_2 = int(input('Variable 2\n'))
# var_sum = var_1 + var_2
# var_sub = var_1 - var_2
# print("Sum is = ", var_sum)
# print("Subtraction is = ", var_sub)



## Conditionals

"""
Operator	Description	Example	Result
>	Greater than	5 > 3	True
<	Less than	5 < 3	False
==	Equal to	5 == 5	True
!=	Not equal to	5 != 3	True
>=	Greater than or equal to	5 >= 5	True
<=	Less than or equal to	5 <= 3	False
"""


num1 = 11
num2 = 22

x = num1        # Makes a copy of num 11


print(num1 == x)
print(num1 is x)


str1 = '11'
str2 = 'abc'


# `IS` -> checks the object in MEMORY SPACE (IT SHOULD MATCH THE SAME ADRESS)
# `==` -> checks the equality of both objects 


# day = 'MONDAY'
# date = 11

# # 1. Leave as its 
# if day == 'MONDAY':
#     print("SLAVE")


# # Option #1 
# if day == 'MONDAY':
#     print("SLAVE")

# if day == 'Wednesday':
#     print("WEEKLY CALL")

# if day == 'Saturday':
#     print("SLEEP")


# # Option #2 (NESTED CONDITIONAL LOGIC)
# if day == 'MONDAY':
#     print("SLAVE")
#     if date == 11:
#         print("asdasd")
# elif day == 'Wednesday':
#     print("WEEKLY CALL")
# elif day == 'Saturday':
#     print("SLEEP")
# else:
#     print('What day is it?')


# """
# and	True if both the operands are true	5 < 10 and 3 > 1	True
# or	True if at least one of the operands is true	5 < 3 or 3 > 1	True
# not	True if operand is false (complements the operand)	not(5 < 3)	True
# """

# day = 'Wednesday'
# date = 8 
# month = 'March'

# if day == 'Wednesday' and date == 8 and month == 'March':
#     print("Dear women! With international women day!")


result = not True and (not 5 > 3 and 3 < 2 or 5 != 4) and (5 < 3)


# result = not 5 > 3 and 3 < 2 or 5 != 4

# Breakdown:
# 1. not 5 > 3 evaluates to False       False and 3 < 2 or 5 != 4
# 2. 3 < 2 evaluates to False           False and False or True
# 3. 5 != 4 evaluates to True
# Final result: False and False or True, which evaluates to True

print(result)  # Output: True


# F string


greetings = 'hello'
name = 'test'

print(f"Dear {name}, say {greetings}!")

# Define the map of the game
game_map = {
    1: [5],  # Room 1 is connected to Room 5
    2: [5],  # Room 2 is connected to Room 5
    3: [5],  # Room 3 is connected to Room 5
    4: [5],  # Room 4 is connected to Room 5
    5: [1, 2, 3, 4]  # Room 5 is connected to Rooms 1, 2, 3, and 4
}

def get_connected_rooms(room_id):
    """
    Get a list of rooms that can be entered from the given room.

    :param room_id: ID of the current room
    :return: List of connected room IDs
    """
    # Check if the room exists in the map
    if room_id in game_map:
        return game_map[room_id]
    else:
        return []  # Return an empty list if the room doesn't exist

# Example Usage
current_room = 5
available_rooms = get_connected_rooms(current_room)
print(f"From room {current_room}, you can enter rooms: {available_rooms}")

graph = {
    '1': {'2': 1}, # Комната 1 соединена с комнатой 2
    '2': {'3': 1, '1': 1}, # Комната 2 соединена с комнатами 1 и 3
    '3': {'4': 1, '2': 1}, # Комната 3 соединена с комнатами 2 и 4
    '4': {'5': 1, '3': 1}, # Комната 4 соединена с комнатами 3 и 5
    '5': {'1': 1, '4': 1, '2': 1, '3': 1} # Центральная комната 5 соединена со всеми другими
}

# Вес каждого перехода по умолчанию равен 1