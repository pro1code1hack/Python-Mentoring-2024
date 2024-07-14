class Pet:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hunger: int = 50
        self.happiness: int = 50
        self.health: int = 100

    def feed(self) -> None:
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        self.health += 5
        if self.health > 100:
            self.health = 100
        print(f"{self.name} has been fed.")

    def play(self) -> None:
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        self.hunger += 5
        self.health += 5
        if self.health > 100:
            self.health = 100
        print(f"{self.name} has played.")

    def check_status(self) -> None:
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")


def main() -> None:
    pet_name: str = input("What is the name of your pet? ")
    pet: Pet = Pet(pet_name)

    while True:
        print("\nMenu:")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check status of your pet")
        print("4. Exit")
        choice: str = input("Choose an option: ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.check_status()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
