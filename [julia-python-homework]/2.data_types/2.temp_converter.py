"""Write a program that converts a temperature from Fahrenheit to Celsius"""

temp_fh = float(input("Enter temperature in Fahrenheit: "))
temp_c = (temp_fh - 32) * 5 / 9
print(temp_c, "Celsius")
