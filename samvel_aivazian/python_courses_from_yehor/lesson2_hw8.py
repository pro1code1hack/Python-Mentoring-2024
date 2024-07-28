def custom_string_slicer() -> None:
    """
    Allows the user to input a string and slice it using start, stop, and optional step indices.
    """
    user_string = input("Enter a string: ")

    # Get start and stop indices for slicing
    start_index = int(input("Enter start index: "))
    stop_index = int(input("Enter stop index: "))

    # Check if the user wants to add a step to the slicing
    add_step = input("Do you want to add a step (yes/no)? ").strip().lower() == 'yes'

    if add_step:
        step = int(input("Enter step: "))
        sliced_string = user_string[start_index:stop_index:step]
    else:
        sliced_string = user_string[start_index:stop_index]

    # Display the result
    print(f"The sliced string{' with step' if add_step else ''} is: {sliced_string}")


if __name__ == "__main__":
    custom_string_slicer()
