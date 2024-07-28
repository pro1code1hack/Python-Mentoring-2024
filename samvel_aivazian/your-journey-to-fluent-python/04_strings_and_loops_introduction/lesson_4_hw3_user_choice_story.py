import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class StoryBuilder:
    def __init__(self, name, companion, destination):
        self.name = name
        self.companion = companion
        self.destination = destination

    def build_story(self):
        companion_full = "loyal dog" if self.companion == "dog" else "curious cat"
        story = (f"{self.name}, along with her {companion_full}, set out on an adventure to the {self.destination}. "
                 "They encountered many wonders and challenges, making it a journey to remember.")
        return story


def main():
    logging.info("Choose your character's name: ")
    name = input()
    logging.info("Choose a companion (dog/cat): ")
    companion = input().strip().lower()
    logging.info("Choose a destination (forest/beach): ")
    destination = input().strip().lower()

    builder = StoryBuilder(name, companion, destination)
    story = builder.build_story()
    logging.info(story)


if __name__ == "__main__":
    main()
