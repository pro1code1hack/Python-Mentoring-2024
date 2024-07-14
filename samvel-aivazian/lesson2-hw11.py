import time


def countdown_timer() -> None:
    """
    Simulate a countdown timer for a bomb with a wire-cutting decision at the end.
    """
    try:
        countdown_time = int(input("Enter the countdown time in seconds: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print(f"The bomb will explode in {countdown_time} seconds!")

    for i in range(countdown_time, 0, -1):
        print(i)
        time.sleep(1)

    wire_choice = input("Quick! Which wire to cut? Red or Blue? ").strip().lower()

    if wire_choice == 'blue':
        print("You cut the blue wire...")
        print("The bomb has been defused. Congratulations, you saved the day!")
    elif wire_choice == 'red':
        print("You cut the red wire...")
        print("BOOM!!! The bomb exploded.")
    else:
        print("Invalid choice, the bomb exploded!")


if __name__ == "__main__":
    countdown_timer()
