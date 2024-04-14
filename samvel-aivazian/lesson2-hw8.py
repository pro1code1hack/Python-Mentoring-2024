def custom_string_slicer() -> None:
    user_string = input("Enter a string: ")
    start_index = int(input("Enter start index: "))
    stop_index = int(input("Enter stop index: "))

    add_step = input("Do you want to add a step (yes/no)? ").lower() == 'yes'
    if add_step:
        step = int(input("Enter step: "))
        sliced_string = user_string[start_index:stop_index:step]
    else:
        sliced_string = user_string[start_index:stop_index]

    print(f"The sliced string{' with step' if add_step else ''} is: {sliced_string}")

custom_string_slicer()