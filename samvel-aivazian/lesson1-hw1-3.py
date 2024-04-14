# Assignment 1: Interval Membership
def find_shortest_longest_cities(cities: list[str]) -> list[str]:
    # Sort the cities based on their length
    sorted_cities = sorted(cities, key=len)
    # The shortest city name will be the first and the longest will be the last
    return sorted_cities[0], sorted_cities[-1]

# Assignment 2: Resting Query
def contains_weekend_day(text: str) -> str:
    # Check if "Saturday" or "Sunday" is in the text
    if "Saturday" in text or "Sunday" in text:
        return "YES"
    else:
        return "NO"

# Assignment 3: Validating an Email Address
def is_valid_email(email: str) -> str:
    # Check for the presence of '@' and '.'
    if "@" in email and "." in email:
        return "YES"
    else:
        return "NO"


# For assignment 1
cities = ["Tokyo", "New York", "Delhi"]
shortest, longest = find_shortest_longest_cities(cities)
print(shortest)
print(longest)

# For assignment 2
text = "I will rest on Saturday."
print(contains_weekend_day(text))

# For assignment 3
email = "example@example.com"
print(is_valid_email(email))
