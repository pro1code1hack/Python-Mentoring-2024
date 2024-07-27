def input_validator() -> None:
    """
    Continuously prompt the user to enter their age until a valid integer is provided.
    Prints the age once a valid input is received.
    """
    while True:
        user_input = input("Enter your age: ")

        try:
            age = int(user_input)
            print(f"Age entered: {age}")
            break
        except ValueError:
            print("Invalid input, please enter a number.")


if __name__ == "__main__":
    input_validator()
