import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class TextBasedGame:
    def start_game(self):
        logging.info("Welcome to the Adventure Game!")
        self.choose_path()

    def choose_path(self):
        logging.info("Choose your path (forest/mountain): ")
        choice = input().strip().lower()
        if choice == "forest":
            self.forest_path()
        elif choice == "mountain":
            self.mountain_path()
        else:
            logging.info("Invalid choice, please try again.")
            self.choose_path()

    @staticmethod
    def forest_path():
        logging.info("You walk into the forest and find a hidden treasure chest!")

    @staticmethod
    def mountain_path():
        logging.info("You climb the mountain and discover a beautiful hidden valley!")


def main():
    game = TextBasedGame()
    game.start_game()


if __name__ == "__main__":
    main()
