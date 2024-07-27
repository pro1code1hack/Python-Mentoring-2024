import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.health = 50

    def feed(self):
        self.hunger -= 10
        self.health += 5
        self.check_status()

    def play(self):
        self.happiness += 10
        self.health += 5
        self.check_status()

    def check_status(self):
        logging.info(f"Pet Name: {self.name}")
        logging.info(f"Hunger: {self.hunger}")
        logging.info(f"Happiness: {self.happiness}")
        logging.info(f"Health: {self.health}")


class Menu:
    def __init__(self, pet):
        self.pet = pet

    def display_menu(self):
        while True:
            logging.info("\nMenu:")
            logging.info("1. Feed the pet")
            logging.info("2. Play with the pet")
            logging.info("3. Check pet status")
            logging.info("4. Exit")
            logging.info("Choose an action: ")
            choice = input().strip()

            if choice == '1':
                self.pet.feed()
            elif choice == '2':
                self.pet.play()
            elif choice == '3':
                self.pet.check_status()
            elif choice == '4':
                break
            else:
                logging.info("Invalid choice, please try again.")


if __name__ == "__main__":
    logging.info("Welcome to the Pet Simulator!")
    logging.info("Enter the name of your pet: ")
    pet_name = input().strip()
    pet = Pet(pet_name)
    menu = Menu(pet)
    menu.display_menu()
