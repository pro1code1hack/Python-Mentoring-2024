def escape_room() -> None:
    escape_code = "1234"

    while True:
        user_input = input("Enter the escape code: ")

        if user_input == escape_code:
            print("Correct! You've escaped!")
            break
        else:
            print("Wrong code, try again.")


escape_room()
