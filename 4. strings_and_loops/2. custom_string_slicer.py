# Develop a program that allows users to input a string and then perform various slicing operations based on the user input.

#Input:
#Enter a string: Hello World
#Enter start index: 2
#Enter stop index: 8
#Do you want to add a step (yes/no)? yes
#Enter step: 2
#Output:
#The sliced string with step is: loW

main = input("Enter a string: ")
start_index = int(input("Enter a start index: "))
last_index = int(input("Enter a last index: "))
step = input("Do you want to add a step? (yes/no): ")

if step == "no": 
    print (f"The sliced string is: {main[start_index : last_index]}")
elif step == "yes":
    step_count = int(input("Enter step: "))
    print (f"The sliced string with a step is: {main[start_index : last_index: step_count]}")
