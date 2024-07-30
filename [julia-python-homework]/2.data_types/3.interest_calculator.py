"""Create a script to calculate simple interest"""

principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate: "))
time_in_years = int(input("Enter the time period in years: "))

calc_interest = principal_amount * interest_rate * time_in_years / 100
print("Simple Interest is: ", calc_interest)
