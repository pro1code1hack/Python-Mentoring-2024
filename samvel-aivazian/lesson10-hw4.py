# Movie database
movie_database = {
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "The Matrix": ["Action", "Sci-Fi"],
    "The Godfather": ["Crime", "Drama"],
    "Shawshank Redemption": ["Drama"],
    "The Avengers": ["Action", "Adventure", "Sci-Fi"],
    "Titanic": ["Drama", "Romance"],
    "Finding Nemo": ["Animation", "Adventure", "Comedy"]
}


def get_user_preferences() -> list:
    genres = input("Enter your preferred genres (comma separated): ")
    preferred_genres = [genre.strip() for genre in genres.split(',')]
    return preferred_genres


def recommend_movie(preferred_genres: list) -> str:
    recommendations = []
    for movie, genres in movie_database.items():
        if any(genre in genres for genre in preferred_genres):
            recommendations.append(movie)

    if recommendations:
        return recommendations
    else:
        return "No movies found matching your preferences."


def main() -> None:
    print("Welcome to the Movie Recommendation System!")
    preferred_genres = get_user_preferences()
    recommendations = recommend_movie(preferred_genres)

    if isinstance(recommendations, list):
        print("\nRecommended movies based on your preferences:")
        for movie in recommendations:
            print(movie)
    else:
        print(recommendations)


if __name__ == "__main__":
    main()
