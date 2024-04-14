import re

# Task 1: Secure Password Generator
def check_password_strength(password: str) -> str:
    # Strength criteria:
    # Strong: Length at least 8, contains uppercase, lowercase, digit, and special character
    # Medium: Length at least 6, contains three of the four conditions for strong
    # Weak: Anything else
    conditions_met = sum([bool(re.search(pattern, password)) for pattern in [r'[A-Z]', r'[a-z]', r'[0-9]', r'[^A-Za-z0-9]']])
    if len(password) >= 8 and conditions_met == 4:
        return "Strong password"
    elif len(password) >= 6 and conditions_met >= 3:
        return "Medium password"
    else:
        return "Weak password"

# Task 2: Custom Text-based Game
def choose_path(choice: str) -> str:
    if choice.lower() == "forest":
        return "You walk into the forest and find a hidden treasure chest!"
    elif choice.lower() == "mountain":
        return "You climb the mountain and enjoy a breathtaking view!"
    else:
        return "Invalid choice. Please choose 'forest' or 'mountain'."

# Task 3: Travel Itinerary Planner
def create_itinerary(cities: str) -> str:
    return "Your travel itinerary: " + " -> ".join(cities)


# For Task 1
password_input = "Pass123!"
print(check_password_strength(password_input))

# For Task 2
choice_input = "forest"
print(choose_path(choice_input))

# For Task 3
cities_input = ["London", "Paris", "Rome"]
print(create_itinerary(cities_input))
