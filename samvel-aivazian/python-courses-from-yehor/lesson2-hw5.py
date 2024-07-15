def escape_room() -> None:
    """
    Simulate an escape room game where the user must enter the correct escape code to "escape".
    """
    escape_code = "1234"  # The correct escape code

    while True:
        user_input = input("Enter the escape code (or type 'exit' to quit): ")

        if user_input == "exit":
            print("You've chosen to exit the game. Better luck next time!")
            break

        if user_input == escape_code:
            print("Correct! You've escaped!")
            break
        else:
            print("Wrong code, try again.")


if __name__ == "__main__":
    escape_room()
