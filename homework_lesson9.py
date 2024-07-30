"""
Movie Recommendation System
Objective: Create a simple movie recommendation system that suggests movies to users based on their preferences.

Requirements:
Movie Database: Create a dictionary named movie_database where keys are movie titles and values are lists containing the genre(s) of each movie.

Recommendation Algorithm: Suggest a movie to a user based on their preferred genres and the movie database.

The format should be something like this:

movie_database = {
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"]
}
"""


anime_database = {
    "Attack on Titan": ["Action", "Fantasy", "Drama"],
    "Death Note": ["Mystery", "Psychological", "Supernatural"],
    "Naruto": ["Action", "Adventure", "Fantasy"],
    "One Piece": ["Action", "Adventure", "Comedy"],
    "Dragon Ball Z": ["Action", "Adventure", "Fantasy"],
    "Fullmetal Alchemist: Brotherhood": ["Action", "Adventure", "Drama"],
    "My Hero Academia": ["Action", "Adventure", "Superhero"],
    "Sword Art Online": ["Action", "Fantasy", "Romance"],
    "Tokyo Ghoul": ["Horror", "Psychological", "Supernatural"],
    "Demon Slayer": ["Action", "Supernatural", "Historical"],
    "One Punch Man": ["Action", "Comedy", "Superhero"],
    "Hunter x Hunter": ["Action", "Adventure", "Fantasy"],
    "Steins;Gate": ["Sci-Fi", "Thriller", "Time Travel"],
    "Your Lie in April": ["Drama", "Romance", "Music"],
    "Clannad": ["Drama", "Romance", "Slice of Life"],
    "Neon Genesis Evangelion": ["Mecha", "Psychological", "Sci-Fi"],
    "Fairy Tail": ["Action", "Adventure", "Fantasy"],
}

def recommend_anime(preferred_genres):
    recommended_anime = []
    for anime, genres in anime_database.items():
        if any(genre in genres for genre in preferred_genres):
            recommended_anime.append(anime)
    return recommended_anime

# preferred_genres_input = input("Enter preferred genres (comma-separated): ")
# preferred_genres = [genre.strip() for genre in preferred_genres_input.split(",")]
# recommended_anime = recommend_anime(preferred_genres)

# if recommended_anime:
#     print(f"Recommended anime based on your preferences ({', '.join(preferred_genres)}):")
#     for anime in recommended_anime:
#         print(f"- {anime}")
# else:
#     print("No anime found based on your preferences.")


"""
Quiz Game
Objective: Create a flashcard quiz game that helps users learn and test their knowledge on various topics.

Requirements:
Data: Define a dictionary named flashcards where keys are questions and values are answers.

Quiz: Implement a quiz functionality that presents users with a random flashcard question and prompts them to input their answer.

Repeat: Allow the user to continue the quiz until they decide to quit.

flashcards = {
    "What is the chemical simbol for water?": "H2O",
}

"""
import random

flashcards = {
    "What does HTML stand for?": "HyperText Markup Language",
    "What is the main purpose of CSS?": "Styling and formatting web pages",
    "What is a function in programming?": "A reusable block of code that performs a specific task",
    "What does IDE stand for?": "Integrated Development Environment",
    "What is the difference between '==' and 'is' in Python?": "'==' compares the values of variables, 'is' checks if two variables point to the same object",
    "What is a variable in programming?": "A named storage location in memory",
    "What does API stand for?": "Application Programming Interface",
    "What is the difference between 'GET' and 'POST' methods in HTTP?": "'GET' retrieves data from a server, 'POST' submits data to be processed by a server",
    "What is recursion in programming?": "A technique where a function calls itself directly or indirectly",
    "What is version control?": "A system that records changes to a file or set of files over time so that you can recall specific versions later"
}

def quiz():
    while True:
        question = random.choice(list(flashcards.keys()))
        
        print("\nQuestion:", question)
        user_answer = input("Your answer: ").strip()
        
        correct_answer = flashcards[question]
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
        
        continue_quiz = input("\nDo you want to continue? (yes/no): ").lower()
        if continue_quiz != "yes":
            print("Thank you for playing!")
            break

