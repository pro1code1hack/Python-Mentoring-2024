
"""
###Assignment 1: Interval Membership

**Objective**: Write a program that takes an integer `x` and determines whether `x` falls within specified intervals.

```
Input:
One integer: the value of `x`.

Output:
The program should output text in accordance with the task's condition.

Example: If the intervals are -3 to 7 (inclusive), and the user enters 5, the output should be 'The number 5 belongs to the interval [-3, 7]'.
```

"""
def shortest_and_longest_city_names():
    city1 = input("Enter the first city name: ")
    city2 = input("Enter the second city name: ")
    city3 = input("Enter the third city name: ")

    cities = [city1, city2, city3]
    shortest = min(cities, key=len)
    longest = max(cities, key=len)

    print("Shortest city name:", shortest)
    print("Longest city name:", longest)



"""
#### Assignment 2: Resting Query

**Objective:** Create a program that reads a single line of text and then decides if the text suggests resting.

```
Input:
A single line of text.

Output:
The program should output "YES" if the line contains the word "Saturday" or "Sunday", and "NO" otherwise.
```

"""
def resting_query():
    text = input("Enter a line of text: ")
    if "Saturday" in text or "Sunday" in text:
        print("YES")
    else:
        print("NO")


"""
#### Assignment 3:  Validating an Email Address

**Objective:** Write a program that checks if an email address is correct, assuming correctness requires the presence of the `'@'` symbol and a `.`

```
Input:
A single line containing an email address.

Output:
The program should print "YES" if the email address is considered correct, and "NO" otherwise.

Note: The presence of symbols '@' and '.' is necessary for an email address to be correct, but their absence does not guarantee the address is incorrect.
```
"""
def validate_email():
    email = input("Enter an email address: ")
    if '@' in email and '.' in email:
        print("YES")
    else:
        print("NO")


"""
Task 1: Secure Password Generator
Objective: Create an app which checks user's password and based on your rules states if it's secure or not.

Input: The user inputs a password.
Output: The program outputs whether the password is 'Strong', 'Medium', or 'Weak'.

Input:
Pass123!

Output:
Strong password
"""
import re

def secure_password():
    password = input("Input password for secure check: ")
    pattern = r'[!@#$%^&()\-_=,<>/]'
    
    special_symbols = bool(re.search(pattern, password))
    has_digit = any(char.isdigit() for char in password)
    has_alpha = any(char.isalpha() for char in password)
    length = len(password)
    
    if has_digit and has_alpha and special_symbols and length >=8:
        print(f"{password} is strong!")
    elif has_digit and has_alpha and length >=8:
        print(f"{password} is medium!")
    else:
        print(f"{password} is weak!")

"""
Task 2: Custom Text-based Game
Objective: Develop an interactive game with a mini plot twist.

Input: The user makes choices at story junctures.
Output: The program narrates the consequence of the choices, leading to a unique story ending.

Choose your path (forest/mountain):
>> forest

Output:
You walk into the forest and find a hidden treasure chest!
"""

def samurai_adventure():
    print("Welcome, noble samurai. Your journey begins now.")
    print("Choose your path (forest/mountain):")
    path = input(">> ").strip().lower()

    if path == "forest":
        print("\nYou walk into the forest, the sound of rustling leaves and chirping birds filling the air.")
        print("As you navigate through the dense trees, you come across an ancient shrine hidden among the foliage.")
        print("Do you (1) explore the shrine or (2) continue deeper into the forest?")
        choice = input(">> ").strip()

        if choice == "1":
            print("\nYou approach the shrine and kneel in reverence. As you do, a hidden compartment opens, revealing a mystical katana.")
            print("This blade is said to possess extraordinary power. Do you (1) take the katana or (2) leave it?")
            katana_choice = input(">> ").strip()

            if katana_choice == "1":
                print("\nYou take the katana and feel its power coursing through you. With this new strength, you are destined to become a legendary warrior.")
                print("The spirit of the forest watches over you as you continue your journey, now with a powerful ally by your side.")
            else:
                print("\nYou decide to leave the katana, respecting the sacredness of the shrine.")
                print("As you continue your journey, the forest seems to guide and protect you, rewarding your humility with safe passage.")
        
        else:
            print("\nYou continue deeper into the forest, feeling the presence of unseen eyes watching you.")
            print("Suddenly, you are surrounded by a group of bandits. Do you (1) fight them or (2) try to negotiate?")
            bandit_choice = input(">> ").strip()

            if bandit_choice == "1":
                print("\nYou draw your sword and engage the bandits in combat. Your skills as a samurai prevail, and you defeat them.")
                print("Among the defeated bandits, you find a map leading to a hidden treasure deep within the forest.")
                print("Your bravery is rewarded as you follow the map and discover a trove of gold and ancient artifacts.")
            else:
                print("\nYou attempt to negotiate with the bandits, offering them a portion of your provisions in exchange for safe passage.")
                print("Impressed by your wisdom and generosity, the bandits agree and let you go unharmed.")
                print("As you continue your journey, you find an old hermit who shares with you the secrets of the forest, enhancing your skills and knowledge.")

    elif path == "mountain":
        print("\nYou choose the path of the mountain, the air growing colder as you ascend.")
        print("As you reach a high plateau, you encounter a wise old monk meditating. Do you (1) seek his guidance or (2) continue alone?")
        choice = input(">> ").strip()

        if choice == "1":
            print("\nYou bow before the monk and seek his wisdom. He tells you of a sacred cave at the mountain's peak, said to grant enlightenment to those who enter.")
            print("Do you (1) head to the cave or (2) stay and train with the monk?")
            monk_choice = input(">> ").strip()

            if monk_choice == "1":
                print("\nYou thank the monk and make your way to the cave. Inside, you find a serene place filled with ancient carvings and peaceful energy.")
                print("Meditating in the cave, you gain profound insights and inner strength, emerging as a samurai of unmatched wisdom and clarity.")
            else:
                print("\nYou decide to stay and train with the monk, learning ancient techniques and philosophies.")
                print("After months of rigorous training, you become a master samurai, known for both your combat skills and deep spiritual understanding.")
        
        else:
            print("\nYou continue alone, climbing higher and higher until you reach a treacherous cliff.")
            print("Do you (1) attempt to scale the cliff or (2) search for another path?")
            cliff_choice = input(">> ").strip()

            if cliff_choice == "1":
                print("\nYou gather your courage and begin to scale the cliff. Halfway up, you find a hidden ledge with an ancient scroll.")
                print("The scroll contains lost techniques of the samurai, which you master as you continue your climb, becoming a legendary warrior.")
            else:
                print("\nYou search for another path and find a hidden trail leading to a hidden village of skilled craftsmen.")
                print("The villagers, impressed by your perseverance, offer to forge you a unique, powerful weapon.")
                print("With this new weapon, you become a celebrated samurai, known for your skill and the unparalleled craftsmanship of your blade.")
    
    else:
        print("\nInvalid choice. Please restart the game and choose a valid path (forest/mountain).")

"""
Travel Itinerary Planner
Objective: Plan your futre holiday, you might be tired already :)

Input: The user enters three cities they plan to visit.
Output: The program outputs a travel itinerary in the order entered.

Input:

>> London
>> Paris
>> Rome

Output:
Your travel itinerary: London -> Paris -> Rome
"""

def travel_itinerary_planner():
    print("Welcome to the Travel Itinerary Planner!")
    
    city1 = input("Enter the first city you plan to visit: ")
    city2 = input("Enter the second city you plan to visit: ")
    city3 = input("Enter the third city you plan to visit: ")
    
    itinerary = f"{city1} -> {city2} -> {city3}"
    
    print(f"Your travel itinerary: {itinerary}")


