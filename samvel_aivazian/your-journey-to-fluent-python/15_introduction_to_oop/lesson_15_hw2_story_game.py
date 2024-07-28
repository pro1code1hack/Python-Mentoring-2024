import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class StoryNode:
    def __init__(self, narrative, choices):
        self.narrative = narrative
        self.choices = choices

    def display_node(self):
        logging.info(self.narrative)
        for index, choice in enumerate(self.choices):
            logging.info(f"{index + 1}. {choice['text']}")

    def get_next_node(self):
        self.display_node()
        if not self.choices:
            return None
        logging.info("Choose an option: ")
        try:
            choice = int(input().strip()) - 1
            if 0 <= choice < len(self.choices):
                return self.choices[choice]['next_node']
            else:
                logging.info("Invalid choice, please try again.")
                return self
        except ValueError:
            logging.info("Invalid input, please enter a number.")
            return self


if __name__ == "__main__":
    end_node = StoryNode("The End. Thanks for playing!", [])
    node3 = StoryNode("You enter a dark cave and find a treasure!",
                      [{'text': 'Take the treasure', 'next_node': end_node}])
    node2 = StoryNode("You climb a mountain and see a beautiful sunrise.",
                      [{'text': 'Enjoy the view', 'next_node': end_node}])
    start_node = StoryNode("You are on an adventure. Do you want to go to the cave or climb the mountain?", [
        {'text': 'Go to the cave', 'next_node': node3},
        {'text': 'Climb the mountain', 'next_node': node2}
    ])

    current_node = start_node
    while current_node:
        next_node = current_node.get_next_node()
        if next_node is None:
            break
        current_node = next_node
