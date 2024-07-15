import logging
from typing import List, Dict

import pytest

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Movie database
movie_database: Dict[str, List[str]] = {
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


def get_user_preferences() -> List[str]:
    """Get preferred genres from the user."""
    try:
        genres = input("Enter your preferred genres (comma separated): ")
        preferred_genres = [genre.strip() for genre in genres.split(',')]
        logging.info(f"User preferences: {preferred_genres}")
        return preferred_genres
    except Exception as e:
        logging.error(f"Error getting user preferences: {e}")
        return []


def recommend_movie(preferred_genres: List[str], movie_db: Dict[str, List[str]]) -> List[str]:
    """Recommend movies based on preferred genres."""
    try:
        recommendations = [movie for movie, genres in movie_db.items() if
                           any(genre in genres for genre in preferred_genres)]
        logging.info(f"Recommendations: {recommendations}")
        return recommendations
    except Exception as e:
        logging.error(f"Error generating recommendations: {e}")
        return []


def display_recommendations(recommendations: List[str]) -> None:
    """Display movie recommendations."""
    if recommendations:
        logging.debug(f"Displaying recommendations: {recommendations}")
        print("\nRecommended movies based on your preferences:")
        for movie in recommendations:
            print(movie)
    else:
        logging.debug("No recommendations to display.")
        print("No movies found matching your preferences.")


def main() -> None:
    """Main function to run the movie recommendation system."""
    logging.info("Movie Recommendation System started.")
    preferred_genres = get_user_preferences()
    recommendations = recommend_movie(preferred_genres, movie_database)
    display_recommendations(recommendations)
    logging.info("Movie Recommendation System ended.")


def recommend_movie(preferred_genres: List[str], movie_db: Dict[str, List[str]]) -> List[str]:
    """Recommend movies based on preferred genres."""
    try:
        recommendations = [movie for movie, genres in movie_db.items() if
                           any(genre in genres for genre in preferred_genres)]
        logging.info(f"Recommendations: {recommendations}")
        return recommendations
    except Exception as e:
        logging.error(f"Error generating recommendations: {e}")
        return []


def test_recommend_movie():
    test_db = {
        "Movie1": ["Genre1", "Genre2"],
        "Movie2": ["Genre3"],
        "Movie3": ["Genre2", "Genre4"]
    }

    # Test case 1: Single genre match
    assert recommend_movie(["Genre1"], test_db) == ["Movie1"]

    # Test case 2: Multiple genre match
    assert recommend_movie(["Genre2"], test_db) == ["Movie1", "Movie3"]

    # Test case 3: No match
    assert recommend_movie(["Genre5"], test_db) == []

    # Test case 4: Multiple preferred genres
    assert recommend_movie(["Genre2", "Genre3"], test_db) == ["Movie1", "Movie2", "Movie3"]


if __name__ == "__main__":
    pytest.main()
