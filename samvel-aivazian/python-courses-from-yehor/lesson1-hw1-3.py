from typing import List, Tuple


# Assignment 1: Interval Membership
def find_shortest_longest_cities(cities: List[str]) -> Tuple[str, str]:
    """Find the shortest and longest city names in the given list."""
    # Sort the cities based on their length
    sorted_cities = sorted(cities, key=len)
    # The shortest city name will be the first and the longest will be the last
    return sorted_cities[0], sorted_cities[-1]


# Assignment 2: Resting Query
def contains_weekend_day(text: str) -> str:
    """Check if the text contains 'Saturday' or 'Sunday'."""
    # Check if "Saturday" or "Sunday" is in the text using a ternary operator
    return "YES" if "Saturday" in text or "Sunday" in text else "NO"


# Assignment 3: Validating an Email Address
def is_valid_email(email: str) -> str:
    """Validate if the given email address contains '@' and '.'."""
    # Check for the presence of '@' and '.' using a ternary operator
    return "YES" if "@" in email and "." in email else "NO"


# For assignment 1
cities = ["Tokyo", "New York", "Delhi"]
shortest, longest = find_shortest_longest_cities(cities)
print(f"The shortest city name is: {shortest}")
print(f"The longest city name is: {longest}")

# For assignment 2
text = "I will rest on Saturday."
print(f"Does the text contain a weekend day? {contains_weekend_day(text)}")

# For assignment 3
email = "example@example.com"
print(f"Is the email address valid? {is_valid_email(email)}")
