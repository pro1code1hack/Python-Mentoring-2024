def cheer_for_team() -> None:
    """
    Prompt the user to enter the name of their favorite soccer team and print a cheer message.

    Returns:
    None
    """
    team_name = input("Enter the name of your favorite soccer team: ").strip()

    # Handle edge case where the user might input an empty string
    if team_name:
        print(f"{team_name} are the champions!")
    else:
        print("You didn't enter a team name.")


if __name__ == "__main__":
    cheer_for_team()
