"""
Task 1: Safe Division

Create a function safe_divide that safely performs division and handles any division errors gracefully.

"""

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    else:
        return result
    finally:
        print("Division attempt completed")

# Example usage
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(5, 0))   # Output: Error: Cannot divide by zero

"""
Task 2: Voting

Implement a function check_voter_age that checks if a person is eligible to vote and raises an exception if the age is below the minimum voting age.


"""

def check_voter_age(age):
    if age < 18:
        raise ValueError("You are too young to vote.")
    else:
        print("You are allowed to vote.")

# Test the function with different ages
def main():
    ages_to_test = [21, 16, 18, 17]

    for age in ages_to_test:
        try:
            check_voter_age(age)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
