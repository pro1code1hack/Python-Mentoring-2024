def story_builder() -> None:
    character_name = input("Choose your character's name: ")
    companion_type = input("Choose a companion (dog/cat): ")
    destination = input("Choose a destination (forest/beach): ")

    story = f"{character_name}, along with her loyal {companion_type}, set out on an adventure to the {destination}."

    print(story)


story_builder()
