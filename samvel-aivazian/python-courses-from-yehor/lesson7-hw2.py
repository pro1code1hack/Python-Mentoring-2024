from typing import List, Optional, Tuple


class StoryNode:
    """
    A class representing a node in the interactive story.

    Attributes:
    narrative (str): The narrative text of the story node.
    choices (List[Tuple[str, 'StoryNode']]): A list of choices leading to the next story nodes.
    """

    def __init__(self, narrative: str, choices: Optional[List[Tuple[str, 'StoryNode']]] = None) -> None:
        """
        Initialize a StoryNode with a narrative and optional choices.

        Args:
        narrative (str): The narrative text of the story node.
        choices (Optional[List[Tuple[str, 'StoryNode']]]): A list of choices leading to the next story nodes.
        """
        self.narrative: str = narrative
        self.choices: List[Tuple[str, 'StoryNode']] = choices or []

    def add_choice(self, choice_text: str, next_node: 'StoryNode') -> None:
        """
        Add a choice to the story node.

        Args:
        choice_text (str): The text describing the choice.
        next_node ('StoryNode'): The story node that follows this choice.
        """
        self.choices.append((choice_text, next_node))


def display_node(node: StoryNode) -> Optional[StoryNode]:
    """
    Display the narrative and choices of a story node and prompt the user to make a choice.

    Args:
    node (StoryNode): The current story node.

    Returns:
    Optional[StoryNode]: The next story node based on the user's choice, or None if the story ends.
    """
    print(node.narrative)
    if not node.choices:
        print("The End.")
        return None

    for idx, (choice_text, _) in enumerate(node.choices, 1):
        print(f"{idx}. {choice_text}")

    while True:
        try:
            choice: int = int(input("Choose an option: ")) - 1
            if 0 <= choice < len(node.choices):
                return node.choices[choice][1]
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(node.choices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main() -> None:
    """
    Main function to create the story nodes and start the interactive story.
    """
    # Create story nodes
    start: StoryNode = StoryNode("You wake up in a forest. You see a path to the left and right.")
    left_path: StoryNode = StoryNode("You walk down the left path and find a river.")
    right_path: StoryNode = StoryNode("You walk down the right path and encounter a bear.")
    end: StoryNode = StoryNode("You safely reach the end of your journey.")

    # Add choices to the nodes
    start.add_choice("Take the left path", left_path)
    start.add_choice("Take the right path", right_path)
    left_path.add_choice("Swim across the river", end)
    left_path.add_choice("Walk along the river", end)
    right_path.add_choice("Run away", end)
    right_path.add_choice("Fight the bear", end)

    # Start the interactive story
    current_node: Optional[StoryNode] = start
    while current_node:
        current_node = display_node(current_node)


if __name__ == "__main__":
    main()
