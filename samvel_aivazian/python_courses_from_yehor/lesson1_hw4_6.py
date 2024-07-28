import re
from typing import List, Dict, Callable


# Task 1: Secure Password Generator
def check_password_strength(password: str) -> str:
    """
    Check the strength of a given password.
    - Strong: Length at least 8, contains uppercase, lowercase, digit, and special character
    - Medium: Length at least 6, contains three of the four conditions for strong
    - Weak: Anything else
    """
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))

    conditions_met = sum([has_upper, has_lower, has_digit, has_special])

    if len(password) >= 8 and conditions_met == 4:
        return "Strong password"
    elif len(password) >= 6 and conditions_met >= 3:
        return "Medium password"
    else:
        return "Weak password"


# Task 2: Custom Text-based Game
def choose_path(choice: str) -> str:
    """
    Choose a path in the text-based game.
    """
    choices = {
        "forest": "You walk into the forest and find a hidden treasure chest!",
        "mountain": "You climb the mountain and enjoy a breathtaking view!"
    }
    return choices.get(choice.lower(), "Invalid choice. Please choose 'forest' or 'mountain'.")


# Task 3: Travel Itinerary Planner
def create_itinerary(cities: List[str]) -> str:
    """
    Create a travel itinerary from a list of cities.
    """
    return "Your travel itinerary: " + " -> ".join(cities)


# Handlers
def handle_password_check() -> None:
    password_input = input("Enter a password to check its strength: ")
    print(check_password_strength(password_input))


def handle_choose_path() -> None:
    choice_input = input("Choose a path (forest/mountain): ")
    print(choose_path(choice_input))


def handle_create_itinerary() -> None:
    cities_input = input("Enter cities for your travel itinerary, separated by commas: ").split(',')
    cities_input = [city.strip() for city in cities_input]
    print(create_itinerary(cities_input))


# Main function to select a task
def main() -> None:
    handlers: Dict[str, Callable[[], None]] = {
        "password_check": handle_password_check,
        "choose_path": handle_choose_path,
        "create_itinerary": handle_create_itinerary
    }

    while True:
        print("\nSelect a task:")
        print("1. Password Strength Check")
        print("2. Choose Path in Text-based Game")
        print("3. Create Travel Itinerary")
        print("4. Exit")
        task_choice = input("Enter your choice: ").strip()

        if task_choice == "1":
            handlers["password_check"]()
        elif task_choice == "2":
            handlers["choose_path"]()
        elif task_choice == "3":
            handlers["create_itinerary"]()
        elif task_choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
