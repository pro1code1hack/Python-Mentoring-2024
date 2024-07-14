from datetime import datetime
from typing import List


class Workout:
    def __init__(self, date: str, exercise: str, duration: int, intensity: str) -> None:
        self.date: datetime = datetime.strptime(date, "%Y-%m-%d")
        self.exercise: str = exercise
        self.duration: int = duration  # duration in minutes
        self.intensity: str = intensity

    def calculate_calories_burned(self) -> float:
        intensity_factor = {"low": 4.0, "medium": 6.0, "high": 8.0}
        return self.duration * intensity_factor.get(self.intensity, 6.0)


class User:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.workouts: List[Workout] = []

    def add_workout(self, workout: Workout) -> None:
        self.workouts.append(workout)

    def summarize_total_activity(self) -> None:
        total_duration = sum(workout.duration for workout in self.workouts)
        total_calories = sum(workout.calculate_calories_burned() for workout in self.workouts)
        print(f"Total workout duration: {total_duration} minutes")
        print(f"Total calories burned: {total_calories:.2f}")

    def display_workouts(self) -> None:
        for workout in self.workouts:
            print(
                f"Date: {workout.date.strftime('%Y-%m-%d')}, Exercise: {workout.exercise}, Duration: {workout.duration}"
                f" minutes, Intensity: {workout.intensity}"
            )


def main() -> None:
    user: User = User("John Doe")

    # Add workouts
    user.add_workout(Workout("2024-07-01", "Running", 30, "high"))
    user.add_workout(Workout("2024-07-02", "Cycling", 45, "medium"))
    user.add_workout(Workout("2024-07-03", "Yoga", 60, "low"))

    # Display workouts
    print(f"Workouts for {user.name}:")
    user.display_workouts()

    # Summarize total activity
    print("\nSummary of total activity:")
    user.summarize_total_activity()


if __name__ == "__main__":
    main()
