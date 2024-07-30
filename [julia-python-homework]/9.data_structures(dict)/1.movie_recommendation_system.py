"""Create a simple movie recommendation system that
suggests movies to users based on their preferences."""

# Requirements:
# 1. Movie Database: Create a dictionary named movie_database where keys are movie titles and
# values are lists containing the genre(s) of each movie.
# 2. Recommendation Algorithm: Suggest a movie to a user based on their preferred genres and the
# movie database.
# The format should be something like this:
# movie_database = {
#  "Interstellar": ["Adventure", "Drama", "Sci-Fi"]
# }

movie_database = {
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "The Godfather": ["Crime", "Drama"],
    "The Shawshank Redemption": ["Drama"],
    "The Matrix": ["Action", "Sci-Fi"],
    "Fight Club": ["Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "The Lord of the Rings: The Fellowship of the Ring": ["Adventure", "Drama", "Fantasy"],
    "Star Wars: Episode IV - A New Hope": ["Action", "Adventure", "Fantasy"],
    "Back to the Future": ["Adventure", "Comedy", "Sci-Fi"],
    "Gladiator": ["Action", "Adventure", "Drama"],
    "Jurassic Park": ["Adventure", "Sci-Fi", "Thriller"],
    "The Silence of the Lambs": ["Crime", "Drama", "Thriller"],
    "Schindler's List": ["Biography", "Drama", "History"],
    "Titanic": ["Drama", "Romance"],
    "Avatar": ["Action", "Adventure", "Sci-Fi"],
    "Braveheart": ["Biography", "Drama", "History"],
    "The Lion King": ["Animation", "Adventure", "Drama"],
    "Toy Story": ["Animation", "Adventure", "Comedy"],
    "The Terminator": ["Action", "Sci-Fi"],
    "Alien": ["Horror", "Sci-Fi"],
    "Goodfellas": ["Biography", "Crime", "Drama"],
    "Saving Private Ryan": ["Drama", "War"],
    "The Prestige": ["Drama", "Mystery", "Sci-Fi"],
    "The Departed": ["Crime", "Drama", "Thriller"],
    "The Green Mile": ["Crime", "Drama", "Fantasy"],
    "Se7en": ["Crime", "Drama", "Mystery"],
    "The Usual Suspects": ["Crime", "Drama", "Mystery"],
    "American Beauty": ["Drama"],
    "The Social Network": ["Biography", "Drama"],
    "Jaws": ["Adventure", "Thriller"],
    "The Big Lebowski": ["Comedy", "Crime"],
    "Rocky": ["Drama", "Sport"],
    "E.T. the Extra-Terrestrial": ["Family", "Sci-Fi"],
    "The Sixth Sense": ["Drama", "Mystery", "Thriller"],
    "The Avengers": ["Action", "Adventure", "Sci-Fi"],
    "Guardians of the Galaxy": ["Action", "Adventure", "Comedy"],
    "Iron Man": ["Action", "Adventure", "Sci-Fi"],
    "Black Panther": ["Action", "Adventure", "Sci-Fi"],
    "Deadpool": ["Action", "Adventure", "Comedy"],
    "Spider-Man: Into the Spider-Verse": ["Animation", "Action", "Adventure"],
    "Wonder Woman": ["Action", "Adventure", "Fantasy"],
    "Mad Max: Fury Road": ["Action", "Adventure", "Sci-Fi"],
    "The Revenant": ["Action", "Adventure", "Drama"],
    "A Beautiful Mind": ["Biography", "Drama"],
    "La La Land": ["Comedy", "Drama", "Music"],
    "Slumdog Millionaire": ["Drama", "Romance"],
    "The Grand Budapest Hotel": ["Adventure", "Comedy", "Crime"]
}

user_genres = input("What are your favourite genres? Write separated by commas: ")
user_genres_set = set(user_genres.split(", "))

filtered_dict = {
    title: genres for title, genres in movie_database.items()
    if user_genres_set <= set(genres)
}
print("movie_database =", filtered_dict)

# Thriller - 5 films
# Drama, Mystery, Thriller - 1 film
# but Drama, Mystery, Thriller, Horror - is empty because none of the films has such a combination
