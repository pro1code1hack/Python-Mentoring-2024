"""
Task 1: Pet Simulator

Create a virtual pet simulator where users can adopt a pet, feed it, play with it, and monitor its health and happiness.

#### Requirements:
- Implement a `Pet` class with attributes for `name`, `hunger`, `happiness`, and `health`.
- Include methods to `feed`, `play`, and `check_status` of the pet. Feeding decreases hunger, playing increases happiness, and both actions affect health.
- Create a simple user interface in the console to interact with the pet. (Try even using classes for `Menu` in the console itself)
"""


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.health = 5
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
            self.health += 1
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is not hungry.")
    def play(self):
        if self.happiness < 10:
            self.happiness += 1
            self.health += 1
            print(f"{self.name} is playing.")
        else:
            print(f"{self.name} is already very happy.")
    def check_status(self):
        print(f"Status of {self.name}:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
class Menu:
    def __init__(self, pet):
        self.pet = pet
    def display(self):
        while True:
            print("\n1. Feed Pet")
            print("2. Play with Pet")
            print("3. Check Pet Status")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.pet.feed()
            elif choice == '2':
                self.pet.play()
            elif choice == '3':
                self.pet.check_status()
            elif choice == '4':
                print("Exiting the game.")
                break
            else:
                print("Invalid choice. Please try again.")
def main():
    pet_name = input("What is your pet's name? ")
    pet = Pet(pet_name)
    menu = Menu(pet)
    menu.display()
if __name__ == "__main__":
    main()
