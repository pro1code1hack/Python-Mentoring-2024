def story_builder() -> None:
    """
    Build a simple adventure story based on user inputs.
    """
    # Get user inputs for the story
    character_name = input("Choose your character's name: ")
    companion_type = input("Choose a companion (dog/cat): ")
    destination = input("Choose a destination (forest/beach): ")

    # Build the story using the inputs
    story = f"{character_name}, along with their loyal {companion_type}, set out on an adventure to the {destination}."

    # Print the constructed story
    print(story)


if __name__ == "__main__":
    story_builder()
