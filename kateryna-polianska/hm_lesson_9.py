"""
Task 1: Movie Recommendation System

Create a simple movie recommendation system that suggests movies to users based on their preferences.

"""

movie_database = {
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "Titanic": ["Drama", "Romance"],
    "The Matrix": ["Action", "Sci-Fi"],
    "The Godfather": ["Crime", "Drama"],
    "The Shawshank Redemption": ["Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "Gladiator": ["Action", "Adventure", "Drama"],
    "Avatar": ["Action", "Adventure", "Sci-Fi"]
}

def recommend_movies(preferred_genres):
    preferred_genres = [genre.strip().capitalize() for genre in preferred_genres]

    recommendations = []
    for movie, genres in movie_database.items():
        if any(genre in genres for genre in preferred_genres):
            recommendations.append(movie)
    
    return recommendations

def main():
    user_input = input("Enter your preferred genres (separated by comma): ")
    preferred_genres = user_input.split(",")
    
    recommended_movies = recommend_movies(preferred_genres)
    
    if recommended_movies:
        print(f"Recommended movies: {recommended_movies}")
    else:
        print("No movies found for the given genres.")

if __name__ == "__main__":
    main()

"""
Task 2: Quiz Game

Create a flashcard quiz game that helps users learn and test their knowledge on various topics.
"""

import random

flashcards = {
    "What is the chemical symbol for water?": "H2O",
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What planet is known as the Red Planet?": "Mars",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the largest mammal?": "Blue whale",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the tallest mountain in the world?": "Mount Everest",
    "What is the speed of light?": "299,792,458 meters per second",
    "What is the boiling point of water?": "100°C"
}

def quiz():
    questions = list(flashcards.keys())
    
    while True:
        question = random.choice(questions)
        answer = flashcards[question]
        
        print("\nQuestion:")
        user_answer = input(f"{question} ")
        
        if user_answer.strip().lower() == answer.strip().lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {answer}")
        
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

def main():
    print("Welcome to the Flashcard Quiz Game!")
    quiz()
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
