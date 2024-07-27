import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

movie_database = {
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "The Godfather": ["Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "The Shawshank Redemption": ["Drama"],
    "The Matrix": ["Action", "Sci-Fi"],
    "Forrest Gump": ["Drama", "Romance"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "Gladiator": ["Action", "Adventure", "Drama"],
    "Titanic": ["Drama", "Romance"]
}


def recommend_movie(preferred_genres):
    recommended_movies = []
    for movie, genres in movie_database.items():
        if any(genre in genres for genre in preferred_genres):
            recommended_movies.append(movie)
    return recommended_movies


def main():
    logging.info("Enter your preferred genres (separated by commas): ")
    preferred_genres = [genre.strip() for genre in input().split(',')]
    recommended_movies = recommend_movie(preferred_genres)
    if recommended_movies:
        logging.info("Recommended movies based on your preferences:")
        for movie in recommended_movies:
            logging.info(movie)
    else:
        logging.info("No movies found matching your preferences.")


if __name__ == "__main__":
    main()
