from typing import List, Optional, Tuple


class StoryNode:
    def __init__(self, narrative: str, choices: Optional[List[Tuple[str, 'StoryNode']]] = None) -> None:
        self.narrative: str = narrative
        self.choices: List[Tuple[str, 'StoryNode']] = choices or []

    def add_choice(self, choice_text: str, next_node: 'StoryNode') -> None:
        self.choices.append((choice_text, next_node))


def display_node(node: StoryNode) -> Optional[StoryNode]:
    print(node.narrative)
    if not node.choices:
        print("The End.")
        return None

    for idx, (choice_text, _) in enumerate(node.choices, 1):
        print(f"{idx}. {choice_text}")
    choice: int = int(input("Choose an option: ")) - 1
    return node.choices[choice][1]


def main() -> None:
    start: StoryNode = StoryNode("You wake up in a forest. You see a path to the left and right.")
    left_path: StoryNode = StoryNode("You walk down the left path and find a river.")
    right_path: StoryNode = StoryNode("You walk down the right path and encounter a bear.")
    end: StoryNode = StoryNode("You safely reach the end of your journey.")

    start.add_choice("Take the left path", left_path)
    start.add_choice("Take the right path", right_path)
    left_path.add_choice("Swim across the river", end)
    left_path.add_choice("Walk along the river", end)
    right_path.add_choice("Run away", end)
    right_path.add_choice("Fight the bear", end)

    current_node: Optional[StoryNode] = start
    while current_node:
        current_node = display_node(current_node)


if __name__ == "__main__":
    main()
