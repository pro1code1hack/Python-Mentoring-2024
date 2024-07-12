def input_validator() -> None:
    while True:
        user_input = input("Enter your age: ")

        try:
            age = int(user_input)
            print(f"Age entered: {age}")
            break
        except ValueError:
            print("Invalid input, please enter a number.")


input_validator()
